"""Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
[ Formula: c/5 = f - 32/9 [where c = temperature in Celsius and f = temperature in Fahrenheit]
Expected Output:
60°C is 140 in Fahrenheit 45°F is 7 in Celsius"""

c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(c, "°C is" , int(f) , "in Fahrenheit")

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5/9
print(f, "°F is", int(c), "in Celsius")