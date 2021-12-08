#weatherstation.py
 
# Author: C A Newbould

# Version 1

from place import Place

def noLF(text):
    print(text, end = "")

class WeatherStation(Place):
    'WeatherStation class for analysing various readings'
    # WeatherStation(name, latitude, longitude) - use Place constructor implicitly
    def readings(self):
        print('Readings for', self.name)
        self.temperature = float(input("Temperature now(C): "))
        self.rain = float(input('Rainfall in last hour (mm): '))
        self.wind = float(input('Current wind speed (mph): '))
    def report(self):
        noLF('It is ')
        if self.temperature >= 20:
            print("warm", end = ", ")
        elif self.temperature in range(15,20):
            print('mild', end = ", ")
        elif self.temperature in range(10,15):
            print('cool', end = ", ")
        elif self.temperature in range(5,10):
            print('cold', end = ", ")
        else:
            print("chilly", end = ", ")
        if self.rain > 0:
            noLF('wet')
        else:
            noLF('dry')
        print(' and ',end = "")
        if self.wind > 20:
            noLF('windy ')
        elif self.wind in range(10,20):
            noLF('breezy ')
        elif self.wind in range(5,10):
            noLF('quite calm ')
        else:
            noLF('calm ')
        print ("in " + self.name + '.')
   