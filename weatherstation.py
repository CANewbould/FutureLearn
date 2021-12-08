#weatherstation.py
 
# Author: C A Newbould

# Version 2
# defined the words to be output for temperatures as a list
# used the 'bisect' module -- thanks to stackoverflow - to create my one-liner

from place import Place

import bisect

temps = ['chilly','cold','cool','mild','warm']
winds = ['calm', 'quite calm', 'breezy', 'windy']

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
        word = temps[bisect.bisect_left([5,10,15,20], self.temperature)]
        print(word, end = ", ")
        if self.rain > 0:
            noLF('wet')
        else:
            noLF('dry')
        print(' and ',end = "")
        wnd = winds[bisect.bisect_left([5,10,20], self.wind)]
        print(wnd, end = " ")
        print ("in " + self.name + '.')
   