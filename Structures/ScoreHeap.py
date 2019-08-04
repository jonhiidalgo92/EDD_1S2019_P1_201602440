
import os, sys
import subprocess

class NodeHeap(object):
	def __init__(self,data):
		self.data = data
		self.next = None
	def getDato(self):
		return self.data
	pass


class ScoreHeap(object):
#Heap builder
	graficaHeap =""
	def __init__(self):
		self.background=None
		self.top=None
		self.graficaHeap=""
#get the boolean value if the Heap is empty or not
	def getEmpty(self):
		if self.background==None:
			return True
#Insert the Elements in the Heap
	def Insert(self,node):
		if self.getEmpty()==True:
			self.background=node
			self.top=node
		else:
			self.top.next=node
			self.top=node
#print all items in the HEAP
	def PrintAll(self):
		if self.getEmpty()==True:
			print("The Heap is Empty")
		else:
			tempo = self.background
			while tempo != None:
				print(tempo.data,end='')
				print('->',end='')
				tempo = tempo.next
				pass
#Delete Heap
	def PopHeap(self):
		if self.getEmpty()==True:
			print("The Heap is Empty")
		else:
			tempo = self.background
			while tempo.next != self.top:
				tempo = tempo.next
				pass
			tempo.next=None
			self.top=tempo
			tempo=self.background

#Generate graphic od the HEap of Score
	def GenerateGraphicHeap(self):
		ScoreHeap.graficaHeap = ScoreHeap.graficaHeap + "\n" +"digraph G {"+"\n"
		if self.background==None:
			print("The Queue is Empty")
		else:
			tempo = self.background
			while tempo != None:
				if tempo.next == None:
					ScoreHeap.graficaHeap = ScoreHeap.graficaHeap + tempo.data + "->" + "Null"+ ";"+"\n"
				else:
					ScoreHeap.graficaHeap = ScoreHeap.graficaHeap + tempo.data + "->" + tempo.next.data+ ";"+"\n"
				tempo = tempo.next
				pass
		ScoreHeap.graficaHeap = ScoreHeap.graficaHeap +"\n"+"}"
		print(ScoreHeap.graficaHeap)
		archivo = open('GraficaHeap.dot','w')
		archivo.write(ScoreHeap.graficaHeap)
		archivo.seek(0)
		comando = " dot -Tpng  GraficaHeap.dot -o GraficaHeap.png"
		os.system(comando)
		os.system("GraficaHeap.png")



	pass



heap = ScoreHeap()
heap.Insert(NodeHeap("1"))
heap.Insert(NodeHeap("2"))
heap.Insert(NodeHeap("3"))
heap.Insert(NodeHeap("4"))
heap.Insert(NodeHeap("5"))
heap.Insert(NodeHeap("6"))


heap.PrintAll()
heap.PopHeap()
heap.PopHeap()
heap.PrintAll()
heap.GenerateGraphicHeap()
