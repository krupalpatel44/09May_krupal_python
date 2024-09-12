import tkinter
from tkinter import ttk,messagebox

hotel=tkinter.Tk()
hotel.title("Hotel Management System")
hotel.geometry("800x800")
hotel.config(bg="lightgrey")

lebel=tkinter.Label(text="WELCOME",fg="black",bg="lightgrey",font="calibri 36 bold")
lebel.place(x=350,y=30)

first_box=tkinter.Button(text="1.CHECK INN",fg="black",bg="grey",font="calibri 16 bold",borderwidth=5,width=25)
first_box.place(x=100,y=100)    

second_box=tkinter.Button(text="2.SHOW GUEST LIST",fg="black",bg="grey",font="calibri 16 bold",borderwidth=5,width=25)
second_box.place(x=100,y=170)

third_box=tkinter.Button(text="3.CHECK OUT",fg="black",bg="grey",font="calibri 16 bold",borderwidth=5,width=25)
third_box.place(x=100,y=240)

fourth_box=tkinter.Button(text="4.GET INFO OF ANY GUEST",fg="black",bg="grey",font="calibri 16 bold",borderwidth=5,width=25)
fourth_box.place(x=100,y=310)

fifth_box=tkinter.Button(text="5.EXIT",fg="black",bg="grey",font="calibri 16 bold",borderwidth=5,width=25)
fifth_box.place(x=100,y=380)

hotel.mainloop()
