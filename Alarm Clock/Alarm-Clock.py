"""
Alarm Clock - A simple clock where it plays a sound 
after X number of minutes/seconds or at a particular time.
"""
from tkinter import *
import datetime
import time
from playsound import playsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)  # Print current time after every 1 second
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")

            play = 0
            while play != 10:  # This will ring alarm for 10 seconds
                playsound(
                    "sound.wav")
                play += 1
            print("Set alarm again")
            return


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("TryCatch Alarm Clock")
clock.geometry("500x250")
get_up = Label(clock, text="At what time do you wanna get up?",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=35, y=10)

time_format = Label(clock, text="Enter the time in 24 hr format",
                    fg="Blue", bg="black", font=("Arial", 15, 'bold')).place(x=115, y=200)
addTime = Label(clock, text="Hour  Min   Sec", font=60).place(x=150, y=90)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="powderblue",
                 width=15).place(x=150, y=120)
minTime = Entry(clock, textvariable=min, bg="powderblue",
                width=15).place(x=190, y=120)
secTime = Entry(clock, textvariable=sec, bg="powderblue",
                width=15).place(x=240, y=120)

set_alarm = Button(clock, text="Set Alarm", fg="green", activebackground="grey", activeforeground="darkgreen", width=10, font=(
    "Arial", 15, 'bold'), command=actual_time).place(x=200, y=150)

photo = PhotoImage(file="Alarm Clock/alarm.png")
clock.iconphoto(False, photo)


clock.mainloop()
