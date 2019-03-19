from turtle import *
t = Turtle()
#親クラス
class KameClass:
	name = ""
	def __init__(self, n, L):
		self.name = n
		self.add_kame(L)
	def add_kame(self,s):
		print(self.name + str(s) + "ステップ移動")
		t.fd(s)

#子クラス
class SubKameClass(KameClass):
	def __init__(self, n, L, LL):
		parent_class = super(SubKameClass, self)
		parent_class.__init__(n,L)
		self.sankaku(LL)
	def sankaku(self, s):
		print("一辺が" + str(s) + "の" + self.name + "の正三角形")
		for i in range(3):
			t.fd(s)
			t.lt((360/3))

h = SubKameClass("次郎", 50, 200)
