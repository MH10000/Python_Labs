'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
f = 100
c = round((f -32) * (5 / 9),1)
print(str(f) + " degrees fahrenheit = " + str(c) + " degrees celcius")

