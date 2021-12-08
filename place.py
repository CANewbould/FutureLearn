#place.py
 
# Author: C A Newbould

# Version 1

# Base class used by WeatherStation

class Place:
    'This is the base class for all Places registered'
    def __init__ (self, name, latitude, longitude): # Constructor
        # properties
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    # methods  
    def getName(self):
        return self.name
