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
	def ride(self):
		print "Riding"
		self.miles += 10
	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -= 5


bike1 = bike(100,10)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.display()

bike2 = bike(200,20)
bike2.ride()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.display()

bike3 = bike(300,30)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.display()
