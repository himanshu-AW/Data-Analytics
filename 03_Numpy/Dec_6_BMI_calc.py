# BMI(Body Mass index) 
import numpy as np

# Get user input for weight and height
weight = np.array(float(input("Enter yor weight(kg) : ")))
height = float(input("Enter your height(meter): "))

BMI = weight / (height**2)

if BMI < 18.5:
    print(f"Your Body Mass Index is {BMI} and You are Underweight")
elif BMI >= 18.5 and BMI < 24.5 :
    print(f"Your Body Mass Index is {BMI} and You are Normal weight")
elif BMI >=24.5 and BMI < 29.9:
    print(f"Your Body Mass Index is {BMI} and You are Overweight")
elif BMI >= 29.9 :
    print(f"Your Body Mass Index is {BMI} and You are Obesity")