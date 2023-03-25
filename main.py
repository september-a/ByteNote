from appJar import gui
from screeninfo import get_monitors

def main():
    app = main_screen()
    app.go()
    

def main_screen():
    height = 0
    width = 0
    for m in get_monitors():
        height = int(m.height * .8)
        width = int(m.width * .8)
    app = gui()
    app.addLabel("title", "Welcome to appJar")
    app.setSize(width, height)
    app.setLabelBg("title", "red")
    return app



if __name__ == "__main__":
    main()