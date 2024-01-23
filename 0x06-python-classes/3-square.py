#!/usr/bin/python3
"""Square Module"""
class Square:
    """Define a Class named Square"""
    def area(self):
        """Area of square

        Return:
            the size squared.
        """

        return self.size ** 2
	def __init__(self, size=0):
	    """Constructor:
		
		Args:
		    size: length of a side of the square.
		
		Raise:
		    TypeError: if size if not an int
	            ValueError: if size if less than 0
		"""
	    if not isinstance(size, int):
	    	raise TypeError('size must be an integer')
	    if size < 0:
	    	raise ValueError('size must be >= 0')
	    self.size = size
