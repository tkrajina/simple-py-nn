# -*- coding: utf-8 -*-

import pynn.utils as mod_utils
import pynn.hopfield as mod_hopfield

import random as mod_random

def helper( hopfield, s, test_data ):
	dd = []
	for i in range( 10 ):
		dd.append( test_data[ i ] )
		
	index = int( 9. * mod_random.random() )
	
	if dd[ index ] < 0.:
		dd[index] = 1.
	else:
		dd[index] = -1.
		
	rr = hopfield.recall( dd, 5 )
	
	print s + "\nOriginal data: "
	
	for i in range( 10 ):
		print pp( test_data[ i ] ),
	print "\nRandomized data: "
	
	for i in range( 10 ):
		print pp( dd[ i ] ),
	print "\nRecognized pattern: "
	
	for i in range( 10 ):
		print pp( rr [ i ] ),

def pp( x ):
	x = float( x )
	
	if x > 0.1:
		return 1
	
	return 0

if __name__ == '__main__':
	data = [
			[  1,  1,  1, -1, -1, -1, -1, -1, -1, -1 ],
			[ -1, -1, -1,  1,  1,  1, -1, -1, -1, -1 ],
			[ -1, -1, -1, -1, -1, -1, -1,  1,  1,  1 ]
	]
	
	hopfield = mod_hopfield.Hopfield( 10 )
	
	for data_row in data:
		hopfield.add_training_data( data_row )
		
	hopfield.train()
	
	helper( hopfield, "pattern 0", data[ 0 ] )
	helper( hopfield, "pattern 1", data[ 1 ] )
	helper( hopfield, "pattern 2", data[ 2 ] )

	
