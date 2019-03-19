class BMI:
	def __init__(self, weight, height):
		self.weight = weight
		self.height = height
		self.calBMC() #オブジェクトの中のcalBMC()メソッドを呼び出して実行する

	def calBMC(self):
		h = self.height /100
		self.bmi = self.weight/(h**2)

	def printJudge(self):
		print("---------")
		print("BMI=", self.bmi)
		b = self.bmi
		if(b<18.5): print("痩せ型")
		elif(b<25): print("標準")
		elif(b<30): print("軽肥満")
		else: print("肥満")

person1 = BMI(weight = 69, height =170)
person1.printJudge()


