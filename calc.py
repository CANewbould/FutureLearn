#calc.py

# simple terminal-based calculator

# Author: C A Newbould

# Version 2

## Added some try clauses

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
                    no2 = float(input('New divisor: ')) # Version 2
                except ValueError: # Version 2
                    print(invalid) # Version 2
            return n
    elif op == 'x':
        return op # Version 2
    else:
        print("!!! INVALID OP CODE !!!")
        return 888

# Execution
result = ask()
while result != 'x': # Version 2
    if result != 888:
        print("The result is: %g" % result)
    result = ask()

print("!!! CLOSING !!!")


