import tkinter as tk
from tkinter import *
from tkinter import ttk

ws = Tk()
Label(ws, text="ISU Solar Car").grid(row=0, column=2)
Label(ws, text="MPH").grid(row=1, column=0)
Label(ws, text="00000").grid(row=2, column=0)
Label(ws, text="RPM").grid(row=1, column=1)
Label(ws, text="00000").grid(row=2, column=1)
Label(ws, text="Odometer").grid(row=1, column=2)
Label(ws, text="00000").grid(row=2, column=2)

Label(ws, text="Battery Volt ").grid(row=3, column=0)
Label(ws, text="78% ").grid(row=4, column=0)
Label(ws, text="Battery Amp").grid(row=3, column=1)
Label(ws, text="70%").grid(row=4, column=1)
Button(ws, text="Are we there yet button").grid(row=6, column=4)


ws.mainloop()