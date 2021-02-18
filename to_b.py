import sys


def binary_converter(value):
    result = ''
    while value > 0:
        result = ' '.join(value % 2)
        value //= 2
    return result

def to_b(value):
    while True:
        if value != 0:
            return binary_converter(value)
        else:
            sys.exit(-1)
            


print(to_b(10))
