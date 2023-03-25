from tkinter import *

ws=Tk()
ws.title("ByteNote")

ws.geometry('200x200')
width = ws.winfo_screenwidth()
height = ws.winfo_screenheight()
ws.geometry("%dx%d" % (width, height))

p1 = PanedWindow()
p1.pack(fill=BOTH, expand=1)

left = Label(p1, text="Left Panel")
p1.add(left)

p2 = PanedWindow(p1, orient=VERTICAL)
p1.add(p2)

top = Label(p2, text="Top Panel")
p2.add(top)

bottom = Label(p2, text="Bottom Panel")
p2.add(bottom)

ws.mainloop()