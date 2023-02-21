import sys

try:
    x = int(input('x:'))
    y = int(input('y:'))
except ValueError:
    print('Error:Invalid input type')
    sys.exit(1)

try:
    res = x/y
    print(f'{x}/{y} is {res}')
except ZeroDivisionError:
    print('Error:cannot divide by zero')
    sys.exit(1)