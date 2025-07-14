import os
import shutil


#File categories and their extensions

FILE_TYPES = {
    "Images" : [ '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents" : ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Audio" : ['.mp3', '.wav', '.aac','.flac'],
    "Videos" : ['.mp4', '.mov', '.avi', '.mkv'],
    "Archives" : ['.zip', '.rar', '.tar', '.gz', '.7z'],
    "Scripts" : [".py", '.js', '.sh', '.css', '.bat', '.html'],
    "Others" : []
}

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory")
        return
    # create folder for each category if they dont exist

    for category in FILE_TYPES.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterater through items in the folder
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    shutil.move(filepath, os.path.join(folder_path, category, filename))
                    moved = True
                    print(f"Moved '{filename}' to '{category}/ '")
                    break
            
            if not moved:
                shutil.move(filepath, os.path.join(folder_path, "Others", filename))
                print(f"Moved '{filename}' to 'Others/' ")
    print("Folder Organized!!")

if __name__ =="__main__":
    folder = input("Enter the full path of the folder to organize:\n")
    organize_files(folder)