import math
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def get_distance(self, p):
		return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
	def get_midpoint(self, p):
		return Point((self.x + p.x)/2, (self.y + p.y)/2)

p1 = Point(5, 7)
p2 = Point(2, 3)
print(Point.get_distance(p1,p2))
