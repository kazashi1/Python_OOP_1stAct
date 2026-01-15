class SmartLight:
	def __init__(self):
		self.is_on = False

	def toggle(self):
		self.is_on = not self.is_on

	def status(self):
		if self.is_on:
			print("The light is currently ON")
		else:
			print("The light is currently OFF")


smartlight = SmartLight()
smartlight.status()
smartlight.toggle()
smartlight.status()
