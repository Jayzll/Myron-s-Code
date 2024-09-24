from tkinter import *

def startleaderboard():
     window = Tk()
     window.geometry("600x400") 

     title = Label(window, text = "Leaderboard: ")

     title.grid(row = 0, column = 0)

     window.mainloop()