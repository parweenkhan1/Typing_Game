words = ['Apple','gun','Orange','umbrella','pumpkin','Greps','Guava','PEACOCK','LION','TIGER',
           'APPLE','PINEAPPLE','POT','UNICORN','WATCH','TWILIGHT','WATERMELON','MANGO','sun',
         'moon','star','planet','master','MUCH-kin','-----','......','/////','?????']



def labelslider():
    global count,sliderWord
    text = 'Welcome to speed typing game'
    if count >= len(text):
        count = 0
        sliderWord = ''
    sliderWord += text[count]
    count += 1
    rootLebel1.configure(text=sliderWord)
    rootLebel1.after(150,labelslider)
def timeleft():
    global time,score,miss
    if time > 0:
        time -= 1
        TimerLimitCount.configure(text=time)
        TimerLimitCount.after(1000,timeleft)
        if(time < 11):
            TimerLimitCount.configure(fg='red')
    else:
        gamePlaydetaillabel.configure(text='hit={} | miss={} | TotalScore={}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel("Notification",'To play again hit retry button')
        if rr == True:
            score = 0
            time = 60
            miss = 0
            scoreLableCount.configure(text=score)
            TimerLimitCount.configure(text=time)
            wordLebel1.configure(text=words[0])




def startgame(event):
    global score,miss
    if time == 60:
        timeleft()
    gamePlaydetaillabel.configure(text='')
    if wordEntry.get() == wordLebel1['text']:
         score += 1
         scoreLableCount.configure(text=score)
    else:
         miss += 1

    random.shuffle(words)
    wordLebel1.configure(text=words[0])
    wordEntry.delete(0,END)







from tkinter import messagebox
import random
from tkinter import *

####################### root method
root = Tk()
root.geometry('800x600+300+100')
root.configure(bg="light blue")
root.title("Speed Typing Game")
#root.maxsize(height=600,width=800)
#root.minsize(height=600,width=
root.iconbitmap("Yootheme-Social-Bookmark-Social-twitter-box-blue.ico")
root.bind('<Return>',startgame)
############################################# Variable
score = 0
time = 60
count = 0
sliderWord = ''
miss = 0
#_____________________Level Method_______________________
rootLebel1 = Label(root,text="",bg="light blue",font=("arial",25,"italic bold"),fg="red",width=40)
rootLebel1.place(x=10,y=10)
labelslider()


random.shuffle(words)
wordLebel1 = Label(root,text=words[0],font=('arial',35,"italic bold"),bg="light blue")
wordLebel1.place(x=300,y=200)

scoreLabel1 = Label(root,text="Your Score:",font=('arial',25,'italic bold'),bg='light blue',fg='black')
scoreLabel1.place(x=10,y=100)

scoreLableCount = Label(root,text=score,font=('arial',25,'italic bold'),bg="light blue",fg="black")
scoreLableCount.place(x=60,y=150)

TimerLimit = Label(root,text='Time left:',font=('arial',25,'italic bold'),bg='light blue',fg='black')
TimerLimit.place(x=550,y=100)

TimerLimitCount = Label(root,text=time,font=('arial',25,'italic bold'),bg='light blue',fg='black')
TimerLimitCount.place(x=600,y=150)


gamePlaydetaillabel = Label(root,text='Type Word and Hit Enter Button',font=('arial',25,'italic bold'),bg='light blue',fg='gray')
gamePlaydetaillabel.place(x=150,y=500)

#____________________________Entry Method__________________
wordEntry = Entry(root,font=('arial',25,"italic bold"),bd=10,justify="center")
wordEntry.place(x=220,y=300)
wordEntry.focus_set()


root.mainloop()