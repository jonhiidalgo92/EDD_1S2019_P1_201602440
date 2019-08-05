import csv
import os, sys
import subprocess


class NodeUsers(object):
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
	def getDato(self):
		return self.data
	pass


class UsersList(object):
	Grafica = ""
#cicular list builder
	def __init__(self):
		self.first=None
		self.end=None
		self.Grafica = ""

	def getDato(self):
		return self.first.data
		pass
#get the boolean value if the list is empty or not
	def getEmpty(self):
		if self.first==None:
			return True
#Insert the Elements in the Circular list
	def Insert(self,node):
		if self.getEmpty()==True:
			self.first=node
			self.end=node
			node.next = self.first
			node.prev = self.end
		else:
			self.end.next=node
			node.prev=self.end
			node.next=self.first
			self.first.prev=node
			self.end=node
#print all items in the circular list
	def PrintAll(self):
		if self.getEmpty()==True:
			print("The Circular List is Empty")
		else:
			tempo = self.first
			while True:
				print(tempo.data,end='')
				print('-><-',end='')
				tempo = tempo.next
				if tempo==self.first:
					break
				pass
#Show each user of the list
	def PrintEach(self,cosa):
		if self.getEmpty()==True:
			print("The Circular List is Empty")
		else:
		#	print(tempo.data)
	    #	self.first = tempo.next

			pass

	def BulkLoad(self):

		todo=""
		x = []
		e=0
		with open('usuarios.csv') as csvfile:
			data = csv.reader(csvfile,delimiter='\n')
			for i in data:
				x.append(i[0])
			while e < len(x):
				if e>0:
					self.Insert(NodeUsers(x[e]))
					todo+=x[e]+"\n"
				e+=1
			archivo = open('usuarios.txt','w')
			archivo.write(todo)
			archivo.seek(0)


# Generate the graphic report of the users
	def GenerateReportUsers(self):
		UsersList.Grafica = UsersList.Grafica+ "digraph G {"+"\n"
		if self.first==None:
			print("The Circular List is Empty")
		else:
			tempo = self.first
			tempo2 = self.end
			while True:
				UsersList.Grafica = UsersList.Grafica + tempo.data + "->" + tempo.next.data + ";"+" \n"
				tempo = tempo.next
				if tempo.next==self.first.next:
					break
				pass
			while True:
				UsersList.Grafica = UsersList.Grafica + tempo2.data + "->"+ tempo2.prev.data + "\n"
				tempo2 = tempo2.prev
				if tempo2.prev==self.end.prev:
					break
				pass
		UsersList.Grafica = UsersList.Grafica + "\n "+"}"
		print(UsersList.Grafica)
		archivo = open('GraficaCircular.dot','w')
		archivo.write(UsersList.Grafica)
		archivo.seek(0)
		comando = " dot -Tpng  GraficaCircular.dot -o GraficaCircular.png"
		os.system(comando)
		os.system("GraficaCircular.png")



	pass
