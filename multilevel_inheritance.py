class Transport: # Base class of AutoMobile class
	def __init__(self, fuel: float):
		self.fuel = fuel

	def show_fuel(self):
		return f"Has a {self.fuel}"


class AutoMobile(Transport): # Child class and also Base Class of GermanAuto
	def __init__(self, coleso: int, fuel: float):
		self.coleso = coleso
		super(AutoMobile, self).__init__(fuel)

	def show_auto_info(self):
		return f"Auto has {self.coleso} wheels. Fuel: {super(AutoMobile, self).show_fuel()}"


class GermanAuto(AutoMobile): # Child class of AutoMobile and Transport

	def __init__(self, marka: str, speed: int, coleso: int, fuel: float):
		self.marka = marka
		self.speed = speed

		super(GermanAuto, self).__init__(coleso, fuel)

	def drive(self, time):
		distance = self.speed * time
		return f"Auto {self.marka}, with {self.coleso} wheels, has a fuel {self.fuel} and reach distance {distance} in {time} seconds"


bmw = GermanAuto("BMW", 180, 4, 10)
print(bmw.drive(10))
