# weatherstations.py

# main

# Version 2

# modified to be based on VerbalWeather, after moving material around
# now have VerbalWeather inheriting WeatherStation, which inherits from Place

from verbalweather import VerbalWeather

Arnside = VerbalWeather("Arnside", 54.203808, -2.832755)
Finisterre = VerbalWeather("Finisterre", 42.7, -9.27)
Tenerife = VerbalWeather("Tenerife", 28.291564,  -16.629130)

statns = [Arnside, Finisterre, Tenerife]

print("Collect readings\n----------------")
for i in statns:
    i.readings()

print("\n\nWeather reports:\n----------------")
for i in statns:
    i.report()
