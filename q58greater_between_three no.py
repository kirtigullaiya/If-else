num1=int(input("please enter number:"))
num2=int(input("please enter number:"))
num3=int(input("please enter number:"))
if num1>num2 and num2<num1:
    print(num1,"is oldest  and",num2,"is the youngest")
elif num2>num1 and num3<num2:
    print(num2,"is oldest and",num3,"is the youngest")
elif num3>num1 and num1<num3:
    print(num3,"is oldest and",num1,"is the youngest")
else:
    print("they are equal")