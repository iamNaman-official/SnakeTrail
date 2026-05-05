# This is my second mini project in Python.
# It calculates the Body Mass Index (BMI) based on user input for weight and height.
print("Welcome to BMI Calculator!")
weight =float(input("Enter your weiht in kg: \n"))
height = float(input("Enter your height in meters: \n"))
# The formula for calculating BMI is weight (kg) / (height (m) ** 2)
bmi = weight / (height**2) 
print("Your BMI is:" + str(bmi))

