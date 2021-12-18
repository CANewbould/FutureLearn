#weatherstation.py
 
# Author: C A Newbould

# Version 2
# stripped all but essentials - just readings
# added testing routine
# and (commented-out) test case

from place import Place

class WeatherStation(Place):
    'WeatherStation class for analysing various readings'
    # WeatherStation(name, latitude, longitude) - use Place constructor implicitly
    def readings(self):
        print('Readings for', self.name)
        self.temperature = float(input("Temperature now(C): "))
        self.rain = float(input('Rainfall in last hour (mm): '))
        self.wind = float(input('Current wind speed (mph): '))
    def in_words(self):
        print(f'It is {self.temperature}C, {self.rain:.0f}mm and {self.wind:.0f}mph in {self.name}.')

# test
#Arnside = WeatherStation("Arnside", 54.203808, -2.832755)
#Arnside.readings()
#Arnside.in_words()
