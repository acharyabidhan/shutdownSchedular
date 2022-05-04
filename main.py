#Import required libraries
from tkinter import*
from tkinter import messagebox
from threading import Thread
import os, time, pystray
from pystray import MenuItem as item
from PIL import Image
os.system("cls")
#Create root window
root = Tk()
#Geometry management
root.resizable(0,0)
window_width = 400
window_height = 200
root.iconbitmap("others\\icon.ico")
root.title("Routine Of Shutdown")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.config(background = "#323232")
#Hour variable
hour = StringVar()
minute = StringVar()
ampm = StringVar()
#function to check hour, minute and am/pm
#Checktime thread
def checkTimeThread():
    thread1 = Thread(target=checkTime)
    thread1.start()
#Hover
def hourHoverEnter(e):
    hourEntry['background'] = 'white'
    hourEntry['foreground'] = 'black'
def hourHoverLeave(e):
    hourEntry["background"] = "#606060"
    hourEntry["foreground"] = "white"
def minuteHoverEnter(e):
    minuteEntry['background'] = 'white'
    minuteEntry['foreground'] = 'black'
def minuteHoverLeave(e):
    minuteEntry["background"] = "#606060"
    minuteEntry["foreground"] = "white"
def ampmHoverEnter(e):
    ampmEntry['background'] = 'white'
    ampmEntry['foreground'] = 'black'
def ampmHoverLeave(e):
    ampmEntry["background"] = "#606060"
    ampmEntry["foreground"] = "white"
def resetHoverEnter(e):
    if setButon["state"] == DISABLED:
        resetButon["background"] = "white"
        resetButon["foreground"] = "black"
def resetHoverLeave(e):
    resetButon["background"] = "#606060"
    resetButon["foreground"] = "white"
def setHoverEnter(e):
    if resetButon["state"] == DISABLED:
        setButon["background"] = "white"
        setButon["foreground"] = "black"
def setHoverLeave(e):
    setButon["background"] = "#606060"
    setButon["foreground"] = "white"
#Get hour
def checkHour():
    checkHour = hour.get()
    if len(checkHour) != 0:
        if checkHour.isdigit():
            checkHour = int(checkHour)
            if checkHour <= 12 and checkHour > 0:
                if checkHour <= 9:
                    checkHour1 = str(checkHour)
                    checkHour2 = "0"+checkHour1
                    return checkHour2
                else:
                    return checkHour
#Get minute
def checkMinute():
    checkMinute = minute.get()
    if len(checkMinute) != 0:
        if checkMinute.isdigit():
            checkMinute = int(checkMinute)
            if checkMinute <= 59:
                if checkMinute <= 9:
                    checkMinute1 = str(checkMinute)
                    checkMinute2 = "0"+checkMinute1
                    return checkMinute2
                else:
                    return checkMinute
#Get am/pm
def checkAmpm():
    checkAmpm = ampm.get()
    if len(checkAmpm) == 2:
        upperAmpm = checkAmpm.upper()
        if upperAmpm == "AM" or upperAmpm == "PM":
            return upperAmpm
def nothingThread():
    thread = Thread(target=nothing)
    thread.start()
