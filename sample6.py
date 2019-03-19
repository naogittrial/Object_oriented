class Student:
	def __init__(self, id, name, score=0):
		self.id = id
		self.name = name
		self.score = score

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def setScore(self, score):
		self.score = score

	def getScore(self):
		return self.score

class CalScore:
	def __init__(self):
		self.students = []

	def addStudent(self, student):
		self.students.append(student)

	def ave(self):
		v = 0
		for i in self.students:
			v += i.getScore()
		ave_v = v/sum(self.students)
		return ave_v

p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score=79)
p3 = Student(11, "佐々木", score=84)
p4 = Student(11, "井上", score=77)

cal = CalScore()
cal.addStudent(p1)
cal.addStudent(p2)
cal.addStudent(p3)
cal.addStudent(p4)

print(cal.ave())