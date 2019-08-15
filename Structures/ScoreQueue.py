import os, sys
import subprocess
class NodeQueue(object):
	def __init__(self,data,data2):
		self.data = data
		self.data2 = data2
		self.next = None
	def getDato(self):
		return self.data
	pass

class ScoreQueue(object):

	size=0
	graficaQueue =""
#Queue builder
	def __init__(self):
		self.first=None
		self.end=None
		self.size=0
		self.graficaQueue=""
#get the boolean value if the Queue is empty or not
	def getEmpty(self):
		if self.first==None:
			return True
#Insert the Elements in the Queue ScoreHeap
	def Insert(self,x,y):
		node=NodeQueue(x,y)
		if self.getEmpty()==True:
			self.first=node
			self.top=node
		else:
			self.top.next=node
			self.top=node

#print all items in the Queue
	def PrintAll(self):
		if self.getEmpty()==True:
			print("The Queue is Empty")
		else:
			tempo = self.first
			while tempo != None:
				print(tempo.data,end='')
				print('->',end='')
				print(tempo.data2,end='')
				print('->',end='')
				tempo = tempo.next
				pass

#Delete first item in the Queue
	def RemoveQueue(self):
		if self.getEmpty()==True:
			print("The Queue is Empty")
		else:
			tempo=self.first
			self.first=self.first.next
			tempo.next=None

#remove when there is more than 10

	def RestrictioQueue(self,data,data2):
		ScoreQueue.size += 1
		if ScoreQueue.size <= 10:
			print("Dale dale aun caben nodos.. ")
			self.Insert(NodeQueue(data,data2))
		elif ScoreQueue.size > 10:
			print("Bamos a seguir insertando pero eliminamos al inicio.. ")
			self.Insert(NodeQueue(data,data2))
			self.RemoveQueue()
#Generate graphic of Queue
	def GenerateGraphic(self):
		ScoreQueue.graficaQueue = ScoreQueue.graficaQueue + "\n" +"digraph G {"+"\n"
		if self.first==None:
			print("The Queue is Empty")
		else:
			tempo = self.first
			while tempo != None:
				if tempo.next == None:
					ScoreQueue.graficaQueue = ScoreQueue.graficaQueue +"\""+"("+str(tempo.data)+","+str(tempo.data2)+")" +"\""+ "->" + "Null"+ ";"+"\n"
				else:
					ScoreQueue.graficaQueue = ScoreQueue.graficaQueue +"\""+"("+str(tempo.data)+","+str(tempo.data2)+")" +"\""+ "->"+"\""+"("+str(tempo.next.data)+","+str(tempo.next.data2)+")" +"\""+ ";"+"\n"
				tempo = tempo.next
				pass
		ScoreQueue.graficaQueue = ScoreQueue.graficaQueue +"\n"+"}"
		print(ScoreQueue.graficaQueue)
		archivo = open('GraficaScore.dot','w')
		archivo.write(ScoreQueue.graficaQueue)
		archivo.seek(0)
		comando = " dot -Tpng  GraficaScore.dot -o GraficaScore.png"
		os.system(comando)
		os.system("GraficaScore.png")

#Generate graphic of Queue
	def GenerateGraphic2(self,cosa):
		ScoreQueue.graficaQueue = ScoreQueue.graficaQueue + "\n" +"digraph G {"+"\n"
		if cosa.first==None:
			print("The Queue is Empty")
		else:
			tempo = cosa.first
			while tempo != None:
				if tempo.next == None:
					ScoreQueue.graficaQueue = ScoreQueue.graficaQueue +"\""+"("+str(tempo.data)+","+str(tempo.data2)+")" +"\""+ "->" + "Null"+ ";"+"\n"
				else:
					ScoreQueue.graficaQueue = ScoreQueue.graficaQueue +"\""+"("+str(tempo.data)+","+str(tempo.data2)+")" +"\""+ "->"+"\""+"("+str(tempo.next.data)+","+str(tempo.next.data2)+")" +"\""+ ";"+"\n"
				tempo = tempo.next
				pass
		ScoreQueue.graficaQueue = ScoreQueue.graficaQueue +"\n"+"}"
		print(ScoreQueue.graficaQueue)
		archivo = open('GraficaScore.dot','w')
		archivo.write(ScoreQueue.graficaQueue)
		archivo.seek(0)
		comando = " dot -Tpng  GraficaScore.dot -o GraficaScore.png"
		os.system(comando)
		os.system("GraficaScore.png")

	pass
