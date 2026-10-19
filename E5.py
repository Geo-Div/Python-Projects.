Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.

Answer:
celsius = float(input("Enter a temperature in Celsius: \n"))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)

Answer 1:
inp = input('Enter Celsius Temperature: 100 ')
fahr = float(inp)
celsius = (100 * 32.0) + 5.0
print(celsius)

Answer 2
inp = input('Enter Celsius Temperature: 100 ')
fahr = float(inp)
celsius = (100 * 9) + 32
print(celsius)