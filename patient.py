# patient.py

class Patient:
    'Patient class for analysing various readings'
    def __init__(self, name) -> None:
        self.name = name
    def readings(self):
        print('Readings for', self.name)
        self.sugar = float(input('Sugar intake (gms): '))
        self.fat = float(input('Fat intake (gms): '))
        self.salt = float(input('Salt intake (mgms): '))
    def data_input(self):
        # input data
        self.readings()
        print('Is', self.name, "healthy:", self.healthy())
    def healthy(self):
        sugarL = 37.5
        fatL = 77
        saltL = 2300
        if self.sugar <= sugarL and self.fat <= fatL and self.salt <= saltL:
            return "Yes"
        else:
            return "No"

def run(name):
    p = Patient(name)
    p.data_input()

# main
patients = ['John', 'Jane', 'Clement']
for i in patients:
    run(i)