class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def calculate_area(self):
		return self.width * self.height

	def __str__(self):
		return f"Rectangle: {self.width} x {self.height}"

rectangle = Rectangle(4, 8)
print(rectangle)
print("Area:", rectangle.calculate_area())
