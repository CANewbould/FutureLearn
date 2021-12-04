#calc.py

# simple terminal-based calculator

# Author: C A Newbould

# Version 1

print('\n\nThis app runs a simple calculator')
print('----------------------------------\n')

print('To use:\n')
print('Key either:')

print(" 'a' for add")
print(" 's' for subtract")
print(" 'm' for multiply")
print(" 'd' for divide")
print(" 'x' to exit\n")

print("Then ,after the prompt, key in the two numbers to carry out the operation", end = ',')
print(' with a space in-between\n')

def ask():
    op = input("Operation: 'a', 's', 'd', 'm', or 'x': ")
    if op == 'x':
        return -999
    elif op in ['a', 's', 'm', 'd']:
        print("Numbers", end = ': ')
        no1, no2 = map(float, input().split()) # functional, I like

        # pity there is no 'switch' (could use map?)

        if op == 'a':
            return no1 + no2
        elif op =='s':
            return no1 - no2
        elif op == 'm':
            return no1 * no2
        elif op == 'd':
            return no1 / no2
    else:
        print("!!! INVALID OP CODE !!!")
        return 8888

# Execution
result = ask()
while result != -999:
    if result != 8888:
        print("The result is: %g" % result)
    result = ask()

print("!!! CLOSING !!!")


