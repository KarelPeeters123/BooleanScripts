import sys
hex_values = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def contains_point(number):
    return '.' in number
def decimal_to_check_fraction(number, base):
    if contains_point(number):
        number = str(number)
        [integer_part, fractional_part] = number.split('.')
        integer_part = decimal_to(integer_part, base)
        fractional_part = fractional_decimal_to(fractional_part, base)
        result = "{}.{}".format(integer_part, fractional_part)
    else:
        result = decimal_to(number, base)
    return result
def to_decimal_check_fraction(number, base):
    if contains_point(number):
        number = str(number)
        [integer_part, fractional_part] = number.split('.')
        integer_part = to_decimal(integer_part, base)
        fractional_part = fractional_to_decimal(fractional_part, base)
        result = "{}.{}".format(integer_part, str(fractional_part)[2:])
    else:
        result = to_decimal(number, base)
    return result

def fractional_decimal_to(fractional, base):
    fractional = float('0.{}'.format(str(fractional)))
    factor = base
    result = ""
    while fractional != 0:
        if fractional * factor >= 1:
            fractional = (fractional) - 1/factor
            result = result + '1'
        else:
            result = result + '0'
        factor = factor * base
    return result
def fractional_to_decimal(fractional, base):
    fractional = str(fractional)
    factor = 1
    value = 0
    for i in range(len(fractional)):
        value = value + float(fractional[i]) / (base**(i+1))
    return value
def get_digit(integer, isHex):
    if isHex:
        return hex_values[integer-1]
    return str(integer)
def get_int(digit, isHex):
    if isHex:
        return hex_values.index(digit)+1
    return int(digit)
def decimal_to(decimal, base):
    isHex = base == 16
    result = ""
    decimal = int(decimal)
    while (decimal > 0):
        result = get_digit(decimal % base, isHex) + result
        decimal = decimal // base
    return result
def to_decimal(input, base):
    isHex = base == 16
    factor = 1
    decimal = 0
    while(len(input) > 0):
        decimal = decimal + (get_int(input[len(input)-1], isHex) * factor)
        factor = factor * base
        input = input[:len(input)-1]
    return decimal
# x = input("type your decimal:\n")
# print(decimal_to_binary(x))
if sys.argv[1] == 'to':
    x = input("type your decimal:\n")
    # print(not y[:len(y)-1] == "")
    print(decimal_to_check_fraction(x, int(sys.argv[2])))
else:
    x = input("type your value of base {}:\n".format(sys.argv[2]))
    # print(not y[:len(y)-1] == "")
    print(to_decimal_check_fraction(x, int(sys.argv[2])))
# print(fractional_decimal_to(75, 2))
