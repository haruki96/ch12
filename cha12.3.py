class Triangle:
	"""docstring for Triangle"""
	def __init__(self, bottom, hight):
		self.bottom = bottom
		self.hight = hight

	def area(self):
		return self.bottom * self.hight / 2

triangle1 = Triangle(10, 10)
print(triangle1.area())
		