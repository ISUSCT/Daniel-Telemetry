import tkinter as tk
from tkinter import *
from tkinter import ttk

ws = Tk()

# title
Label(ws, text="ISU Solar Car").grid(row=0, column=4)

# MPH, RPM, Odometer
Label(ws, text="MPH").grid(row=1, column=3)
Label(ws, text="00000").grid(row=2, column=3)
Label(ws, text="RPM").grid(row=1, column=4)
Label(ws, text="00000").grid(row=2, column=4)
Label(ws, text="Odometer").grid(row=1, column=5)
Label(ws, text="00000").grid(row=2, column=5)

Label(ws, text="Battery Volt ").grid(row=1, column=0)
Label(ws, text="78% ").grid(row=2, column=0)
Label(ws, text="Battery Amp").grid(row=1, column=1)
Label(ws, text="70%").grid(row=2, column=1)

# Error Message output
Label(ws, text="Error Messages").grid(row=1, column=8)
Label(ws, text="sample error message").grid(row=2, column=8)

# Solar Array
Label(ws, text="SOLAR ARRAY").grid(row=5, column=8)
Label(ws, text="A1").grid(row=6, column=7)
Label(ws, text="40").grid(row=7, column=7)
Label(ws, text="A2").grid(row=6, column=8)
Label(ws, text="40").grid(row=7, column=8)
Label(ws, text="A3").grid(row=6, column=9)
Label(ws, text="40").grid(row=7, column=9)
Label(ws, text="A4").grid(row=8, column=7)
Label(ws, text="40").grid(row=9, column=7)
Label(ws, text="A5").grid(row=8, column=8)
Label(ws, text="40").grid(row=9, column=8)
Label(ws, text="A6").grid(row=8, column=9)
Label(ws, text="40").grid(row=9, column=9)




# Battery Cell display
Label(ws, text="BATTERY CELLS ").grid(row=6, column=2)
Label(ws, text="BC1").grid(row=7, column=0)
Label(ws, text="80%").grid(row=8, column=0)
Label(ws, text="BC2").grid(row=7, column=1)
Label(ws, text="80%").grid(row=8, column=1)
Label(ws, text="BC3").grid(row=7, column=2)
Label(ws, text="80%").grid(row=8, column=2)
Label(ws, text="BC4").grid(row=7, column=3)
Label(ws, text="80%").grid(row=8, column=3)
Label(ws, text="BC5").grid(row=7, column=4)
Label(ws, text="80%").grid(row=8, column=4)
Label(ws, text="BC6").grid(row=7, column=5)
Label(ws, text="80%").grid(row=8, column=5)

Label(ws, text="BC7").grid(row=9, column=0)
Label(ws, text="80%").grid(row=10, column=0)
Label(ws, text="BC8").grid(row=9, column=1)
Label(ws, text="80%").grid(row=10, column=1)
Label(ws, text="BC9").grid(row=9, column=2)
Label(ws, text="80%").grid(row=10, column=2)
Label(ws, text="BC10").grid(row=9, column=3)
Label(ws, text="80%").grid(row=10, column=3)
Label(ws, text="BC11").grid(row=9, column=4)
Label(ws, text="80%").grid(row=10, column=4)
Label(ws, text="BC12").grid(row=9, column=5)
Label(ws, text="80%").grid(row=10, column=5)

Label(ws, text="BC13").grid(row=11, column=0)
Label(ws, text="80%").grid(row=12, column=0)
Label(ws, text="BC14").grid(row=11, column=1)
Label(ws, text="80%").grid(row=12, column=1)
Label(ws, text="BC15").grid(row=11, column=2)
Label(ws, text="80%").grid(row=12, column=2)
Label(ws, text="BC16").grid(row=11, column=3)
Label(ws, text="80%").grid(row=12, column=3)
Label(ws, text="BC17").grid(row=11, column=4)
Label(ws, text="80%").grid(row=12, column=4)
Label(ws, text="BC18").grid(row=11, column=5)
Label(ws, text="80%").grid(row=12, column=5)

Label(ws, text="BC19").grid(row=13, column=0)
Label(ws, text="80%").grid(row=14, column=0)
Label(ws, text="BC20").grid(row=13, column=1)
Label(ws, text="80%").grid(row=14, column=1)
Label(ws, text="BC21").grid(row=13, column=2)
Label(ws, text="80%").grid(row=14, column=2)
Label(ws, text="BC22").grid(row=13, column=3)
Label(ws, text="80%").grid(row=14, column=3)
Label(ws, text="BC23").grid(row=13, column=4)
Label(ws, text="80%").grid(row=14, column=4)
Label(ws, text="BC24").grid(row=13, column=5)
Label(ws, text="80%").grid(row=14, column=5)

Label(ws, text="BC25").grid(row=15, column=0)
Label(ws, text="80%").grid(row=16, column=0)
Label(ws, text="BC26").grid(row=15, column=1)
Label(ws, text="80%").grid(row=16, column=1)
Label(ws, text="BC27").grid(row=15, column=2)
Label(ws, text="80%").grid(row=16, column=2)
Label(ws, text="BC28").grid(row=15, column=3)
Label(ws, text="80%").grid(row=16, column=3)
Label(ws, text="BC29").grid(row=15, column=4)
Label(ws, text="80%").grid(row=16, column=4)
Label(ws, text="BC30").grid(row=15, column=5)
Label(ws, text="80%").grid(row=16, column=5)

Label(ws, text="BC31").grid(row=17, column=0)
Label(ws, text="80%").grid(row=18, column=0)
Label(ws, text="BC32").grid(row=17, column=1)
Label(ws, text="80%").grid(row=18, column=1)
Label(ws, text="BC33").grid(row=17, column=2)
Label(ws, text="80%").grid(row=18, column=2)
Label(ws, text="BC34").grid(row=17, column=3)
Label(ws, text="80%").grid(row=18, column=3)
Label(ws, text="BC35").grid(row=17, column=4)
Label(ws, text="80%").grid(row=18, column=4)
Label(ws, text="BC36").grid(row=17, column=5)
Label(ws, text="80%").grid(row=18, column=5)




ws.mainloop()