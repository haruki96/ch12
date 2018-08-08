class Apple:
	"""docstring for Apple"""
	def __init__(self, w, c, n):
		self.weight = w
		self.color = c
		self.number = n

	def temp(self):
		return self.weight * self.number

apple1 = Apple(100, "red", 1)
print(apple1.temp())
apple2 = Apple(75, "green", 6)
print(apple2.temp())
print(apple2.color)