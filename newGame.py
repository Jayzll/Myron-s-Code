from tkinter import *
from tkinter import messagebox
import introduction
import re
import database

def validatePassword(password):
    #checks if password meets requirements
    valid = True
    # Minimum length 8 characters
    if len(password) < 8:
        valid = False

    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        valid = False

    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        valid = False

    # Check for digit
    if not re.search(r'[0-9]', password):
        valid = False

    # Check for special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        valid = False

    return valid  

def validateUsername(username):
    #checks username field is not blank
    valid = True
    if username == "":
        valid = False
    return valid
        


def loadIntro(): 
    userVar = usernameVar.get()
    passVar = passwordVar.get()
    validCheckPass = validatePassword(passVar)
    validCheckUser = validateUsername(userVar)
    if validCheckPass and validCheckUser: 
        print("Valid username and password")
        if database.addUser(userVar, passVar): 
            root.destroy() 
            introduction.startintroduction(userVar) 
    else: 
        print("invalid pass") 
        messagebox.askretrycancel("Error", "Invalid username or password, try again") 

def startNewGame():
     global root
     global passwordVar
     global usernameVar 
     root = Tk()
     root.geometry("600x400") 

     title = Label(root, text = "New Game")
     
     userText = Label(root, text = "Enter usename")
     passText = Label(root, text  = "Enter password")

     usernameVar = StringVar()
     passwordVar = StringVar()

     entryBox = Entry(root, textvariable = usernameVar)
     entryBoxTwo = Entry(root, textvariable = passwordVar, show = "*")

     submitButton = Button(root, text = "submit", command = loadIntro)
     
     title.grid(row = 0, column = 0)
     userText.grid(row = 1, column = 0)
     passText.grid(row = 2, column = 0)
     entryBox.grid(row = 1, column = 1)
     entryBoxTwo.grid(row = 2, column = 1)
     submitButton.grid(row = 3, column = 1)

     
     root.mainloop()
     
 



     

  
    

