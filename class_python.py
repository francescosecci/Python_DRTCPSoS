

class Person:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def printData(self):
		print self.name + " " + self.surname



class Student(Person):
	def __init__(self, name, surname, reg_number):
		Person.__init__(self, name, surname)
		self.reg_number = reg_number

	def printData(self):
		print self.name + " " + self.surname + " - " + str(self.reg_number)



x = Person("francesco", "secci")
y = Student("francesco", "secci", 656345)

x.printData()
y.printData()