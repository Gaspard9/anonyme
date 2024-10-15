h=float(input("enter your height"))
w=float(input("enter your weight"))
bmi=w/(h*h)

if bmi<18.5 :
    print("you are underweight")

elif bmi>18.5 and bmi<24.5 :
    print("you are normal weight")

else :
    print("you are overweight")
