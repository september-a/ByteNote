from appJar import gui

def main():
    app = gui()
    app.addLabel("title", "Welcome to appJar")
    app.setLabelBg("title", "red")
    app.go()


if __name__ == "__main__":
    main()