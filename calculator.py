#calculator.py

# Python Program to Make a Simple Calculator

# This is Version 3, to include the try statements

def multiplication(num1, num2):
   return num1 * num2


def addition(num1, num2):
  return num1 + num2


def subtraction(num2, num1):
   return num1 - num2


def divide(num1, num2):
   return num1 / num2

while True:
   print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction, Other-exit")
   while True:
      try:
         operation = int(input("Choose operation 1/2/3/4: "))
         break
      except ValueError:
         print("Only numbers are allowed!")
   if operation not in [1,2,3,4]:
      break
   else:
      while True:
         try:
            value1 = int(input("Enter 1st number: "))
            break
         except ValueError:
            print("MUST be an INTEGER")
      while True:
         try:
            value2 = int(input("Enter 2nd number: "))
            break
         except ValueError:
            print("MUST be an INTEGER")
   if operation == 1:
      while True:
         try:
            ret = divide(value1, value2)
            break
         except ZeroDivisionError:
            value2 = int(input("Please enter a non-zero value: "))         
      print(value1, "/", value2, "=", ret)
   elif operation == 2:
      print(value1, "*", value2, "=", multiplication(value1, value2))
   elif operation == 3:
       print(value1, "+", value2, "=", addition(value1, value2))
   elif operation == 4:
       print(value1, "-", value2, "=", subtraction(value1, value2))
   else:
      print("Enter correct operation")

print("!!!CLOSING!!!")