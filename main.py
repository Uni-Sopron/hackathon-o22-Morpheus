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
    szavak = readszavak()
    selected_choices=[]
    random.choice()

    


def createcard():
    pass


def main():
    

    window = Tk()


    window.geometry("500x500")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    my_frame = Frame(window,bg="#954535")
    my_frame.pack(pady=20)
    card_frame = LabelFrame(my_frame,width=200,height=200)
    card_label = Label(card_frame,text="")

    
    

    window.mainloop()

main()