import tkinter
from tkinter import ttk,messagebox
import tkinter.messagebox
#import hotelmangement

checkin=tkinter.Tk()
checkin.title("Hotel Management System")
checkin.geometry("400x400")
checkin.config(bg="white")

label=tkinter.Label(text="YOU CLICKED ON          :    CHECK INN     ",fg="black",bg="white",font="calibri 16 bold",borderwidth="1")
label.place(x=20,y=10)
checkin.mainloop()
