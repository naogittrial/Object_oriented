class Hero():
	def __init__(self, name):
		self.name = name

	def speak(self):
		return "私は"+self.name+"です。"

class Enemy():
	def __init__(self, name):
		self.name = name


	def speak(self):
		return "我は"+self.name+"なり。"

def self_introduction(obj):
	print(obj.speak())

hero = Hero("ヨシヒコ")
enemy = Enemy("魔王")

self_introduction(hero)
self_introduction(enemy)