quantity=int(input("please enter quantity"))
cost_of_one_unit=int(input("enter cost"))
amount=cost_of_one_unit*quantity
if amount>=1000:
    print("give discount")
else:
    print("dont give discount")    