from tkinter import *
from tkinter import messagebox
import webbrowser
from tkvideo import tkvideo
from Virtula import command

def first():
    # create instance fo window
    root = Tk()
    root.resizable(False, False)
    # set window title
    root.title('Virtula - The desktop Assitant')
    # create label
    video_label = Label(root)
    video_label.pack()
    # read video to display on label
    player = tkvideo(
                        "C:/Users/Jadhav/Desktop/Final Year Project/ChatBot/Animation.mp4",
                        video_label,
                    )
    player.play()

    root.after(10000,lambda:root.destroy())

    root.mainloop()

def hello():  
    print("hello!")  

def helpDef():
    return messagebox.showinfo('Help','This is some help for you!')

def feedbackDef():
    webbrowser.open(
        "https://www.microsoft.com/en-gb/microsoft-365/online-surveys-polls-quizzes",
        new="new"
        )

def startDef():
    command()

def stopDef():
    print("Stop Clicked")

def second():
    second_frame = Tk()
    second_frame.geometry('340x350')
    second_frame.resizable(False, False)
    second_frame.title('Virtula-Desktop Assitant')
    second_frame['bg']='white'

    # create a toplevel menu  
    menubar = Menu(second_frame)  
    # menubar.add_command(label="Feedback")  
    # menubar.add_command(label="Help")  
    menubar.add_command(label="Explore")  
    menubar.add_command(label="About Us", command=hello)  
    menubar.add_command(label="Specs")  
    # menubar.add_command(label="Quit", command=second_frame.quit)  
    
    # display the menu  
    second_frame.config(menu=menubar) 

    start = PhotoImage(file = r"C:/Users/Jadhav/Desktop/Final Year Project/ChatBot/startFinal.png")
    startBtn=Button(second_frame, command=startDef, image = start , bg='#ffffff', borderwidth=0,  compound=LEFT, cursor='hand1')
    startBtn.place(x=95, y=60)

    stop = PhotoImage(file = r"C:/Users/Jadhav/Desktop/Final Year Project/ChatBot/stopFinal.png")
    stopBtn=Button(second_frame, command=stopDef, image = stop , bg='#ffffff', borderwidth=0,  compound=LEFT, cursor='hand1')
    stopBtn.place(x=95, y=170)
    
    photo1 = PhotoImage(file = r"C:/Users/Jadhav/Desktop/Final Year Project/ChatBot/help.png")
    photoimage1 = photo1.subsample(12, 12)
    help=Button(second_frame, text = "Help", command=helpDef, image = photoimage1 , bg='#ffffff', fg='#219ebc',borderwidth=0,padx=10, pady=5, compound=LEFT, cursor='hand1')
    help.place(x=10, y=290)

    photo2 = PhotoImage(file = r"C:/Users/Jadhav/Desktop/Final Year Project/ChatBot/feedback.png")
    photoimage2 = photo2.subsample(9, 9)
    help=Button(second_frame, text = "Feedback", command=feedbackDef, image = photoimage2 , bg='#ffffff', fg='#219ebc',borderwidth=0,padx=10, pady=5, compound=LEFT, cursor='hand1')
    help.place(x=200, y=297)

    second_frame.mainloop()

# first()
# second()