import numpy as np
import math
import cv2
import os
import traceback
import tkinter as tk
from PIL import Image, ImageTk
import urllib.request

class Application:

    def __init__(self):
        self.url = 'http://192.168.81.22/cam-hi.jpg'
        self.vs = cv2.VideoCapture(self.url)
        self.current_image = None

        self.root = tk.Tk()
        self.root.title("Live Camera Feed")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("1600x900")
        self.background_image = Image.open("bg_image.jpeg")
        self.background_image = self.background_image.resize((1550, 800), Image.ANTIALIAS)  # Resize the image to fit the window
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.header_label = tk.Label(self.root, text="Live Camera Feed ", font=("Courier", 30, "bold"), bg='#f0f0f0')  # Light gray background color
        self.header_label.pack(pady=10)

        self.panel = tk.Label(self.root, bg='#f0f0f0')  # Light gray background color
        self.panel.pack()

        self.video_loop()

    def video_loop(self):
        try:
            img_res = urllib.request.urlopen(self.url)
            imgnp = np.array(bytearray(img_res.read()), dtype=np.uint8)
            frame = cv2.imdecode(imgnp, 1)
            frame = cv2.resize(frame, (640, 480))
            cv2image = cv2.flip(frame, 1)
            cv2image_rgb = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGB)
            self.current_image = Image.fromarray(cv2image_rgb)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.configure(image=imgtk)

        except Exception:
            print("==", traceback.format_exc())
        finally:
            self.root.after(10, self.video_loop)

    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()

print("Starting Application...")
(Application()).root.mainloop()
