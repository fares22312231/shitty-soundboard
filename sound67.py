import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk


pygame.mixer.init()

def on_click():
    pygame.mixer.music.load("/home/fschool/Downloads/dry-fart.mp3")
    pygame.mixer.music.play() 



def on_click3():
    pygame.mixer.music.load("/home/fschool/Downloads/fahhhhhhhhhhhhhhh.mp3")
    pygame.mixer.music.play()

def on_click4():
    pygame.mixer.music.load("/home/fschool/Downloads/[2188317559] SlipONBLEAT - yes_chef.mp3")
    pygame.mixer.music.play()

def on_click5():
    pygame.mixer.music.load("/home/fschool/Downloads/wombo-combo_2.mp3")
    pygame.mixer.music.play()

def on_click6():
    pygame.mixer.music.load("/home/fschool/Downloads/wow-mlg-sound-effect.mp3")
    pygame.mixer.music.play()

root = tk.Tk()
root.title("soundboard")
root.geometry("1440x900")
bg_image = Image.open("/home/fschool/Downloads/SON.jpeg")  
bg_image = bg_image.resize((1440, 900))  
bg_photo = ImageTk.PhotoImage(bg_image)


bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

bg_label.image = bg_photo


button = tk.Button(root, text="fart", command=on_click)
button.pack()



buttom3 = tk.Button(root, text="FAH", command=on_click3)
buttom3.pack()

button4 = tk.Button(root, text="yes_chef", command=on_click4)
button4.pack()

button5 = tk.Button(root, text="WOMBOCOMBO", command=on_click5)
button5.pack()


button6 = tk.Button(root, text="wow.mlg", command=on_click6)
button6.pack()





root.mainloop() 


#all rights reserved for the () on line 48 to saud zaid almuqbeel 

