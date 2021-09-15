from implementation import *
from helpers import *

# import other modules
from sys import argv, stdin

def encode_str( string, state_of_3b4b, state_of_5b6b ):
    for character in string:
        # Turn character into its ASCII bit representation
        char_in_bits = char_to_bit_array( character )

        # Split bit representation into its five bit and three bit part
        # ------------Stage 1--------------- (implemented for us)
        five_bit_part  = char_in_bits[0:5]
        three_bit_part = char_in_bits[5:8]

        # ------------Stage 2 -------------- (1. Need to Write get_disparity_of_parts()   )
        is_three_bit_disparity, is_five_bit_disparity = get_disparity_of_parts( three_bit_part, five_bit_part )

        # Apply 3b/4b encoding and 5b/6b encoding (implement these in implementation.py)
        # -----------Stages 3, 4-------------
        six_bit_output,  state_of_5b6b = do_five_bit_encoding( five_bit_part, state_of_5b6b, is_three_bit_disparity, is_five_bit_disparity )
        four_bit_output, state_of_3b4b = do_three_bit_encoding( three_bit_part, state_of_3b4b, is_three_bit_disparity, is_five_bit_disparity ) 
         
        # Concatenate four bit part and six bit part and print
        # ------------Stage 5-------------------
        for bit in four_bit_output + six_bit_output:
            print( bit, end="")

        print( "" )

if __name__ == '__main__':
    argc = len( argv )

    if( argc > 1 ):
        print( "usage: python main.py" )
        exit( 1 )

    input_str = stdin.readline() 
    input_str = input_str.strip()

    while( input_str != "" ):
        encode_str( input_str, get_initial_three_bit_state(), get_initial_five_bit_state() )
        input_str = stdin.readline() 
        input_str = input_str.strip()
    
