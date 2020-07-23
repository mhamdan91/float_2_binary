# Function returns octal representation
def float_bin(number, places=3):
    # split() seperates whole number and decimal
    # part and stores it in two seperate variables
    whole, dec = str(number).split(".")

    # Convert both whole number and decimal
    # part from string type to integer type
    whole = int(whole)
    zeros = dec.count('0')
    dec = int(dec)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
        # Multiply the decimal value by 2
        # and seperate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec, zeros)) * 2.0).split(".")
        zeros = len(dec) - len(dec.lstrip('0'))
        # Convert the decimal part
        # to integer again
        if dec.__contains__('e'):
            dec = dec.split('e')
            digit = int(dec[0])
            exponent = pow(10, int(dec[1]))
            dec = digit*exponent
        else:
            dec = int(dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return res


# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num, zeros):
    while num >= 1:
        num /= 10
    for i in range(zeros):
        num /= 10
    # print("number:", num)
    return num


print(float_bin(0.25003424, places=16))
