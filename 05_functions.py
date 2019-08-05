# function to convert temperature in Kelvin to temperatures in degree celsius
def kelvin_to_celsius(temperature):
    return temperature - 273


print(kelvin_to_celsius(298))

# lambda function
result = (lambda temperature: temperature - 273)(250)
print(result)

kelvin_temperatures = [298, 278, 305, 245, 0, 100, 300, 400]
# convert all the temperatures in the above list into celsius
celsius_temperatures = list(map(kelvin_to_celsius, kelvin_temperatures))
print(celsius_temperatures)
# filtering out temperatures below freezing point
temp_below_zero = list(filter(lambda x: x < 0, celsius_temperatures))
print(temp_below_zero)
