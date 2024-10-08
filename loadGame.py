from tkinter import *
import introduction
import questions
import sqlite3
from tkinter import messagebox

root = Tk()
root.withdraw()

def loadUserProgress(username, password):
     conn = sqlite3.connect('iqeqdatabase.db')
     cursor = conn.cursor()
     cursor.execute('SELECT * FROM login WHERE username = ? AND password = ?', (username, password))
     user_data = cursor.fetchone()
     conn.close()
     return user_data


def startloadGame():
     window = Toplevel() 
     window.geometry("600x400")
     window.title("Load Game")
     
     loadTextOne = Label(window, text = "Enter usename")
     loadTextTwo = Label(window, text  = "Enter password")

     passVar = StringVar()
     userVar = StringVar() 

     loadBox = Entry(window, textvariable = userVar)
     loadBoxTwo = Entry(window, textvariable = passVar, show = "*")

     def handlesubmit():
          username = userVar.get()
          password = passVar.get()

          user_data = loadUserProgress(username, password)

          if user_data:
               user_id, username, password, current_question, score = user_data 
               messagebox.showinfo("success", f"welcome back, {username}!")
               window.destroy()
               quizWindow = Toplevel(root)
               app = questions.QuizApp(username, current_question, score)
               quizWindow.mainloop()
          else:
               messagebox.showerror("Error", "Invalid username or password")

     
     loadButton = Button(window, text = "Submit",command = handlesubmit)

     window.title.grid(row = 0, column = 0)
     loadTextOne.grid(row = 1, column = 0)
     loadTextTwo.grid(row = 2, column = 0)
     loadBox.grid(row = 1, column = 1)
     loadBoxTwo.grid(row = 2, column = 1)
     loadButton.grid(row = 3, column = 1)

     window.mainloop()

def startQuizApp(user_id, username, current_question = 0, score = 0):
     root.withdraw()
     quizWindow = Toplevel(root)
     app = questions.QuizApp(quizWindow, user_id, username, current_question, score)
     quizWindow.mainloop() 

def loadUserProgress(username, password):
     conn = sqlite3.connect('iqeqDatabase.db')
     cursor = conn.cursor()
     cursor.execute('''SELECT login.id, login.username, login.password, scores.currentQuestion, scores.score
                    FROM login
                    LEFT JOIN scores ON login.id = scores.id
                    WHERE login.username = ? AND login.password = ?''', (username, password))
     user_data = cursor.fetchone()
     conn.close()
     return user_data