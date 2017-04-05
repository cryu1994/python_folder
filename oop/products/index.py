class bike(object):
	def __init__(self, price, max_speed, miles = 0):
		print "New bike"
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def display(self):
		print "Price is:",self.price
		print "The max_speed is:",self.max_speed
		print "The total miles riden is:",self.miles
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -= 5
		return self


bike1 = bike(100,10).ride().ride().ride().reverse().display()

bike2 = bike(200,20).ride().ride().ride().reverse().display()

bike3 = bike(300,30).reverse().reverse().reverse().display()
