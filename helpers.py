from luts import *

def char_to_bit_array( character ):
    '''Converts an ASCII character into an array of eight bits'''
    character_as_number = ord( character )
    to_return = []
        
    for _ in range( 8 ):
        to_return.append( character_as_number % 2 )
        character_as_number = character_as_number >> 1

    return to_return

def bit_array_to_int( bit_array, flip_endianness=False ):
    '''Returns the number associated with an array of bits. Every vector of bits can be viewed as the digits of a number in base 2, this is useful for indexing a lookup table.'''
    iterator = reversed( bit_array ) if flip_endianness else iter( bit_array )
    index = 0   
 
    for value in iterator:
        index = index << 1
        index = index + value

    return index

def five_bit_lookup_table( bit_array ):
    '''Takes an array of five bits and returns the corresponding 5b/6b six bit output 
       This output will have three '0's and three '1's or four '0's and two '1's 
    '''

    index = bit_array_to_int( bit_array, True )
    return lut_5b_to_6b[index]


def three_bit_lookup_table( bit_array ):
    '''Takes an array of three bits and returns the corresponding 3b/4b four bit output 
       This output will have two '0's and two '1's or three '0's and a single '1'
    '''

    index = bit_array_to_int( bit_array, True )
    return lut_3b_to_4b[index]

def weight( bit_array ):
    '''Returns the number of ones in a set of bits. This is also known as the array's "weight"'''
    to_return = 0
    for value in bit_array:
        if( value == 1 ):
            to_return += 1
    return to_return

