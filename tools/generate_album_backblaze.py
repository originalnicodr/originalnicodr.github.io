import os
import json
import sys
import time

from b2sdk.v2 import B2Api, InMemoryAccountInfo
import shutil

from dotenv import load_dotenv, set_key
from PIL import Image, ImageFilter

load_dotenv()
BACKBLAZE_KEY = os.environ.get("BACKBLAZE_KEY")
BACKBLAZE_KEY_ID = os.environ.get("BACKBLAZE_KEY_ID")
BACKBLAZE_SCREENSHOTS_FOLDER_NAME = os.environ.get("BACKBLAZE_SCREENSHOTS_FOLDER_NAME")
BACKBLAZE_BUCKET_NAME = os.environ.get("BACKBLAZE_BUCKET_NAME")

print(BACKBLAZE_SCREENSHOTS_FOLDER_NAME)

info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", BACKBLAZE_KEY_ID, BACKBLAZE_KEY)

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
        #saved_filename = f"/thumbnails/{file_name_without_file_extension(file_name)}-{str(size)}.jpg"

        shot.save(saved_filename, "JPEG", quality=95)

        return f"thumbnails/{file_name_without_file_extension(file_name)}-{str(size)}.jpg"

def upload_shot(file_name, album_path, is_thumbnail):
    album_folder = os.path.basename(os.path.normpath(album_path))
    local_file_path = f'{album_path}/{file_name}'
    b2_file_name = f'{BACKBLAZE_SCREENSHOTS_FOLDER_NAME}/{album_folder}/{file_name}' if not is_thumbnail else f'{BACKBLAZE_SCREENSHOTS_FOLDER_NAME}/{album_folder}/thumbnails/{file_name}'

    print(album_folder)
    print(local_file_path)

    bucket = b2_api.get_bucket_by_name(BACKBLAZE_BUCKET_NAME)
    uploaded_file = bucket.upload_local_file(
            local_file=local_file_path,
            file_name=b2_file_name,
    )

    print(uploaded_file.id_)

    file_url = b2_api.get_download_url_for_fileid(uploaded_file.id_)
    return file_url

def generate_album(directory_name):
    album = []

    if os.path.exists(directory_name + '.json'):
        with open(directory_name + '.json') as json_file:
            album = json.load(json_file)
            print("Continuing previous uploading session.")

    for dirpath,_,filenames in os.walk(directory_name):
        for file_name in filenames:
            
            img = {}
            img['file_name'] = file_name
            print(file_name)
            absolute_path = os.path.abspath(os.path.join(dirpath, file_name))

            img['imageFull-link'] = upload_shot(file_name, dirpath, False)

            print("Uploading first thumbnail.")
            img_600 = createthumbnail(absolute_path, 600)
            img['thumbnail-link'] = upload_shot(img_600, dirpath, True)

            print("Uploading second thumbnail.")
            img_1080 = createthumbnail(absolute_path, 1080)
            img['image1080-link'] = upload_shot(img_1080, dirpath, True)

            img['aspect-ratio'] = str(get_ar(absolute_path))

            album.append(img)
    
            with open(directory_name + '.json', 'w') as f:
                json.dump(album, f, indent=4)

if __name__ == "__main__":
    load_dotenv()
    try:
        directory_name = sys.argv[1]
    except:
        print('Please pass directory_name')
        sys.exit()

    thumbnails_path = os.path.join(directory_name, 'thumbnails')
    if os.path.exists(thumbnails_path) and os.path.isdir(thumbnails_path):
        shutil.rmtree(thumbnails_path)

    generate_album(directory_name)
    print(f"Album {directory_name} created successfully!")
    time.sleep(3)
