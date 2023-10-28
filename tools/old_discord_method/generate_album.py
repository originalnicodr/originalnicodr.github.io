from PIL import Image, ImageFilter
import os
import sys
import json
from dotenv import load_dotenv
import time
import discord

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

async def generate_album(directory_name):
    album = []
    for dirpath,_,filenames in os.walk(directory_name):
        for file_name in filenames:
            img = {}
            print(file_name)
            absolute_path = os.path.abspath(os.path.join(dirpath, file_name))
            
            img['imageFull-link'] = await upload_shot(absolute_path)

            img_600 = createthumbnail(absolute_path, 600)
            img['thumbnail-link'] = await upload_shot(img_600)

            img_1080 = createthumbnail(absolute_path, 1080)
            img['image1080-link'] = await upload_shot(img_1080)

            img['aspect-ratio'] = str(get_ar(absolute_path))

            album.append(img)
    
    with open(directory_name + '.json', 'w') as f:
        json.dump(album, f, indent=4)


intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot started successfully!")
    try:
        directory_name = sys.argv[1]
    except:
        print('Please pass directory_name')
        sys.exit()

    await generate_album(directory_name)
    print(f"Album {directory_name} created successfully!")
    time.sleep(3)

def _get_upload_channel():
    for g in bot.guilds:
        if g.name == DISCORD_SERVER:
            return discord.utils.get(g.channels, name=DISCORD_CHANNEL)

async def upload_shot(file_name):
    dump_channel = _get_upload_channel()

    uploaded_shot = await dump_channel.send(file=discord.File(file_name))
    return uploaded_shot.attachments[0].url


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_SERVER = os.getenv('DISCORD_SERVER')
DISCORD_CHANNEL = os.getenv('DISCORD_CHANNEL')

bot.run(DISCORD_TOKEN)