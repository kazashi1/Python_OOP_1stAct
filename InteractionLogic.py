class CoffeeMachine:
	def __init__(self):
		self.water_level = 100

	def brew_coffee(self):
		if self.water_level >= 20:
			self.water_level -= 20
			print("Coffee is ready!")
		else:
			print("Please refill water.")

machine = CoffeeMachine()
machine.brew_coffee()
machine.brew_coffee()
print("Current water level:", machine.water_level)
