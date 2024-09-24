from tkinter import *
import database
import leaderboard

def adminLogin():
     passwordVar = passVar.get()
     validAdminPass = database.checkAdminPassword(passwordVar)
     if validAdminPass:
          window.destroy()
          leaderboard.startleaderboard()
          

def startleaderboardGame():
     global passVar
     global window
     window = Tk()
     passVar = StringVar()
     window.geometry("600x400") 

     title = Label(window, text = "Enter Admin Password Below:")
     
     passwordText = Label(window, text = "Enter password")

     entryBox = Entry(window, textvariable = passVar, show = "*")

     submitButton = Button(window, text = "Submit",command = adminLogin)

     title.grid(row = 0, column = 0)
     passwordText.grid(row = 1, column = 0)
     entryBox.grid(row = 1, column = 1)
     submitButton.grid(row = 2, column = 1)

     window.mainloop()




