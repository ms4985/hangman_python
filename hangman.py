import random
import string
from tkinter import *

path = 'movies.txt'
i = 0
dict = {}
with open(path) as f:
	for line in f:
		line = line.split()
		line = ' '.join(line)
		dict[i] = line
		i = i+1

def pickMovie():
	n = random.randrange(1,i)
	return(dict[n]) 

class Hangman:

	def __init__(self):
		self.frame = Frame(root)
		self.frame.grid(row=0,column=0)
		self.frame2 = Frame(self.frame)
		self.frame2.grid(row=2, column = 0)
		self.quit = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
		self.start = Button(self.frame, text="START GAME", command=self.start)
		self.start.grid(row=0,column=0)
		self.quit.grid(row=0,column=1)


	def setImage(self, n):
		img1 = PhotoImage(file='man1.gif')
		self.man1 = Label(self.frame2, image= img1)
		self.man1.image = img1
		img2 = PhotoImage(file='man2.gif')
		self.man2 = Label(self.frame2, image= img2)
		self.man2.image = img2
		img3 = PhotoImage(file='man3.gif')
		self.man3 = Label(self.frame2, image= img3)
		self.man3.image = img3
		img4 = PhotoImage(file='man4.gif')
		self.man4 = Label(self.frame2, image= img4)
		self.man4.image = img4
		img5 = PhotoImage(file='man5.gif')
		self.man5 = Label(self.frame2, image= img5)
		self.man5.image = img5
		img6 = PhotoImage(file='man6.gif')
		self.man6 = Label(self.frame2, image= img6)
		self.man6.image = img6
		img7 = PhotoImage(file='man7.gif')
		self.man7 = Label(self.frame2, image= img7)
		self.man7.image = img7
		img8 = PhotoImage(file='man8.gif')
		self.man8 = Label(self.frame2, image= img8)
		self.man8.image = img8

		if n == 1:
			self.image = self.man1
		elif n == 2:
			self.image = self.man2
		elif n == 3:
			self.image = self.man3
		elif n == 4:
			self.image = self.man4
		elif n == 5:
			self.image = self.man5
		elif n == 6:
			self.image = self.man6
		elif n == 7:
			self.image = self.man7
		elif n == 8:
			self.image = self.man8

		self.image.grid(row=1, column=0)

	def start(self):
		self.frame2.destroy()
		self.frame2 = Frame(self.frame)
		self.frame2.grid(row=2, column = 0)
		self.img = 1
		self.setImage(1)
		self.movie = pickMovie()
		self.curboard = {}
		self.wlist = []
		self.length = len(self.movie)
		self.setInitBoard()
		self.setEntryTool()
		self.showWrongGuesses()
		
		
	def setInitBoard(self):
		i = 0
		while i < self.length:
			if(self.movie[i] == " "):
				l=Label(self.frame2, text = " ", font = "Helvetica 25 bold ")
				l.grid(row=1, column=i+3)
				self.curboard[i] = " "
			else:
				l=Label(self.frame2, text = "_", font = "Helvetica 25 bold ")
				l.grid(row=1, column=i+3)
				self.curboard[i] = "_"
			i = i+1

	def setBoard(self):
		i = 0
		while i < len(self.curboard):
			w = Label(self.frame2, text = self.curboard[i], font = "Helvetica 25 bold ")
			w.grid(row=1, column=(i+3))
			i = i+1


	def setEntryTool(self):
		self.enter = Label(self.frame2, text = "Enter a letter", font = "Helvetica 16 bold ")
		self.entry = Entry(self.frame2, width = "2")
		self.gbutton = Button(self.frame2, text = "Guess",font = "Helvetica 16 bold ", command = self.guess)
		self.enter.grid(row=2, column=0)
		self.entry.grid(row=2, column=1)
		self.gbutton.grid(row=2,column=2)

	def showWrongGuesses(self):
		w = Label(self.frame2, text = "Wrong Guesses: ", font = "Helvetica 16 bold")
		w.grid(row=3, column=0)
		i = 1
		for x in self.wlist:
			w=Label(self.frame2, text = x, font = "Helvetica 16 bold")
			w.grid(row=3, column =i)
			i = i+1

	def guess(self):
		guess = self.entry.get().upper()
		self.entry.delete(0,END)
		if self.check(guess) == True:
			i = 0
			for x in self.movie:
				if x == guess:
					self.curboard[i] = x
				i = i+1
			self.correct()
		else:
			self.wlist.append(guess)
			self.wrong()

	def check(self, guess):
		for x in self.movie:
			if x == guess:
				return(True)
		return(False)

	def correct(self):
		
		self.setBoard()
		self.setEntryTool()
		self.showWrongGuesses()
		self.response = Label(self.frame2, text = " Correct! ", fg = "blue", font = "Helvetica 16 bold italic")
		self.response.grid(row=4, column=0)
		if self.checkIfWinner() == True:
			self.response = Label(self.frame2, text = "YOU WIN!", fg = "green", font = "Helvetica 30 bold italic")
			self.response.grid(row=5, column=0)
		self.setImage(self.img)

	def wrong(self):
		if self.img == 1:
			self.img = 2
		elif self.img == 2:
			self.img = 3
		elif self.img == 3:
			self.img = 4
		elif self.img == 4:
			self.img = 5
		elif self.img == 5:
			self.img = 6
		elif self.img == 6:
			self.img = 7
		elif self.img == 7:
			self.img = 8
			self.setImage(self.img)
			self.gameover()

		self.setBoard()
		self.setEntryTool()
		self.showWrongGuesses()
		self.response = Label(self.frame2, text = "Incorrect!", fg = "red", font = "Helvetica 16 bold italic")
		self.response.grid(row=4, column=0)
		self.setImage(self.img)

	def gameover(self):
		self.setBoard()
		self.response = Label(self.frame2, text = "GAMEOVER!", fg = "orange",font = "Helvetica 30 bold italic")
		self.response.grid(row=5, column=0)
		w = Label(self.frame2, text = "Answer: " + self.movie, fg = "purple",font = "Helvetica 16 bold italic" )
		w.grid(row=6, column = 0)

	def checkIfWinner(self):
		i=0
		while(i < self.length):
			if self.curboard[i] == "_":
				return False
			i = i+1
		return True


root = Tk()
game = Hangman()
root.wm_title("Hangman: Movie Titles")
root.geometry("1250x400+400+400")
root.mainloop()


