import os
import shutil
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

def organize_directory(directory_path):
    """Organizes files in the given directory by sorting them into categorized subfolders."""
    if not os.path.exists(directory_path):
        print("Error: The specified directory does not exist.")
        return
    for category, extensions in FILE_CATEGORIES.items():
        category_folder = os.path.join(directory_path, category)
        os.makedirs(category_folder, exist_ok=True)

        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path) and any(file_name.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(category_folder, file_name))
                print(f"Moved: {file_name} -> {category}")
    print("File organization completed successfully!")
if __name__ == "__main__":
    target_directory = input("Enter the path to the folder you want to organize: ")
    organize_directory(target_directory)
