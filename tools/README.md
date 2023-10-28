# Album generator using Imgur as a host

This site is using Imgur to host its albums.

To facilitate the process I created this script to upload folders of images to a hidden Imgur album, while also generating thumbnails for different sizes according to what the album grid needs, getting the AR of the shot for the mentioned grid, and creating a JSON file to easily use it on the Jekyll site.

To use this simply create an Imgur account, then go to https://api.imgur.com/oauth2/addclient to register your client. Put whatever you want on the Application name and URL fields. Include an email and a short description if you want. After creating it go to https://imgur.com/account/settings/apps and copy the Client ID and the Client secret. Then, create a .env file with the following env variables:

- `CLIENT_ID`: imgurs app Client ID.
- `CLIENT_SECRET`: imgurs app Client secret.

After setting that up just simply draw the folder with the album images (without uppercase letters, spaces, or special characters) and drop it on top of this Python script. It will open your preferred web browser and ask you to authorize your Imgur account when you do it for the first time. Be sure to paste the pin it gives you after doing so to the terminal.

Do be aware that Imgur API only allows uploading around 1250 shots per day, and since we are uploading 2 thumbnails for each shot (the way the grid works it needs thumbnails with specific resolutions) you may have to wait some time between uploads. If you happen to hit a rate limit, after the time the Imgur API response told you to wait, you can draw the shots folder to the script again and it will continue upload shots from where it was left.

It's worth mentioning that Imgur's CDN seems to restrict access to images from a `127.0.0.1` referer, which means they won't load on your site when testing it locally. So try using `localhost` instead of `127.0.0.1` to be able to see these images on your 

I recommend compressing the images with [Sqoosh](https://github.com/GoogleChromeLabs/squoosh). I personally compress my images using the `mozjpeg` compression with `quality:95`:

```
squoosh-cli --mozjpeg '{quality:95}' -d out ./
```

The difference with the lossless file is barely noticeable and it tends to reduce the image size from 50% to 75%.
