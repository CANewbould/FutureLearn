# primes.py

# Version 3

primes = [2] # Version 3

print("\n\nThis app calculates all prime numbers up to a user-defined limit")
print("----------------------------------------------------------------")

limit = int(input("Maximum value? "))

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in primes: # Version 2
            if n % i == 0:
                return False
        return True

# Execution
for i in range(3,limit): # Version 3
    if is_prime(i):
        primes.append(i)

print('\n*** Prime numbers up to', limit,'***\n') # Version 3

# removed in Version 3: for i in primes:
    # removed in Version 3: print(i)
print (', '.join(map(str,primes))) # Version 3 - source Reactgo for idea
