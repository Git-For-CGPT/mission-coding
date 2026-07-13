import os
import shutil

def move_file(file, destination_folder):
    file_path = os.path.join(folder_path, file)
    destination_path = os.path.join(destination_folder, file)
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    shutil.move(file_path, destination_path)

print("Smart File Organizer Started!")

folder_path = input("Enter the folder path to organize: ")

for file in os.listdir(folder_path):
    print(file)
    filename, extension = os.path.splitext(file)

    if extension in (".png", ".jpg", ".jpeg"):
        destination_folder = os.path.join(folder_path, "Images")
        move_file(file, destination_folder)

    elif extension in (".pdf", ".txt", ".docx"):
        destination_folder = os.path.join(folder_path, "Documents")
        move_file(file, destination_folder)

    elif extension in (".mp3", ".wav", ".flac"):
        destination_folder = os.path.join(folder_path, "Music")
        move_file(file, destination_folder)

    elif extension in (".mp4", ".mkv", ".avi"):
        destination_folder = os.path.join(folder_path, "Videos")
        move_file(file, destination_folder)

    elif extension in (".zip", ".rar", ".7z"):
        destination_folder = os.path.join(folder_path, "Archives")
        move_file(file, destination_folder)

    elif extension in (".py", ".java", ".cpp", ".html", ".css", ".js"):
        destination_folder = os.path.join(folder_path, "Code files")
        move_file(file, destination_folder)