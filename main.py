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
    
    app.setSize(width, height)

    app.startTabbedFrame("TabbedFrame")
    app.startTab("Metronome")
    app.addCanvas("c1")
    app.addCanvasOval("c1", int(height/2)+100, int(width/5), 200, 200, fill="black", outline="black", width=3)
    app.addCanvasText("c1", 10, 10,"Help")
    app.stopTab()

    app.startTab("Pitch Generator")
    app.addLabel("l2", "Tab 2 Label")
    app.stopTab()

    app.startTab("Tuner")
    app.addLabel("l3", "Tab 3 Label")
    app.stopTab()

    app.startTab("File Save")
    app.addLabel("l4", "Tab 4 Label")

    app.addButton("Create Project", launch)

    app.startSubWindow("one", modal=True)
    app.addLabel("l1", "SubWindow One")
    app.stopSubWindow()



    
   
    
    app.go()


def launch(win):
    app.showSubWindow(win)
    app.go(startWindow="one")


if __name__ == "__main__":
    main()

