import tkinter
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
from tkinter import *
def get_image():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, f"{id_entry.get()}")
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic =ImageTk.PhotoImage(image)

# Create the main window
window =Tk()
window.geometry("400x250")  # Set window size
window.title('InstalDownloader')
label1=tkinter.Label(window,text="write your id") # a statice text
label1.pack()
id_entry = tkinter.Entry(window)
id_entry.pack()
sub_button = tkinter.Button(window,text="Submit",command=get_image)
sub_button.pack()

window.mainloop()

