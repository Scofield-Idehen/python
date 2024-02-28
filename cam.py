import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os
import threading
import time
import datetime


# Create output directory
output_dir = "spycam_output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Initialize camera
cap = cv2.VideoCapture(0)

# Create GUI 
root = tk.Tk()
root.title("My Spy Cam")  

btn_photo = tk.Button(root, text="Take Photo")
btn_video = tk.Button(root, text="Record Video")
btn_quit = tk.Button(root, text="Quit") 

btn_photo.pack()  
btn_video.pack()
btn_quit.pack()

# Global variables
output_path = ""
output_video = None

# Functions
def take_photo():
    print("Taking photo!")
    
    ret, frame = cap.read()  
    if ret:
        now = datetime.datetime.now()  
        filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
        path = os.path.join(output_dir, filename)
        
        cv2.imwrite(path, frame)   

def start_recording():
   global output_path, output_video  
        
   now = datetime.datetime.now() 
   filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".avi"
    
   output_path = os.path.join(output_dir, filename)   
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
   output_video = cv2.VideoWriter(output_path, fourcc, 20.0, (640,480))
   
def stop_recording():
   global output_video
    
   output_video.release()
   output_video = None 
   
# Bind buttons to functions   
btn_photo.config(command=take_photo)  
btn_video.config(command=start_recording)

root.mainloop()