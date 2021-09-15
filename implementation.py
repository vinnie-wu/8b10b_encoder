# there's just 5 parts
# ---------------------------------
# 1. 
#
from helpers import *

def get_initial_three_bit_state():
    # Return the initial state for your 3b/4b encoder.
    
    return -1 # should be -1, only called once at the start of every encoding.

def get_initial_five_bit_state():
    """Return the initial state for your 5b/6b encoder."""
    return -1 # should be -1, only called once at the start of every encoding.

def get_disparity_of_parts( three_bit_input , five_bit_input ): # 3-bit input, 5-bit input
    # Given the 3-bit & 5-bit parts, determine if 4-bit & 6-bit outputs will have disparity
    # --------2nd stage----------
    is_three_bit_disparity = False
    is_five_bit_disparity  = False
    # 1. encode 3-bit to 4-bit, 5-bit to 6-bit.
    encodedSixBits = []
    encodedSixBits = five_bit_lookup_table(five_bit_input)
    encodedFourBits = []
    encodedFourBits = three_bit_lookup_table(three_bit_input)
    
    # 2. Detect if a disparity exists (not equal to 0) in 6-bit
    onesInSixBit = weight(encodedSixBits)
    if onesInSixBit != 3:
        is_five_bit_disparity = True
    # 3. Detect if a disparity exists in 4-bit
    onesInFourBit = weight(encodedFourBits)
    if onesInFourBit != 2:
        is_three_bit_disparity = True

    return is_three_bit_disparity, is_five_bit_disparity

def do_five_bit_encoding( current_input, current_state, is_three_bit_disparity, is_five_bit_disparity ):
    # -------3rd stage------------
    # Given: -R.D.
    #        -5-bit
    # Return:
    #       - 6-bit
    #       - new R.D.
    #       - invert3b4b: Y(1) = invert, N(0) = Don't invert
    # Given the current state and five bit part of the current input, return a tuple containing the six bit of the output, the next state and a value to feed into the 3b/4b encoder (you can put None if you don't need to send anything to the 3b/4b encoder)."""
    # ---------------------------------------------
    # 1. Encode from 5-bit to 6-bit first,
    six_bit_value = []
    six_bit_value = five_bit_lookup_table(current_input)
    #  2A). Case by R.D. = -1
    #  - Look at 3-bit-disparity, and 5-bit-disparity, decide on each case if the 6-bit should be flipped.
    if (int(current_state) == -1):
        if(is_five_bit_disparity == True and is_three_bit_disparity == True):
            six_bit_value = invert_array(six_bit_value)
            current_state = 1 #  -1 This might be INTERIM R.D. ... check later if test fails.
        if(is_five_bit_disparity == True and is_three_bit_disparity == False):
            six_bit_value = invert_array(six_bit_value)
            current_state = 1
        if(is_five_bit_disparity == False and is_three_bit_disparity == True):
            # do nothing, invert 4-bit
            current_state = -1 # 1
        if(is_five_bit_disparity == False and is_three_bit_disparity == False):
            # do nothing for BOTH
            current_state = -1
    # 2B). Case by R.D = 1
    if (int(current_state) == 1):
        # ---- In this particular case, no matter what five-disparity is, it will always be NOT INVERT 6-bit
        if(is_five_bit_disparity == True and is_three_bit_disparity == True):
            current_state = -1 # 1
        if(is_five_bit_disparity == False and is_three_bit_disparity == True):
            current_state = 1 # -1 
        if(is_five_bit_disparity == True and is_three_bit_disparity == False):
            current_state = -1
        if(is_five_bit_disparity == False and is_three_bit_disparity == False):
            current_state = 1

    return six_bit_value, current_state
 
def do_three_bit_encoding( current_input, current_state, is_three_bit_disparity, is_five_bit_disparity ):
    # Given the current input, the current state and a message from the 5b/6b encoder and returns its next state and a four bit output."""
    # --- Doing the same thing previously, for the 5b/6b encoder--------------
    four_bit_value = []
    four_bit_value = three_bit_lookup_table(current_input)

#  2A). Case by R.D. = -1
    #  - Look at 3-bit-disparity, and 5-bit-disparity, decide on each case if the 4-bit should be flipped.
    if (int(current_state) == -1):
        if(is_five_bit_disparity == True and is_three_bit_disparity == True):
            four_bit_value = invert_array(four_bit_value)
            current_state = -1 # This is TRUE
        if(is_five_bit_disparity == True and is_three_bit_disparity == False):
            # Don't invert 4-bit
            current_state = 1 
        if(is_five_bit_disparity == False and is_three_bit_disparity == True):
            four_bit_value = invert_array(four_bit_value)
            current_state = 1
        if(is_five_bit_disparity == False and is_three_bit_disparity == False):
            # do nothing for BOTH
            current_state = -1
    # 2B). Case by R.D = 1
    
    if (int(current_state) == 1):
        # ---- In this particular case, no matter what five-disparity is, it will always be NOT INVERT 6-bit
        if(is_five_bit_disparity == True and is_three_bit_disparity == True):
            four_bit_value = invert_array(four_bit_value)
            current_state = 1
        if(is_five_bit_disparity == False and is_three_bit_disparity == True):
            current_state = -1
        if(is_five_bit_disparity == True and is_three_bit_disparity == False):
            current_state = -1
        if(is_five_bit_disparity == False and is_three_bit_disparity == False):
            current_state = 1

    return four_bit_value, current_state

# adding invert_array()- inverts 0 to 1, and 1 to 0
def invert_array(arrayToInvert):
    arrayInverted = []
    for i in arrayToInvert:
        i = 1 - int(i)
        arrayInverted.append(i)
    return arrayInverted
