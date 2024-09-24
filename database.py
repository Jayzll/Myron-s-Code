import sqlite3
from tkinter import messagebox

def createLoginTable():
    conn = sqlite3.connect('iqeqDatabase.db', timeout = 20)
    loginTableCreateQuery = ('''CREATE TABLE IF NOT EXISTS login(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
    );''')
    conn.execute(loginTableCreateQuery)
    conn.commit()
    conn.close()

def createScoresTable():
    conn = sqlite3.connect('iqeqDatabase.db', timeout = 20)
    scoresTableCreateQuery = ('''CREATE TABLE IF NOT EXISTS scores(
                scoreId INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                id INTEGER,
                currentQuestion INTEGER,
                FOREIGN KEY (id) REFERENCES login(id)       
    );''')
    conn.execute(scoresTableCreateQuery)
    conn.commit()
    conn.close()

def createAdminTable():
    conn = sqlite3.connect('iqeqDatabase.db', timeout = 20)
    adminTableCreateQuery = ('''CREATE TABLE IF NOT EXISTS admin(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT NOT NULL
    );''')
    conn.execute(adminTableCreateQuery)
    conn.commit()
    conn.close()

def enterLoginData(username, password):
    conn = sqlite3.connect('iqeqDatabase.db')
    conn.execute('INSERT INTO login (username, password) VALUES (?,?)',(username, password))
    conn.commit()
    conn.close()

def usernameDuplicateCheck(username):
    conn = sqlite3.connect('iqeqDatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM login WHERE username = ?',(username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def addUser(username, password):
    userAdded = True
    if usernameDuplicateCheck(username):
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        userAdded = False
    else:
        enterLoginData(username, password)
        messagebox.showinfo("Success", "User added successfully.")
        userAdded = True
    return userAdded

def checkAdminPassword(password):
    conn = sqlite3.connect('iqeqDatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admin WHERE password = ?',(password,))
    result = cursor.fetchone()
    conn.close()
    print(result)
    return result

createLoginTable()
createAdminTable()
createScoresTable()

def enterAdminData(password):
    conn = sqlite3.connect('iqeqDatabase.db')
    conn.execute('INSERT INTO admin (password) VALUES (?)',(password,))
    conn.commit()
    conn.close()



string = 'IQ-EQg@m3'

def loadUserProgress(username):
    conn = sqlite3.connect('iqeqDatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username FROM login WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data