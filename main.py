from tkinter import *




szavak = []
file1 = open('szavak.txt', 'r',encoding='utf-8')
Lines = file1.readlines()
for line in Lines:
    szavak.append(line.strip())
print(szavak)


def createcard():
    pass



window = Tk()
greeting = Label(text="Hello, Tkinter")
greeting.pack()
window.geometry("500x500")
#bg = PhotoImage(file = "wood.png")
canvas1 = Canvas( window, width = 500,
                 height = 500)
canvas1.pack(fill = "both", expand = True)
#canvas1.create_image( 0, 0, image = bg, 
#                    anchor = "nw")

window.mainloop()