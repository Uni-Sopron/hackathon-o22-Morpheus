from tkinter import *
import random

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

def createcards():
    pass


def main():
    

    window = Tk()


    window.geometry("500x500")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    my_frame = Frame(window)
    my_frame.pack(pady=20)
    card_frame = LabelFrame(my_frame,text="hello")
    card_frame.pack()
    card_label = Label(card_frame,text="")
    card_label.pack(pady=20)

    
    

    window.mainloop()

main()