from turtle import *
t = Turtle()

class KameClass:
	name = ""
	def __init__(self, n, L, LL):
		 self.name= n
		 self.L1 = L
		 self.L2 = LL
		 print(self.name + str(self.L1) + "ステップ移動")
		 t.fd(L)

class SubKameClass(KameClass):
	def __init__(self, n, L, LL):
		parent_class = super(SubKameClass, self)
		parent_class.__init__(n, L, LL)
		print("一辺が" + str(LL) + "の" + self.name + "の正三角形")
		for i in range(3):
			t.fd(LL)
			t.lt(360/3)

h = SubKameClass("太郎", 50, 200)


