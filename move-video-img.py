# move video and image to separate folders
# requires Python 3.14+ due to using Path.move()

import argparse
from pathlib import Path

if __name__ == "__main__":
    
    p = argparse.ArgumentParser(description='move video and image to separate folder')
    p.add_argument('folder_name', type=str, help='folder name to split')
    args = p.parse_args()

    start_directory = Path(args.folder_name)
    for item_path in start_directory.rglob('*'):
        if item_path.is_file():
            extension = item_path.suffix.lower()
            match extension:
                case ".jpg":
                    item_type = "image"
                case ".png":
                    item_type = "image"
                case ".bmp":
                    item_type = "image"
                case ".mp4":
                    item_type = "video"
                case ".mkv":
                    item_type = "video"
                case ".avi":
                    item_type = "video"
                case ".wmv":
                    item_type = "video"
                case ".asf":
                    item_type = "video"
                case ".gif":
                    item_type = "video"                    
                case _:
                    item_type = "unknown"                 
            
            path_parts = item_path.parts
            new_path = args.folder_name + "_" + item_type
            for i in range(1, len(path_parts) - 1):
                new_path = new_path + "\\" + path_parts[i]
            new_file = new_path + "\\" + path_parts[len(path_parts) - 1]
            target_path = Path(new_path)
            target_file = Path(new_file)
            
            target_path.mkdir(0o777, True, True) #create target path
                        
            result_path = item_path.move(new_file)
            print (f"{item_path} moved to {result_path}")
