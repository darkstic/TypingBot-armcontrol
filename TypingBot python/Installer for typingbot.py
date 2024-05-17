import os
import subprocess
import sys
import shutil

username = os.environ.get("USERNAME") or os.environ.get("USER")

def move_tesseract():
    source_folder_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\tesseract"
    destination_folder_path = "C:\\TypingBotAssets"

    try:
        shutil.move(source_folder_path, destination_folder_path)
        print(f"Folder moved successfully from {source_folder_path} to {destination_folder_path}")
    except Exception as e:
        print(f"Error moving folder: {e}")


def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print(f"Folder created at {folder_path}")
    except FileExistsError:
        print(f"Folder already exists at {folder_path}")

if __name__ == "__main__":
    folder_path = "C:\\TypingBotAssets"

    create_folder(folder_path)



def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error installing package '{package_name}'.")

if __name__ == "__main__":
    package_to_install = "mymodule"  
    install_package(package_to_install)



if __name__ == "__main__":
    package_to_install = "pytesseract"  
    install_package(package_to_install)
    # sys.path.insert(0, r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe")


if __name__ == "__main__":
    package_to_install = "pyscreenshot"  
    install_package(package_to_install)

if __name__ == "__main__":
    package_to_install = "serial"  
    install_package(package_to_install)

if __name__ == "__main__":
    package_to_install = "tesseract"  
    install_package(package_to_install)
    sys.path.insert(0, f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\tesseract\\__pycache__")
    move_tesseract()

