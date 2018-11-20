#to show prime if a number is a prime number or not.


class primeNumbers():
	"""Class primeNumbers shows a list prime numbers from one to
to the number stated by the user"""
	def __init__(self,n):
		self.y=2
		self.n=n
		primeNumbers.nos=[]
		self.testing_files()
		# if self.arg < 0:
		# 	self.arg=abs(self.arg)
	def testing_files(self):
		"""Method to test the input"""
		
		if type(self.n) is list or type(self.n) is dict:
			raise TypeError("is not a number it is a",type(self.n))
		if self.n==0 or self.n<0:
			return []
		else:
			self.function()
	def function(self):
		# number=int(input("no: "))
		for x in range(2,self.n):
			# print("hello")
			for self.y in range(2,x):
				if x%self.y==0:
					break
			else:
				primeNumbers.nos.append(x)
			# break
		return primeNumbers.nos



Prime=primeNumbers(-5)
# print(Prime.nos)

