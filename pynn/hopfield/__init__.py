# -*- coding: utf-8 -*-

import pynn.utils as mod_utils

class Hopfield:
	"""
	Simple implementation of Hopfield neural network.
	
	Rewriten from the java source code www.markwatson.com/opencontent/
	"""
    
	num_inputs = None
	weights = None
	input_cells = None
	temp_storage = None
        
	training_data = []
    
	def __init__( self, num_inputs ):
		self.num_inputs = num_inputs
		
		self.weights = mod_utils.multidimensional_array( num_inputs, dimensions = 2, default_value = 0. )
		self.input_cells = mod_utils.array( num_inputs, default_value = 0. )
		self.temp_storage = mod_utils.array( num_inputs, default_value = 0. )
        
	def add_training_data( self, data ):
		""" data must be a list/array of floats """
		assert type( data ) in ( list, tuple )
		
		self.training_data.append( data )
		
	def train( self ):
		""" Train the neural network """
		
		for j in range( self.num_inputs ):
			for i in range( j ):
				for n in range( len( self.training_data ) ):
					data = self.training_data[ n ]
					temp1 = self.adjust_input( float( data[ i ] ) ) * self.adjust_input( float( data[ j ] ) )
					temp = self.truncate( temp1 + self.weights[ j ][ i ] )
					self.weights[ j ][ i ] = temp
					self.weights[ i ][ j ] = temp
					
		for i in range( self.num_inputs ):
			self.temp_storage[ i ] = 0.
			for j in range( i ):
				self.temp_storage[ i ] += self.weights[ i ][ j ]
				
	def recall( self, pattern, num_iterations ):
		assert pattern
		assert num_iterations
		
		for i in range( self.num_inputs ):
			self.input_cells[ i ] = pattern[ i ]
			
		for ii in range( num_iterations ):
			for i in range( self.num_inputs ):
				if self.delta_energy( i ) > 0.:
					self.input_cells[ i ] = 1.
				else:
					self.input_cells[ i ] = 0.
					
		return self.input_cells
	
	def adjust_input( self, x ):
		assert type( x ) == float
		
		if x < 0.1:
			return -1.
		
		return 1.
	
	def truncate( self, x ):
		assert type( x ) == float
		
		return float( int( x ) )
	
	def delta_energy( self, index ):
		assert type( index ) == int
		
		temp = 0.
		
		for j in range( self.num_inputs ):
			temp += self.weights[ index ][ j ] * self.input_cells[ j ]
			
		return 2. * temp - self.temp_storage[ index ]