def toCelsius(f):
    return (f-32)*5/9

def toFahrenheit(c):
    return c*9/5+32

inp = int(input("Insert Fahrenheit temperature:"))
convertF = toCelsius(inp)
print('{} Fahrenheit degrees is {} Celsius degrees'.format(inp, convertF))

inp2 = int(input("Insert Celsius temperature:"))
convertC = toFahrenheit(inp2)
print('{} Celsius degrees is {} Fahrenheit degrees'.format(inp, convertC))
