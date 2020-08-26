# get twos complement
def twos_comp(number):
    number = list(number.split('b')[1])
    for i, num in enumerate(number):
        if num == '0':
            number[i] = '1'
        else:
            number[i] = '0'
    for i in range(len(number)):
        if number[-1 - i] == '0':
            number[-1 - i] = '1'
            break
        else:
            number[-1 - i] = '0'

    return ''.join(number)


# Function returns binary representation
def float_bin(number, digits=4, places=4):
    LN = len(str(1 + number).split('.')[1])
    whole, dec = format(number, '0.{}f'.format(LN)).split(".")
    zeros = len(dec) - len(dec.lstrip('0'))

    # Convert both whole number and decimal
    # part from string type to integer type
    dec = dec.split('0')
    for idx in dec:
        if idx != '':
            dec = idx
            break
    whole = int(whole)
    dec = int(dec)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.

    # clamp input to only 4-bits
    dig_cap = pow(2, digits) - 1
    if whole < -dig_cap:
        whole = -dig_cap
    elif whole > dig_cap:
        whole = dig_cap
    else:
        pass

    res = bin(abs(whole)).lstrip("0b")
    if whole < 0:
        res = twos_comp("0b0" + res)

        # pad with 1s to meet digits precision
        while len(res) < digits:
            res = '1' + res
    res += "."
    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):

        # Multiply the decimal value by 2
        # and seperate the whole number part
        # and decimal part

        DC = format(decimal_converter(dec, zeros) * 2.0, '0.{}f'.format(LN))
        whole, dec = DC.split(".")
        zeros = len(dec) - len(dec.lstrip('0'))

        # Convert the decimal part
        # to integer again
        if dec.__contains__('e'):
            dec = dec.split('e')
            digit = int(dec[0])
            exponent = pow(10, int(dec[1]))
            dec = digit * exponent
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


# Take the user input for
# the floating point number
n = input("Enter your floating point value : ")

# Take user input for the number of
d = int(input("Enter the number of digit places of the result : "))
# decimal places user want result as
p = int(input("Enter the number of decimal places of the result : "))

print("Binary representation: ", float_bin(float(n), digits=int(d), places=int(p)))