#compare current time and given time
def checkTime():
    finalhour = checkHour()
    finalminute = checkMinute()
    finalampm = checkAmpm()
    givenTime = f"{finalhour}{finalminute}{finalampm}"
    if finalhour != None and finalminute != None and finalampm != None:
        setButon.config(state=DISABLED)
        hourEntry.config(state=DISABLED)
        minuteEntry.config(state=DISABLED)
        ampmEntry.config(state=DISABLED)
        resetButon.config(state=NORMAL)
        info.config(text=f"Your pc will shutdown in {finalhour}:{finalminute} {finalampm}")
        messagebox.showinfo("Info", f"Your pc will shutdown in {finalhour}:{finalminute} {finalampm}.\n You can find this app running in System Tray.")
        nothingThread()
        global running
        running = True
        while running:
            currentHour = time.strftime("%I")
            currentMinute = time.strftime("%M")
            currentNoon = time.strftime("%p")
            currentTime = f"{currentHour}{currentMinute}{currentNoon}"
            print("Given time:",givenTime)
            print("Current time:", currentTime)
            if givenTime == currentTime:
                os.system("shutdown -s -t 0")
                break
            time.sleep(1)
        resetButon.config(state=DISABLED)
        setButon.config(state=NORMAL)
        hourEntry.config(state=NORMAL)
        minuteEntry.config(state=NORMAL)
        ampmEntry.config(state=NORMAL)
        info.config(text=f"Your pc will shutdown in given time.")
        print("STOPPED")
    else:
        messagebox.showerror("Invalid Time","Enter the correct time!!")
def resetTime():
    global running
    running = False
#Enter label
enterTime = Label(root, text="Enter time in 12-Hour format.", bg="#323232", fg="white", bd=0,font=("Arial",15))
enterTime.place(relx=0.50, rely=0.01, anchor=N)
#Info label
info = Label(root, bg="#323232", text = 'Your pc will shutdown in given time.', fg="white", bd=0,font=("Arial",15))
info.place(relx=0.50, rely=0.95, anchor=S)
#Hour entry
hourEntry = Entry(root, textvariable=hour,bd=0, bg="#606060", font=("Arial", 15), width=8, fg="white")
hourEntry.insert(0,"hour")
hourEntry.place(relx=0.10, rely=0.20, anchor=NW)
#Minute entry
minuteEntry = Entry(root, textvariable=minute,bd=0, bg="#606060", font=("Arial", 15), width=8, fg="white")
minuteEntry.insert(0,"minute")
minuteEntry.place(relx=0.50, rely=0.20, anchor=N)
#AM PM entry
ampmEntry = Entry(root, textvariable=ampm,bd=0, bg="#606060", font=("Arial", 15), width=8, fg="white")
ampmEntry.insert(0,"am/pm")
ampmEntry.place(relx=0.90, rely=0.20, anchor=NE)
#Set button
setButon = Button(root, bg="#606060", fg="white", font=("Arial", 15), text="SET", width=8, bd=0, command=checkTimeThread)
setButon.place(relx=0.20, rely=0.60, anchor=W)
#Reset button
resetButon = Button(root, bg="#606060", fg="white", font=("Arial", 15), width=8, text="RESET", bd=0, command = resetTime)
resetButon.place(relx=0.80, rely=0.60, anchor=E)
resetButon.config(state=DISABLED)
#Bind buttons
hourEntry.bind("<Enter>", hourHoverEnter)
hourEntry.bind("<Leave>", hourHoverLeave)
minuteEntry.bind("<Enter>", minuteHoverEnter)
minuteEntry.bind("<Leave>", minuteHoverLeave)
ampmEntry.bind("<Enter>", ampmHoverEnter)
ampmEntry.bind("<Leave>", ampmHoverLeave)
resetButon.bind("<Enter>", resetHoverEnter)
resetButon.bind("<Leave>", resetHoverLeave)
setButon.bind("<Enter>", setHoverEnter)
setButon.bind("<Leave>", setHoverLeave)
running = False
def quitWindow(icon, item):
    resetTime()
    icon.stop()
    root.destroy()
def show_window(icon, item):
   icon.stop()
   root.after(0,root.deiconify())
def nothing():
    if setButon["state"] == DISABLED:
        root.withdraw()
        image = Image.open("others\\icon.ico")
        menu = (item('Exit app', quitWindow), item('Show app', show_window))
        icon = pystray.Icon("name", image, "Routine Of Shutdown", menu)
        icon.run()
    else:
        root.destroy()
root.protocol('WM_DELETE_WINDOW', nothing)
#Run forever
root.mainloop()