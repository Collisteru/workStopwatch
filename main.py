h## FILE MAIN.PY

import tkinter as tk
import tkinter.font as TkFont
import getpass
import platform


SOURCE = PATH + "clockSource.txt"

running = False


def parse_source(SOURCE):
    with open(SOURCE, 'a+') as src:
        # This assumes src.readlines() returns an integer
        src.seek(0)
        localCounter = src.read().strip()
    try:
        return int(localCounter)
    except:
        return 0

def write_source(SOURCE, localCounter):
    with open(SOURCE, 'a+') as src:
        src.seek(0)
        src.truncate(0)
        src.write(str(localCounter))

def increment():
    global localCounter
    global imgWrapper
    if(running == True):
        localCounter+= 1
    clockMode = localCounter % 8
    img = tk.PhotoImage(file=PATH+"/frame000{0}.png".format(clockMode))
    imgWrapper.configure(image=img)
    imgWrapper.image = img # Prevent garbage collection from deleting the image
    root.after(1000, increment)

def displayUpdate():
    global localCounter, display
    display.config(text=formatCounter(localCounter));
    root.after(1000, displayUpdate)

# We pass in a localCounter that we can easily manipulate ourselves
def formatCounter(localCounter):
    hours = localCounter // 3600
    localCounter = localCounter % 3600
    minutes = localCounter // 60
    localCounter = localCounter % 60
    seconds = localCounter
    if(seconds < 10):
        seconds = "0{0}".format(seconds)
    if(minutes < 10):
        minutes = "0{0}".format(minutes)
    displayString = "{0}:{1}:{2}".format(hours, minutes, seconds)
    return displayString 

def toggleRunning():
    global B
    global running
    if(running == False):
        running = True
        B.config(text="Stop", bg = "#ff8c8c", activebackground="#fcb6b6")
        return
    if(running == True):
        running = False
        B.config(text="Start", bg = "#8cffad", activebackground="#b6fcca")
        return


def on_closing(root):
    global localCounter
    write_source(SOURCE, localCounter)

def stay_on_top():
    global root
    root.lift()
    root.after(1, stay_on_top)




# MAIN CODE ##

# Create Window

root = tk.Tk() # Set tkinter root
root.geometry('230x48+1000+300')

# Initialize Root Info

root.title('Time Spent on Activity')
root.resizable(0,0)
root.bind("<Destroy>", on_closing)

# Initialize Local Counter

localCounter = parse_source(SOURCE)

# Initialize Clock Image


img = tk.PhotoImage(file=(PATH + "/frame0000.png"))
imgWrapper = tk.Label(root, image=img)
imgWrapper.grid(row=0, column=0)

# Create Display

display = tk.Label(text="0", anchor="w", font=("Less Perfect DOS VGA", 25))
display.grid(row=0, column=1)


B = tk.Button(root, text="Start", command = toggleRunning, bg = "#8cffad", activebackground="#b6fcca")
B.grid(row=0, column=2)


increment()
displayUpdate()


root.mainloop()
