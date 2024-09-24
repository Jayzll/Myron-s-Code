import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

questions = [
    {
        "question":"question1.png",
        "option":["compassionate","comforting","explanatory","meddlesome"],
        "answer":"comforting"
    },
    {
        "question":"question2.png",
        "option":["A","B","C","D"],
        "answer":"B" 
    },
    {
        "question":"question3.png",
        "option":["122","120","118","116"],
        "answer":"118" 
    },
    {
        "question":"question4.png",
        "option":["20","24","26","28"],
        "answer":"24" 
    },
    {
        "question":"question5.png",
        "option":["C lied, B cheated","B lied, B cheated","A lied, C cheated","D lied, C cheated"],
        "answer":"C lied, B cheated" 
    },
    {
        "question":"question6.png",
        "option":["2","4","6","8"],
        "answer":"8" 
    },
    {
        "question":"question7.png",
        "option":["35","40","45","50"],
        "answer":"45" 
    },
    {
        "question":"question8.png",
        "option":["5","10","15","20"],
        "answer":"5" 
    },
    {
        "question":"question9.png",
        "option":["18","36","64","128"],
        "answer":"128" 
    },
    {
        "question":"question10.png",
        "option":["6","17","19","21"],
        "answer":"19" 
    }

]

class QuizApp:
    def __init__ (self,root, user_id, username, startQuestion = 0, startScore = 0):
        self.root = root
        self.user_id = user_id
        #self.root.title("Quiz App")
        self.username = username
        self.currentQuestion = startQuestion
        self.selectedOption = tk.StringVar()
        self.score = startScore

        self.image_dir = "iqQuestions"

        self.imageLabel = tk.Label(self.root)
        self.imageLabel.pack()

        self.radioButton = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text = "", variable = self.selectedOption, value = "", font = ("Arial", 14))
            rb.pack(anchor = 'w')
            self.radioButton.append(rb)
        
        self.submitButton = tk.Button(self.root, text = "Submit", command = self.checkAnswer)
        self.submitButton.pack()

        self.photo = None

        self.loadQuestion()
    
    def loadQuestion(self):
        """Load current question and answers"""

        if self.currentQuestion >= len(questions):
            self.finishQuiz()
            return

        questionData = questions[self.currentQuestion]
        imagePath = os.path.join(self.image_dir, questionData["question"])
        try:
            image = Image.open(imagePath)
            image = image.resize((1100, 400), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.imageLabel.config(image = self.photo)

            self.selectedOption.set(None)
            for i, option in enumerate(questionData["option"]):
                self.radioButton[i].config(text=option, value = option)
        except Exception as e:
            messagebox.showerror("Error", f"Error laoding image {imagePath}: {e}")
    def checkAnswer(self):
        questionData = questions[self.currentQuestion]
        selectedAnswer = self.selectedOption.get()

        if selectedAnswer == questionData["answer"]:
            messagebox.showinfo("Result","Correct!")
            self.score += 20
        else:
            messagebox.showinfo("Result",f"Incorrect! The correct answer is: {questionData['answer']}")
        
        self.currentQuestion += 1
        self.saveProgress()

        if self.currentQuestion < len(questions):
            self.loadQuestion()
        else:
            self.finishQuiz()

    def saveProgress(self):
        conn = sqlite3.connect('iqeqdatabase.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM scores WHERE id = ?', (self.user_id,))
        existingRecord = cursor.fetchone()

        if existingRecord:
            cursor.execute('UPDATE scores SET currentQuestion = ?, score = ? WHERE id = ?',
                           (self.currentQuestion, self.score, self.user_id))
        else:   
            cursor.execute('INSERT INTO scores (score, id, currentQuestion) VALUES (?,?,?)',
                           (self.score, self.user_id, self.currentQuestion))
        conn.commit()
        conn.close()            
    
    def finishQuiz(self):
        messagebox.showinfo("Quiz", f"You have completed the IQ test. Your IQ is {self.score}")
        self.root.quit()