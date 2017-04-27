
"""
	the name of the object in its own class is called self
	lifetime of fullName on exists in __init__
	the objects attribute is myName 

"""
class Person():

	def __init__(self, fullName):
		self.myName = fullName

	def printMe(self):
		print(self.myName)

#created person object called student
student = Person("Juliana")
#prints attribute myName of object called student 
student.printMe()