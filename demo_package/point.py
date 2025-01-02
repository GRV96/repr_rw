class Point:

	def __init__(self, x, y):
		self._x = x
		self._y = y

	def __repr__(self):
		return self.__class__.__name__\
			+ f"({str(self._x)}, {str(self._y)})"

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y


__all__ = [Point.__name__]
