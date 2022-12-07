from tkinter import *
import random
from PIL import Image, ImageTk
from guess_checker import is_correct_guess
import os
my_path = os.path.abspath(os.path.dirname(__file__))

def newKep (my_frame, szavak, value):
    
    load = Image.open(my_path+"/kepek/"+szavak[value]+".jpg") # csak .jpg képekkel működik, de elég a szót átadni
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
    newKep (frame, list, list[value.get()])


def check(window, frame, card_label, list, value, tipp, eredetiSzo, tippek):
    print(tipp.get(), eredetiSzo, is_correct_guess(tipp.get(), eredetiSzo))
    i = value.get()
    print(value.get())
    newKep(frame, list, i)
    card_label.set(list[i])
    tippek.append(tipp.get())
    tipp.set('')
    print(tippek, i)
    if (i == len(list)-1): 
        window.destroy()
    value.set(i+1)

def render(eredetiSzavak):
    window = Tk()
    
    szavak = eredetiSzavak
    value = IntVar(window, 0)
    value.set(0)
    tippek = []

    window.resizable(width=FALSE, height=FALSE)
    window.geometry("800x800")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    mainframe= Frame(window ,background="#954535",padx=100,pady=100)
    mainframe.pack()

    topframe = Frame(mainframe)
    topframe.grid(row=0, column=1,padx=(value.get(), 10))

    bottomframe = Frame(mainframe)
    bottomframe.grid(row=1, column=1,padx=(value.get(), 10))

    leftFrame = Frame(mainframe)
    leftFrame.grid(row=0, column=0,padx=(value.get(), 10))

    rightFrame = Frame(mainframe)
    rightFrame.grid(row=0, column=2,padx=(value.get(), 10))


    badFrame = Frame(leftFrame, width=200,height=300)
    badFrame.pack()
    badFrame.pack_propagate(False)

    myFrame = Frame(topframe, width=202, height=325)
    myFrame.pack()
    myFrame.pack_propagate(False)

    goodFrame = Frame(rightFrame, width=200, height=300)
    goodFrame.pack()

        
    newKep(myFrame, szavak, value.get()) # megjeleníti az elso kepet

    card_text = StringVar(window, szavak[0])
    card_name = Label(myFrame, textvariable=card_text)
    card_name.pack(pady=10)
    value.set(1)

    badCard = Label(leftFrame, text= "Helytelen")
    badCard.pack()

    goodCard = Label(rightFrame, text="Helyes")
    goodCard.pack()

    tipp = StringVar()
    entry = Entry(bottomframe, textvariable=tipp ,width=33)
    entry.pack()
    button = Button(bottomframe, text="tipp leadás", command=lambda: check(window, myFrame, card_text, szavak, value, tipp, szavak[value.get()], tippek))
    button.pack()

    print(tipp.get())

    window.mainloop()

    return tippek

if __name__ == "__main__": 
    render(['idő', 'asztal', 'almalé', 'cápa', 'cukor'])
    