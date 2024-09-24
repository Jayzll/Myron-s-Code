from newGame import *
from tkinter import *
import questions 
import database


def startQuestions(user_id, username, startQuestion = 0, startScore = 0):
     root.withdraw()
     quizWindow = Toplevel(root)
     app = questions.QuizApp(quizWindow, user_id, username, startQuestion, startScore)
     quizWindow.mainloop()

def startQuestionsWrapper(username):
     #DO THISSSSSSSSSSSSSSSSSSSSSSS
     user_data = database.loadUserProgress(username)  
     print("This is the username",username)   
     if user_data:
          user_id = user_data[0]
          startQuestions(user_id, username)
     else:
          messagebox.showerror("Error","User data not found. Please register or try again")

def startintroduction(username):
     global root
     root = Tk()
     intVar = StringVar()
     root.geometry("600x400") 
     title = Label(root, text = "Introduction")
     title.grid(row=0,column=0,pady=10)

     intro = Label(root, text = "Welcome to the Intelligence Quotient Game", width=80, height=4,)
     intro.grid(row = 1, column = 0)
     sub = Label(root, text = "Press the 'Next' button to discover your IQ", width=80, height=4,)
     sub.grid(row = 2, column = 0,pady=10)
     QuestionsButton = Button(root, text='Next', width=50, height=4, command=lambda: startQuestionsWrapper(username))
     QuestionsButton.grid(row=3, column=0, pady=10)
    
     root.mainloop() 

