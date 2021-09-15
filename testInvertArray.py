def invert_array(arrayToInvert):
    arrayInverted = []
    for i in arrayToInvert:
        i = 1 - int(i)
        arrayInverted.append(i)
    print(arrayInverted)
    return arrayInverted