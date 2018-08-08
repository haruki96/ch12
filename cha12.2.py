import math

class Circle:
	"""docstring for Circle"""
	def __init__(self, a, b):
		self.yoko = a
		self.tate = b

	def area(self):
		return math.pi * self.yoko * self.tate

circle1 = Circle(5, 4)
print(circle1.area())

circle2 = Circle(10, 10)
print(circle2.area())