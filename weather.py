# Get the current temperature, today's high, and today's low for a given ZIP code
# using OpenWeatherMap.org's Weather API


# Imports
import requests
import json

# User input for API key and ZIP Code
api_key = input("Enter your API Key: ")
zip_code = str(input("Enter your zip code: "))

# GET request for data
r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + ",us&units=imperial&APPID=" + api_key)

# Convert to JSON
data = r.json()

# Pull main data into a dictionary, index temp, temp_high and temp_low
main_data = data['main']
current_temp = main_data['temp']
temp_high = main_data['temp_max']
temp_low = main_data['temp_min']

# Print values to console
print("Current temperature in: " + zip_code + ": " + str(current_temp) + " degrees Fahrenheit")
print("Today's high temperature in: " + zip_code + ": " + str(temp_high) + " degrees Fahrenheit")
print("Today's low temperature in: " + zip_code + ": " + str(temp_low) + " degrees Fahrenheit")