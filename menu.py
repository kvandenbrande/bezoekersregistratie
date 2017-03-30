#!/usr/bin/python3
from guizero import *

def screen1Open():
        screen1 = App("Screen 1", height=200, width=400)
        screen1.attributes("-fullscreen", True)
        title1 = Text(screen1, text="Menu 1")
        quitButton1 = PushButton(screen1, destroy, [screen1], text="Main Menu")
        screen1.display()

def screen2Open():
        screen2 = App("Screen 2", height=200, width=400)
        screen2.attributes("-fullscreen", True)
        title2 = Text(screen2, text="Menu 2")
        quitButton2 = PushButton(screen2, destroy, [screen2], text="Main Menu")
        screen2.display()

def screen3Open():
        if yesno("Quit Application", "Quit App - Are you sure?"):
                destroy(app)

def destroy(page):
        page.destroy()


app = App("Quiz Main Menu", height=480, width=800)
app.attributes("-fullscreen", True)
button1 = PushButton(app, screen1Open, text="Menu 1")
button2 = PushButton(app, screen2Open, text="Menu 2")
button3 = PushButton(app, screen3Open, text="Menu 3")

app.display()

