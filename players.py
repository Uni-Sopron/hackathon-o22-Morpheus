from tkinter import *


window = Tk()
def initplayers(mainframe):
    getplayersframe = Frame(mainframe, width=600,height=600)
    getplayersframe.grid(row=0,column=0)
    countframe= Frame(getplayersframe,width=600,height=600)
    countframe.pack()
    getplayersframe.pack_propagate(False)
    welcomemessage =Label(countframe,text= "Álmodj Velem")
    welcomemessage.pack(pady=40)
    playernumber = StringVar()
    welcomemessagefornumber =Label(countframe,text= "Add meg Hányan szertnétek játszani")
    welcomemessagefornumber.pack(pady=20)
    playernumberentry = Entry(countframe, textvariable=playernumber ,width=33)
    playernumberentry.pack()
    playersubmitbutton = Button(countframe,text="mehet",command=lambda:submit(playernumber,countframe,getplayersframe))
    playersubmitbutton.pack()
    
def addplayers(count,players,new_frame):
    secondaryplayerlist = players.get().split(',')
    for i in range(len(secondaryplayerlist)):
        playerlist.append(secondaryplayerlist[i])
    
    
    if len(playerlist) != int(count):
        newlabel = Label(new_frame, text="rossz játékosmennyiség,annyit adj meg amennyit választottál")
        newlabel.pack()
        playerlist.clear()
        
    else:
        window.destroy()
        

def getplayernames(getplayersframe,count):
    
    
    
    new_frame = Frame(getplayersframe, width=600, height = 600)
    new_frame.pack()
    label = Label(new_frame, text= 'add meg a neveket vesszővel elválasztva')
    label.pack()
    
    
    
    players = StringVar()
    entry=Entry(new_frame, textvariable=players )
    entry.pack()
        
    button = Button(new_frame,  text="mehet",command=lambda:addplayers(count,players,new_frame))
    button.pack()
    
def submit(playercount,countframe,getplayersframe):
    count = playercount.get()
    if int(count) <=3 or int(count) >=11:
        newlabel = Label(countframe, text="rossz játékosmennyiség, max 10, minimum 4")
        newlabel.pack()
    else:
        print('playercount= {}'.format(count))
        countframe.destroy()
        getplayernames(getplayersframe,count)

    

    

def rendermethod():
    global playerlist
    playerlist = []
    

   
    
    window.resizable(width=FALSE, height=FALSE)
    window.geometry("1200x800")
    window.title('Álmodj Velem')
    window.configure(background="#954535")
    mainframe= Frame(window ,background="#954535",padx=100,pady=100)
    mainframe.pack()

   
    initplayers(mainframe)
    
   


    window.mainloop()
    return {
        "playerek": playerlist
        
    }

   

if __name__ == "__main__": 
    rendermethod()
    
    