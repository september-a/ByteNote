import tkinter as tk
from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors
from colour import Color
import meternome

from fileOrganize import *
app = gui()
def main():
    height = 0
    width = 0
    for m in get_monitors():
        height = int(m.height * .8)
        width = int(m.width * .8)
    
    root = tk.Tk()
    root.title("Tab Widget")
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Tab1')
    tabControl.add(tab2, text='Tab 2')
    tabControl.pack(expand=1, fill = 'both')
    ttk.Label(tab1, text="Meternome").grid(column=0, row=0, padx=30, pady=30)
    ttk.Label(tab2, text="File Organizer").grid(column=0, row=0, padx=30, pady=30)
    objectMeternome = meternome.Meternome(120)
    B = tk.Button(tab1, text ="Meternome", command = objectMeternome.meternomeClick())
    root.mainloop()

def launch(win):
    app.showSubWindow(win)
    app.go(startWindow="one")


if __name__ == "__main__":
    main()

