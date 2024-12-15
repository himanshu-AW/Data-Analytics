# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = (f-32)/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]  
# Expected Output : -----
# 60°C is 140 in Fahrenheit  
# 45°F is 7 in Celsius 


def celcius_to_fahrenheit(temp):
    return temp*9/5 +32

def fahrenheit_to_celsius(temp):
    return (temp-32)*5/9

celcius = 2
print(f"=>Celcius: {celcius} to Fahrenheit: {celcius_to_fahrenheit(celcius)}")
fahrenheit = 2
print(f"=>Fahrenheit: {fahrenheit} to Celcius: {fahrenheit_to_celsius(fahrenheit)}")