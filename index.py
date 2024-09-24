from tkinter import *
import newGame
import loadGame
import leaderboardLanding

root = Tk()

def startLeader():
    root.destroy()
    leaderboardLanding.startleaderboardGame()

def startNew():
    root.destroy()
    newGame.startNewGame()

def startLoad():
    root.destroy()
    loadGame.startloadGame()

def start():
    w = Label(root, text='IQ Game')
    w.pack()
    root.title('Home page')
    newGameButton = Button(root, text='New Game', width=50, height=15, command=startNew)
    newGameButton.pack()
    loadGameButton = Button(root, text='Load Game', width=50, height=15, command=startLoad)
    loadGameButton.pack()
    leaderBoardButton = Button(root, text='LeaderBoard', width=50, height=15, command=startLeader)
    leaderBoardButton.pack()

    root.mainloop()

start()
