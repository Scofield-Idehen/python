import tkinter as tk
import cv2
from PIL import Image, ImageTk  
import datetime
import os

# Get home directory and create output dir
output_dir = os.path.join(os.path.expanduser("~"), "spycam_output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Saving photos and videos to: {output_dir}")  

# Initialize Camera 
cap = cv2.VideoCapture(0)

# GUI Window 
root = tk.Tk()
root.title("My Spy Camera")

# Buttons
btn_take_photo = tk.Button(root, text="Take Photo") 
btn_record_video = tk.Button(root, text="Record Video")
btn_quit = tk.Button(root, text="Quit")

btn_take_photo.pack()
btn_record_video.pack()  
btn_quit.pack()

# Variables
output_video_path = ""  
output_video_writer = None

# Functions  

def take_photo():
    
    print("Taking photo...")

    ret, frame = cap.read()
    
    if ret:
      
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  
        filename = f"spycam_photo_{timestamp}.jpg"
        
        output_file = os.path.join(output_dir, filename)
        print(f"Saving photo to {output_file}")
        
        cv2.imwrite(output_file, frame)

# Video Recording Functions  


output_path = ""
output_video = None

def start_recording():
    global output_path, output_video
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".avi"    
    output_path = os.path.join(output_dir, filename)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter(output_path, fourcc, 20.0, (640,480))

def stop_recording():
    output_video.release()
    
# Bind Buttons
btn_take_photo.config(command=take_photo)
btn_record_video.config(command=start_recording)

root.mainloop()