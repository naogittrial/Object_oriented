from turtle import *
t = Turtle()

#親クラスの定義
class KameClass:
	name = ""
	def add_kame(self, s): #親クラスのメソッド
		print(self.name + str(s) + "ステップ移動")
		t.fd(s)

#子クラスの定義
class SubKameClass(KameClass):
	def sankaku(self, s): #子クラスのメソッド
		print("一辺が" + str(s) + "の" + self.name + "の正三角形")
		for i in range(3):
			t.fd(s)
			t.lt(360/3)

hh = SubKameClass() #子区r巣のオブジェクト生成
hh.name = "次郎" #オブジェクト変数nameに代入
hh.add_kame(20) #親メソッドを呼び出して実行
hh.sankaku(100) #子メソッドを呼び出して実行
