from PIL import Image
import pytesseract
import pyscreenshot as ImageGrab
import os
import time
import ctypes
import serial

testing=True

username = os.environ.get("USERNAME") or os.environ.get("USER")

if testing==True:
    time.sleep(5)

bulky=[]
#///////////////////////////////////////////////////////////////////////
def send_to_arduino(character):
    arduino_port = 'COM3'  # Change this to your actual COM port
    ardu = serial.Serial(arduino_port, 9600, timeout=0.1)
    time.sleep(1)
    ardu.write(character.encode())
    time.sleep(1)
    ardu.close()

def character_split(exSentence):
    char_list = list(exSentence)  # Split the sentence into individual characters
    for char in char_list:
        send_to_arduino(char)
        print(char)
        time.sleep(0.1)  # Add a slight delay between characters

#/////////////  Screenshot /////////////////////////////////

print("Current working directory:", os.getcwd())

save_path="C:\\TypingBotAssets\\active_image.png"

screenshot= ImageGrab.grab(bbox=())# Set capture region later
screenshot.save(save_path)

#/////////////////////////////////////////////////////////////////////////////////

time.sleep(0.2)

#///////////////// Text ID //////////////////////////////////////////
path_to_tesseract = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\tesseract\\__pycache__"
image_path = "C:\\TypingBotAssets\\active_image.png"  
img = Image.open(image_path)

pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
extracted_text = pytesseract.image_to_string(img)

print("Extracted text:")
finalText=extracted_text[:-1] 

#///////////////////////////////////////////////////////////////////////////////

time.sleep(0.2)

#/////////////// Cleanup /////////////////////////////////////////////////////

try:
    os.remove(save_path)
    print(f"File '{save_path}' deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{save_path}' not found.")

#///////////////////////////////////////////////////////////////////////////////

character_split(finalText)
time.sleep(1)
# send_to_arduino(finalText)
