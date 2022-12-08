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
    img.place(x=-20, y=40)

def newCard(my_frame, list, value):
    
    card = Label(my_frame, text=list[value])
    card.pack(pady=10)
    # return card

def callback(value):
    value+=1

def Tipp(frame, list, value):
    newKep (frame, list, list[value.get()])


def check(window, frame, card_label, list, value, tipp, tippek, joTippek, rosszTippek,mainframe):
    i = value.get()
    tippSzoveg = tipp.get()
    tippek.append(tippSzoveg)

    print('Jó tipp-e a/az', tippSzoveg, list[i-1], is_correct_guess(tippSzoveg, list[i-1]))
    if is_correct_guess(tippSzoveg, list[i-1]):
        joTippek.append(tippSzoveg)
        rightFrame = Frame(mainframe)
        rightFrame.grid(row=0, column=2,padx=(value.get(), 10))
        goodFrame = Frame(rightFrame, width=200, height=300)
        goodFrame.pack() 
        new_label = Label(rightFrame,text=list[i-1])
        new_label.pack()
        newKep(rightFrame, list, i-1)
        
        
    else:
        rosszTippek.append(tippSzoveg)
        leftFrame = Frame(mainframe)
        leftFrame.grid(row=0, column=0,padx=(value.get(), 10))
        badFrame = Frame(leftFrame, width=200,height=300)
        badFrame.pack()
        new_label = Label(leftFrame,text=list[i-1])
        new_label.pack()
        newKep(badFrame, list, i-1)
        badFrame.pack_propagate(False)
        

    tipp.set('')
    print(tippek, i)
    if (i == len(list)): 
        window.destroy()
    else:
        card_label.set(list[i])
        newKep(frame, list, i)
    value.set(i+1)

def render(eredetiSzavak):
    window = Tk()

    szavak = eredetiSzavak
    value = IntVar(window, 0)
    value.set(0)
    tippek = []
    joTippek = []
    rosszTippek = []

    window.resizable(width=FALSE, height=FALSE)
    window.geometry("1200x800")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    mainframe= Frame(window ,background="#954535",padx=100,pady=100)
    mainframe.pack()

    topframe = Frame(mainframe)
    topframe.grid(row=0, column=1,padx=(value.get(), 10))

    bottomframe = Frame(mainframe)
    bottomframe.grid(row=1, column=1,padx=(value.get(), 10))

    

   


   

    myFrame = Frame(topframe, width=202, height=325)
    myFrame.pack()
    myFrame.pack_propagate(False)

    

        
    newKep(myFrame, szavak, value.get()) # megjeleníti az elso kepet

    card_text = StringVar(window, szavak[0])
    card_name = Label(myFrame, textvariable=card_text)
    card_name.pack(pady=10)
    value.set(1)

    

   

    tipp = StringVar()
    entry = Entry(bottomframe, textvariable=tipp ,width=33)
    entry.pack()
    entry.bind('<Return>', lambda event: check(window, myFrame, card_text, szavak, value, tipp, tippek, joTippek, rosszTippek,mainframe))
    button = Button(bottomframe, text="tipp", command=lambda: check(window, myFrame, card_text, szavak, value, tipp, tippek, joTippek, rosszTippek,mainframe))
    button.pack()

    window.mainloop()

    return {
        "tippek": tippek,
        "joTippek": joTippek,
        "rosszTippek": rosszTippek
    }

if __name__ == "__main__": 
    render(['idő', 'asztal', 'almalé', 'cápa', 'cukor'])
    