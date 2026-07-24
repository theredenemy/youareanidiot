import os
import tkinter as tk
import tkinter.messagebox as msgbox
import pygame
import sys
import random
from PIL import Image, ImageTk

close_attempts = 0
def load_img(img_file, width, height):
    try:
        img = ImageTk.PhotoImage(Image.open(os.path.join(sys._MEIPASS, "resources", img_file)).resize(size=(width, height)))
    except AttributeError:
        img = ImageTk.PhotoImage(Image.open(os.path.join("resources", img_file)).resize(size=(width, height)))
    return img



def create_window(root=None, w=357, h=322, x_off=10, y_off=10, title="Idiot!"):
    if root is None:
        window = tk.Tk()
        main_root = window
    else:
        window = tk.Toplevel(root)
        main_root = root
    
    pygame.mixer.init()
    try:
        youareanidiot_audio = pygame.mixer.Sound(os.path.join(sys._MEIPASS, "resources", "youare.mp3"))
    except AttributeError:
        youareanidiot_audio = pygame.mixer.Sound(os.path.join("resources", "youare.mp3")) 
    
    window.title(title)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_pos = (screen_width - w) // 2
    y_pos = (screen_height - h) // 2
    img1 = load_img("0001.png", width=w, height=h)
    img2 = load_img("0005.png", width=w, height=h)
    idiot_label = tk.Label(window, width=w, height=h)
    idiot_label.pack()
    window.focus()
    def animate(state=False):
        img_set = img2 if state else img1
        idiot_label.config(image=img_set)

        idiot_label.image = img_set

        window.after(400, animate, not state)
    def newXlt():
        nonlocal x_off
        x_off = -(random.randint(1, 6) * 5 + 5)
    def newXrt():
        nonlocal x_off
        x_off = random.randint(1, 6) * 5 + 5
    def newYup():
        nonlocal y_off
        y_off = -(random.randint(1, 6) * 5 + 5)
    def newYdn():
        nonlocal y_off
        y_off = random.randint(1, 6) * 5 + 5
    def playBall():
        nonlocal x_pos
        nonlocal y_pos
        x_pos += x_off
        y_pos += y_off

        if x_pos > screen_width - w:
            newXlt()
        elif x_pos < 0:
            newXrt()
        
        if y_pos > screen_height - h:
            newYup()
        elif y_pos < 0:
            newYdn()
        
        window.geometry(f"{w}x{h}+{x_pos}+{y_pos}")
        
        window.after(16, playBall)
    def on_close():
        global close_attempts
        for i in range(3):
            create_window(root=main_root)
        youareanidiot_audio.stop()
        window.destroy()
        if close_attempts >= 3:
            close_attempts = 0
            msgbox.showwarning("Message!", "You are an idiot!")
        else:
            close_attempts += 1
    window.protocol("WM_DELETE_WINDOW", on_close)

    animate()
    playBall()
    youareanidiot_audio.play(loops=-1)
    return window
def start():
    root = tk.Tk()
    root.withdraw()
    
    create_window(root=root, w=800, h=600, x_off=5, y_off=5, title="You Are An Idiot!")
    
    root.mainloop()

def main():
    start()

if __name__ == "__main__":
    main()


    




