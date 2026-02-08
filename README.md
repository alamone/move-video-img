Simple Python script to move images and videos into separate folders.

Requires Python 3.14+ due to using Path.move() function

Example usage: python move-video-img.py mixed_folder

Result:
Images will be in mixed_folder_image (.png, .jpg, .bmp)
Videos will be in mixed_folder_video (.mp4, .mkv, .avi, .wmv, .asf, .gif)
Everything else will be in mixed_folder_unknown
