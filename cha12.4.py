class Heaxagon:
	"""docstring for Heaxagon"""
	def __init__(self, length):
		self.length = length
		
	def calculate_perimeter(self):
		return 6 * self.length

heaxagon1 = Heaxagon(5)
print(heaxagon1.calculate_perimeter())