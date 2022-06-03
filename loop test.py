fullname= input("Enter your Fullname")
lbs = input("Weight in lbs?")
kg = int(lbs) / 2.205 
print("you weight is " , + round(kg,2)  , "Kg")
if kg >=100:
    print("You need to excercise")
elif kg <=30:
    print("You need to eat more")
else:
     print("You're on a healthy weight, make sure to keep it that way")
#The bmi formula is not working telling me bad operand even if i use float it doesn't work.
height_m = input("What is your height?(m)")
bmi = kg/ (int(height_m)^2)
print("Your BMI is: ", + bmi)