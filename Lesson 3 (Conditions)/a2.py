height = float(input("Enter your height"))
weight = float(input("Enter your weight"))

bmi = weight / (height/100)**2

print("Your BMI is:" , bmi)

if bmi < 18.5:
    print("You are underweight")

elif bmi <= 24.9:
    print("You are normal weight")

elif bmi <= 28.8:
    print("You are little heavy")

elif bmi <= 34.9:
    print("You are obese")

else: 
    print("You are extreamly obese :C")

