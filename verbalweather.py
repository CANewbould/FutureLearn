# verbalweather.py
 
# Author: C A Newbould

# Version 2

# Reflecting changes made to weatherstation.py
# defined the words to be output for temperatures as a list
# used the 'bisect' module -- thanks to stackoverflow - to create my one-liner
# included a test case, now commented out

from weatherstation import WeatherStation
import bisect

temps = ['chilly','cold','cool','mild','warm']
winds = ['calm', 'quite calm', 'breezy', 'windy']

def noLF(text):
    print(text, end = "")

class VerbalWeather(WeatherStation):
    def report(self):
        noLF('It is ')
        print(temps[bisect.bisect_left([5,10,15,20], self.temperature)], end = ", ")
        if self.rain > 0:
            noLF('wet')
        else:
            noLF('dry')
        print(' and ',end = "")
        print(winds[bisect.bisect_left([5,10,20], self.wind)], end = " ")
        print ("in " + self.name + '.')

# test
#Arnside = VerbalWeather("Arnside", 54.203808, -2.832755)
#Arnside.readings()
#Arnside.in_words()
#Arnside.report()