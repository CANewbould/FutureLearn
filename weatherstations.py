# weatherstations.py

# main

from weatherstation import WeatherStation

Arnside = WeatherStation("Arnside", 54.203808, -2.832755)
Finisterre = WeatherStation("Finisterre", 42.7, -9.27)
Tenerife = WeatherStation("Tenerife", 28.291564,  -16.629130)

statns = [Arnside, Finisterre, Tenerife]

print("Collect readings\n")
for i in statns:
    i.readings()

print("\n\nWeather reports:\n----------------")
for i in statns:
    i.report()
