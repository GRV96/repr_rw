class Ajxo:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return self.__class__.__name__\
			+ "(" + repr(self.a) + ", " + repr(self.b) + ")"
