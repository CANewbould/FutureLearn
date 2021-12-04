#calc.py

# simple terminal-based calculator

# Author: C A Newbould

# Version 4

## added clear screen into - thanks to https://codecap.org/

import os # Version 4
import platform # Version 4

if(platform.system().lower() == "windows"): # Version 4
    cmdtorun = 'cls' # Version 4
else: # Version 4
    cmdtorun = 'clear' # Version 4
os.system(cmdtorun) # Version 4

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

# Repeated values
prompt = "Numbers" # Version 2
invalid = "!!! INVALID OP CODE !!!" # Version 2
codes = ['a', 's', 'm', 'd'] # Version 2

def ask():
    op = input("Operation: " + ', '.join(codes) + " or 'x': ") # from simplilearn
    if op in codes:
        print(prompt, end = ': ')
        while True: # Version 2
            try: # Version 2
                no1, no2 = map(float, input().split()) # functional, I like
                break # Version 2
            except ValueError: # Version 2
                print('!!!Non-numeric!!!',prompt, end=': ') # Version 2
        # pity there is no 'switch' (could use map?)
        if op == 'a':
            return no1 + no2
        elif op =='s':
            return no1 - no2
        elif op == 'm':
            return no1 * no2
        elif op == 'd':
            while True: # Version 2
                try: # Version 2
                    n = no1 / no2 # Version 2
                    break # Version 2
                except ZeroDivisionError: # Version 2
                    print("!!!Zero divisor!!!", end = ' ') # Version 2
                    while True: # Version 3
                        try: # Version 3
                            no2 = float(input('New divisor: ')) # Version 2
                            break # Version 3
                        except ValueError: # Version 2
                            print(invalid) # Version 2
            return n
    elif op == 'x':
        return op # Version 2
    else:
        print(invalid) # Version 2
        return 'i' # Version 3

# Execution
result = ask()
while result != 'x': # Version 2
    if result != 'i': # Version 3
        print("The result is: %g" % result)
    result = ask()

print("!!! CLOSING !!!")


