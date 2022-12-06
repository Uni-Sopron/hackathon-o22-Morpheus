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

def newKep (my_frame, name):
    load = Image.open(name + ".jpg") # csak .jpg képekkel működik, de elég a szót átadni
    resize_image = load.resize((250, 250))
    render = ImageTk.PhotoImage(resize_image)
    img = Label(my_frame, image=render)
    img.image = render
    # img.place(x=-20, y=60)
    img.place(x=-20, y=60)

def newCard(my_frame, list, value):
    card = Label(my_frame, text=list[value])
    card.pack(pady=10)
    # return card

def callback(value):
    value+=1

def Tipp(frame, list, value):
    newKep (frame, list[value])


def check(frame, card_name, list, value):
    newKep(frame, list[value])
    card_name.destroy()
    newCard(frame, list, value)

# def check(frame, card_name, list, value):
#     newKep(frame, list[value])
#     card_name.destroy()
#     newCard(frame, list, value)
#     if rossztipp:
#         Tipp(leftFrame, list, value-1)
#     else:
#         Tipp(rightFrame, list, value-1)


def render():
    value = 0
    # szavak = get_5_szo()
    szavak = ["parrot", "dog"]
    tippek = []

    window = Tk()

    window.resizable(width=FALSE, height=FALSE)
    window.geometry("800x800")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    mainframe= Frame(window ,background="#954535",padx=100,pady=100)
    mainframe.pack()

    topframe = Frame(mainframe)
    topframe.grid(row=0, column=1,padx=(value, 10))

    bottomframe = Frame(mainframe)
    bottomframe.grid(row=1, column=1,padx=(value, 10))

    leftFrame = Frame(mainframe)
    leftFrame.grid(row=0, column=0,padx=(value, 10))

    rightFrame = Frame(mainframe)
    rightFrame.grid(row=0, column=2,padx=(value, 10))


    for i in range(1): # while len(szavak)?
        badFrame = Frame(leftFrame, width=200,height=300)
        badFrame.pack()
        badFrame.pack_propagate(False)

        myFrame = Frame(topframe, width=202, height=325)
        myFrame.pack()
        myFrame.pack_propagate(False)

        goodFrame = Frame(rightFrame, width=200, height=300)
        goodFrame.pack()

        # load = Image.open("parrot.jpg")
        # resize_image = load.resize((250, 250))

        # render = ImageTk.PhotoImage(resize_image)
        # img = Label(my_frame, image=render)
        # img.image = render
        # img.place(x=-20, y=60)

        newKep(myFrame, "parrot") # megjeleníti a papagáj képet

        # name = newCard(myFrame, szavak, value)

        card_name = Label(myFrame, text=szavak[value])
        card_name.pack(pady=10)

        badCard = Label(leftFrame, text= "Helytelen")
        badCard.pack()

        goodCard = Label(rightFrame, text="Helyes")
        goodCard.pack()


        entry = Entry(bottomframe,width=33)
        entry.pack()
        button = Button(bottomframe, text="tipp leadás", command=lambda: check(myFrame, card_name, szavak, value))
        button.pack()

        value+=1

    window.mainloop()

render()
    
