class Ajxo:
	# "Ajxo" means "thing" in Esperanto.

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return self.__class__.__name__\
			+ "(" + repr(self.a) + ", " + repr(self.b) + ")"


__all__ = [Ajxo.__name__]
