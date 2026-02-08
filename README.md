Simple Python script to move images and videos into separate folders.

Requires Python 3.14+ due to using Path.move() function

Example usage:<br />
python move-video-img.py mixed_folder

Use quotation marks if the folder has a space, e.g.:<br />
python move-video-img.py "mixed folder"

Result:<br />
Images will be in mixed_folder_image (.png, .jpg, .bmp)<br />
Videos will be in mixed_folder_video (.mp4, .mkv, .avi, .wmv, .asf, .gif)<br />
Everything else will be in mixed_folder_unknown<br />
