# -*- coding: utf-8 -*-

def array( size, default_value = 0 ):
	return multidimensional_array( size, dimensions = 1, default_value = default_value )

def multidimensional_array( size, dimensions = 2, default_value = 0 ):
	if dimensions == 0:
		return default_value
	
	result = []
	
	for i in range( size ):
		result.append( multidimensional_array( size, dimensions = dimensions - 1, default_value = default_value ) )

	return result

if __name__ == '__main__':
	pass
