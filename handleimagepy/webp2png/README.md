# webp2png

A simple toolkit for converting [webp image files](https://developers.google.com/speed/webp/) to png format.

Includes 0.6.0 [dwebp](https://developers.google.com/speed/webp/download?csw=1) Linux binary for converting images. You can use newer/older ones by simply replacing it.

Make sure the dewbp binary applies to your current system(Linux, Windows or OS X), otherwise an error "cannot execute binary file" will be threw.

Usage: `python3 webp2png.py [directory_full_of_images_to_convert]`

To use webp2png on Windows or Mac, download appropriate binary and change `dwebppath` in webp2png.py to match your new path.

## License
Code in this project is licensed under [GNU GPLv3 license](https://github.com/zigapk/webp2png/blob/master/LICENSE).
