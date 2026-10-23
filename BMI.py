Weight=input("Your Weight in KG\n")
Height=input("Your Height in Meter\n")
W=float(Weight)
H=float(Height)
bmi=W/(H**2)
print("Your BMI is = "+str(bmi))
if bmi<=18:
    print("you are under Weight")
elif bmi<25:
     print("you have a Normal Weight")
else:
     print("you are Over Weight")

