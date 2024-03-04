import os
import json
import sys
import time
import webbrowser

from dotenv import load_dotenv, set_key
import pyimgur
from PIL import Image, ImageFilter

def file_name_without_file_extension(file_name):
    return os.path.splitext(file_name)[0]

def get_ar(file_name):
    with Image.open(file_name) as shot:
        h = shot.height
        w = shot.width
        return w/h

def createthumbnail(file_path, size):
    with Image.open(file_path) as shot:
        h = shot.height
        w = shot.width
        ar=w/h

        #Flickr method
        ht = size
        wt = int(ar*size)


        shot = shot.convert('RGB')#to save it in jpg
        shot = shot.filter(ImageFilter.SHARPEN)
        
        #filter algorithms
        #Image.NEAREST, Image.BILINEAR, Image.BICUBIC, Image.ANTIALIAS
        shot=shot.resize((wt,ht),Image.Resampling.LANCZOS)

        folder, file_name = os.path.split(file_path)

        newpath = f'{folder}\\thumbnails' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        saved_filename = f"{folder}\\thumbnails\\{file_name_without_file_extension(file_name)}-{str(size)}.jpg"

        shot.save(saved_filename, "JPEG", quality=95)

        return saved_filename

def upload_shot(file_path, imgur_album, im):
    uploaded_image = im.upload_image(file_path, album=imgur_album)
    return uploaded_image

def is_shit_in_album(file_name, album):
    for img in album:
        #print(f"is {file_name} inside {img['file_name']}?")
        if file_name in img["file_name"]:
            return True
    return False

def generate_album(directory_name, im):
    imgur_album = im.create_album(directory_name)
    album = []

    if os.path.exists(directory_name + '.json'):
        with open(directory_name + '.json') as json_file:
            album = json.load(json_file)
            print("Continuing previous uploading session.")

    for dirpath,_,filenames in os.walk(directory_name):
        for file_name in filenames:

            if is_shit_in_album(file_name, album):
                print(f"{file_name} uploaded in previous session, skipping...")
                continue
            
            img = {}
            img['file_name'] = file_name
            print(file_name)
            absolute_path = os.path.abspath(os.path.join(dirpath, file_name))

            imgur_image = upload_shot(absolute_path, imgur_album, im)
            
            img['imageFull-link'] = imgur_image.link

            # Imgur thumbnails have a lot of limitations that we don't want to deal with, so we are making them ourselves.
            # img['thumbnail-link'] = imgur_image.link_large_thumbnail
            # img['image1080-link'] = imgur_image.link_huge_thumbnail

            print("Sleeping 50s to avoid hitting the API rate limit.")
            time.sleep(50)

            print("Uploading first thumbnail.")
            img_600 = createthumbnail(absolute_path, 600)
            img['thumbnail-link'] = upload_shot(img_600, imgur_album, im).link
            print("Sleeping 50s to avoid hitting the API rate limit.")
            time.sleep(50)

            print("Uploading second thumbnail.")
            img_1080 = createthumbnail(absolute_path, 1080)
            img['image1080-link'] = upload_shot(img_1080, imgur_album, im).link
            print("Sleeping 50s to avoid hitting the API rate limit.")
            time.sleep(50)

            img['aspect-ratio'] = str(get_ar(absolute_path))

            album.append(img)
    
            with open(directory_name + '.json', 'w') as f:
                json.dump(album, f, indent=4)

def imgur_log():
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    ACCES_TOKEN = os.getenv('ACCES_TOKEN')
    REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

    im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET, ACCES_TOKEN, REFRESH_TOKEN)

    if not im.is_authenticated:
        if REFRESH_TOKEN:
            print("Access token expired, requesting another.")
            im.refresh_access_token()
        else:
            auth_url = im.authorization_url('pin')
            webbrowser.open(auth_url)
            pin = input("What is the pin? ")
            access_token, refresh_token = im.exchange_pin(pin)
            
            set_key(dotenv_path=".env", key_to_set="REFRESH_TOKEN", value_to_set=refresh_token)
            set_key(dotenv_path=".env", key_to_set="ACCES_TOKEN", value_to_set=access_token)
    return im

if __name__ == "__main__":
    load_dotenv()
    try:
        directory_name = sys.argv[1]
    except:
        print('Please pass directory_name')
        sys.exit()

    im = imgur_log()
    generate_album(directory_name, im)
    print(f"Album {directory_name} created successfully!")
    time.sleep(3)
