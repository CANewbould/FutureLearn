# primes.py

# Version 2

primes = []

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
for i in range(2,limit):
    if is_prime(i):
        primes.append(i)

print('\n*** Prime numbers up to', limit,'***')

for i in primes:
    print(i)


