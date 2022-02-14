charges=int(input("please enter the number"))
per_unit=float(input("please enter the number"))
total_bill=(charges*per_unit)+20/100
if charges<50:
    print("low electricity bill")
elif charges>50 and charges<100:
    print("medium electricity bill")
elif charges>100 and charges<200:
    print("a little high electricity bill")
elif charges>250:
    print("higher electricity bill")
else:
    print("not valid")