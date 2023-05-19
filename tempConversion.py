# a temperature conversion calculator ( from a celcius to fahrenhiet and vice versa )

# converts to fahrenheit
def convertToFahrenheit(degCel):
    return degCel * (9 / 5) + 32

# converts to celcius
def convertToCelsius(degFahren):
    return (degFahren - 32) * (5 / 9)

# asks users for the temperaute and unit
temp = int(input('The Temperature: '))
unit = str(input('The Unit to Convert it to? (f: fahrenheit, c: celsius): '))

if (unit == 'f'):
    print(round(convertToFahrenheit(temp), 2))
else: 
    print(round(convertToCelsius(temp), 2))