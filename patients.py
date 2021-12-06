# patients.py

# Author: C A Newbould

# Version 1

# Created by splitting class from 'main'


from patient import Patient # new to me - needed __init__.py to exist

def run(name):
    p = Patient(name)
    p.data_input()

# main
patients = ['John', 'Jane', 'Clement']
for i in patients:
    run(i)