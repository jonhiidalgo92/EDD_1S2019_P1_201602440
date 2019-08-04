#import ScoreHeap
import os, sys
import subprocess


class NodeSnake(object):
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
	def getDato(self):
		return self.data
	pass

class Snake(object):
#double list builder
	ziseSnake = 3
	GraficaSnake = ""
	def __init__(self):
		self.first=None
		self.end=None
		self.ziseSnake=3
		self.GraficaSnake = ""
#get the boolean value if the list is empty or not
	def getEmpty(self):
		if self.first==None:
			return True
#Insert the Elements in the list at the End of the snake
	def Insert(self,node):
		if self.getEmpty()==True:
			self.first=node
			self.end=node
		else:
			self.end.next=node
			node.prev=self.end
			self.end=node
	#Insert the Elements in the list at the Start of the snake  
		def InsertAtStart(self,node):
			if self.getEmpty()==True:
				self.first=node
				self.end=node
			else:
				self.first.prev=node
				node.next=self.first
				self.first=node
#print all items in the list
	def PrintAll(self):
		if self.getEmpty()==True:
			print("The snake is Empty")
		else:
			tempo = self.first
			while tempo != None:
				print(tempo.data,end='')
				print('.',end='')
				tempo = tempo.next
				pass
#Delete of the Snake for end node
	def DecreaseSnake1(self):
		if self.getEmpty()==True:
			print("The Snake is Dead")
		else:
			tempo = self.first
			while tempo.next != self.end:
				tempo = tempo.next
				pass
			tempo.next=None
			self.end.prev=None
			self.end=tempo
			tempo=self.first

#Delete of the Snake for first node
	def DecreaseSnake2(self):
		if self.getEmpty()==True:
			print("The Queue is Empty")
		else:
			tempo=self.first
			self.first=self.first.next
			tempo.data=None
			tempo.next=None
			self.first.prev=None
#Full Automatic of Snake
	def FullAutomatic(self):
		self.Insert(NodeSnake("#"))
		self.Insert(NodeSnake("#"))
		self.Insert(NodeSnake("#"))

#increase or decrease of the snake
	def IncreaseOrDecrease(self,node):

		if node=="*":
			#Aqui tiene que ir si la serpiente va para adelante o para atras
			if snake.ziseSnake > 3:
				self.DecreaseSnake1()
				snake.ziseSnake = snake.ziseSnake - 1
			else:
				print("Ya perdiste mano..")
		elif node== "+":
			snake.ziseSnake +=1
			self.Insert(NodeSnake("#"))
		else:
			self.Insert(NodeSnake(node))

#Generate graphic of Snake
	def GenerateSnake(self):
		Snake.GraficaSnake = Snake.GraficaSnake + "\n" +"digraph G {"+"\n"
		if self.first==None:
			print("The Snake is Empty")
		else:
			tempo = self.first
			tempo2 = self.end
			while tempo != None:
				if tempo.next == None or tempo.prev == None:
					Snake.GraficaSnake = Snake.GraficaSnake + tempo.data + "->" + "Null"+ ";"+"\n"
				else:
					Snake.GraficaSnake = Snake.GraficaSnake + tempo.data + "->" + tempo.next.data+ ";"+"\n"
				tempo = tempo.next
				pass
			while tempo2 != None:
				if tempo2.prev == None or tempo2.next == None:
					Snake.GraficaSnake = Snake.GraficaSnake + tempo2.data + "->" + "Null"+ ";"+"\n"
				else:
					Snake.GraficaSnake = Snake.GraficaSnake  + tempo2.data + "->" + tempo2.next.data+ ";"+"\n"
				tempo2 = tempo2.prev
				pass
		Snake.GraficaSnake = Snake.GraficaSnake +"\n"+"}"
		print(Snake.GraficaSnake)
		archivo = open('GraficaSnake.dot','w')
		archivo.write(Snake.GraficaSnake)
		archivo.seek(0)
		comando = " dot -Tpng  GraficaSnake.dot -o GraficaSnake.png"
		os.system(comando)
		os.system("GraficaSnake.png")
		pass

	pass



snake = Snake()
#snake.FullAutomatic()
snake.IncreaseOrDecrease("1")
snake.IncreaseOrDecrease("3")
snake.IncreaseOrDecrease("4")
snake.IncreaseOrDecrease("6")
snake.IncreaseOrDecrease("8")
snake.IncreaseOrDecrease("9")
snake.IncreaseOrDecrease("87")
snake.IncreaseOrDecrease("08")
snake.PrintAll()
snake.GenerateSnake()
