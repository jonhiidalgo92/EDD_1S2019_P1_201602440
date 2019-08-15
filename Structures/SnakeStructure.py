#import ScoreHeap
import os, sys
import subprocess
from random import randint
import curses
from curses import KEY_RIGHT
from curses import KEY_LEFT
from curses import KEY_DOWN
from curses import KEY_UP

import random
from curses import textpad

#global variables for the scenario
Width = 75
Height = 25
Maxime_Horizontal = Width -5
Maxime_Vertical = Height - 5
Length_Snake = 3
ZiseHorizontal_Snake = Length_Snake +1
ZiseVertical_Snake = 3
TimeEnd = 100


class NodeSnake(object):
	def __init__(self,x,y, char='#'):
		self.x = x
		self.y = y
		self.char = char
		self.next = None
		self.prev = None


	def getDato(self):
		return self.data

	@property
	def coor(self):
		return self.x, self.y

class Snake(object):
#double list builder
	ziseSnake = 0
	GraficaSnake = ""
	def __init__(self):
		self.first=None
		self.end=None
		self.ziseSnake=0
		self.GraficaSnake = ""
#get the boolean value if the list is empty or not
	def getEmpty(self):
		if self.first==None:
			return True
#Insert the Elements in the list at the End of the snake
	def Insert(self,x,y):
		node = NodeSnake(x,y)
		if self.getEmpty()==True:
			self.first=node
			self.end=node
			#self.ziseSnake = ziseSnake + 1
		else:
			self.end.next=node
			node.prev=self.end
			self.end=node
			#self.ziseSnake = ziseSnake + 1
	#Insert the Elements in the list at the Start of the snake
	def InsertAtStart(self,node):
		if self.getEmpty()==True:
			self.first=node
			self.end=node
			self.ziseSnake = ziseSnake + 1
		else:
			self.first.prev=node
			node.next=self.first
			self.first=node
			self.ziseSnake = ziseSnake + 1



#Trabel  the linked double list
	def TrabelList(self):
		if self.getEmpty()==True:
			print("The snake is Empty")
		else:
			tempo = self.first
			while tempo != None:
				return tempo
				tempo = tempo.next
				pass



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
			return None
		else:
			tempo = self.first
			while tempo.next != self.end:
				tempo = tempo.next
				pass
			return tempo
			tempo.next=None
			self.end.prev=None
			self.end=tempo
			tempo=self.first

#Delete of the Snake for first node
	def DecreaseSnake2(self):
		if self.getEmpty()==True:
			print("The Queue is Empty")
			return None
		else:
			tempo=self.first
			return tempo
			self.first=self.first.next
			tempo.next=None
			self.first.prev=None




#Full Automatic of Snake
	def FullAutomatic(self):
		self.Insert(NodeSnake(0,0))
		self.Insert(NodeSnake(0,1))
		self.Insert(NodeSnake(0,2))




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
			self.Insert(NodeSnake(x,y))
		else:
			self.Insert(NodeSnake(x,y))

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
#Generate graphic of Snake
	def GenerateSnakeOter(self,cosa):
		cont = 0
		Snake.GraficaSnake = Snake.GraficaSnake + "\n" +"digraph G {"+"\n"
		if cosa.first==None:
			print("The Snake is Empty")
		else:
			tempo = cosa.first
			tempo2 = cosa.end
			while tempo != None:
				cont+=1
				if tempo.next == None or tempo.prev == None:
					Snake.GraficaSnake = Snake.GraficaSnake  +"\""+"("+str(tempo.x)+","+str(tempo.y)+")" +"\""+ "->" +"\""+ "Null"+ "\""+";"+"\n"
				else:
					Snake.GraficaSnake = Snake.GraficaSnake +"\""+"("+str(tempo.x)+","+str(tempo.y)+")"+"\"" + "->"+"\""+"("+str(tempo.next.x)+","+str(tempo.next.y)+")" +"\""+ ";"+"\n"
				tempo = tempo.next
				pass
			while tempo2 != None:
				cont+=1
				if tempo2.prev == None or tempo2.next == None:
					Snake.GraficaSnake = Snake.GraficaSnake +"\""+"("+str(tempo2.x)+","+str(tempo2.y)+")" +"\""+ "->" +"\""+ "Null"+ "\""+"[dir=back];"+"\n"
				else:
					Snake.GraficaSnake = Snake.GraficaSnake  +"\""+"("+str(tempo2.x)+","+str(tempo2.y)+")" +"\""+ "->"+"\""+"("+str(tempo2.next.x)+","+str(tempo2.next.y)+")" +"\""+"[dir=back];"+"\n"
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
