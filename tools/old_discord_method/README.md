# Album generator using discord as a host

This site is using discord to host its albums.

To facilitate the process I created this script to upload folders of images to a dump discord channel/server, while also generating thumbnails for different sizes according to what the albums grid need, getting the AR of the shot for the mentioned grid, and creating a json file to easily use it on the Jekyll site.

To use this simply create a .env file with the following env variables:
- `DISCORD_TOKEN`: the discord bot's token.
- `DISCORD_SERVER`: The name of the server to which the channel belongs.
- `DISCORD_CHANNEL`: The name of the channel in which you will be saving the screenshots.

Keep in mind that if the channel or the server gets deleted so will the images.

I recommend compressing the images with [Sqoosh](https://github.com/GoogleChromeLabs/squoosh). I personally compress my images using the `mozjpeg` compression with `quality:95`:

```
squoosh-cli --mozjpeg '{quality:95}' -d out ./
```

The difference with the lossless file is barely noticeable and it tends to reduce the image size from 50% to 75%.