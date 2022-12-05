from tkinter import *
import random
from PIL import Image, ImageTk

def readszavak():
    szavak = []
    file1 = open('szavak.txt', 'r',encoding='utf-8')
    Lines = file1.readlines()
    for line in Lines:
        szavak.append(line.strip())
    
    return szavak

def get_5_szo():
    selected_choices=[]
    szavak = readszavak()
    for _ in range(5):
        choice = random.choice(szavak)
        szavak.remove(choice)
        selected_choices.append(choice)
        print(len(szavak))

    return selected_choices

def render():
    szavak = get_5_szo()

    window = Tk()

    window.resizable(width=FALSE, height=FALSE)
    window.geometry("800x800")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    for i in range(5):
        my_frame = Frame(window, width=200,height=300)
        my_frame.pack(pady=200, expand=True)
        my_frame.pack_propagate(False)
        load = Image.open("parrot.jpg")
        resize_image = load.resize((250, 250))

        render = ImageTk.PhotoImage(resize_image)
        img = Label(my_frame, image=render)
        img.image = render
        img.place(x=-20, y=30)

        card_name = Label(my_frame, text=szavak[i])
        card_name.pack(pady=10)

        entry = Entry(my_frame,width=50)
        entry.pack(pady=100)
        
    
    

    

    
    

    window.mainloop()

render()