print("-"*15)
print("Calculates the BMI ")
print("-"*15)

# Ask the user 
wieght = float(input("Enter your wieght: "))
height = float(input("Enter your height: "))

heightInMeter= height / 100

# Calculate BMI
BMI = (wieght / (heightInMeter**2)) 
print("BMI is : ", round(BMI,2))

# If condition & print the BMI for the user
if BMI >= 25 :
    print("You are overwieght you need to work out more and watch your diet")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are fit & healthy.")
elif BMI < 18.5:
    print("underweight. Watch your health.")

