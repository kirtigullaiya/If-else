num1=int(input("please enter number"))
num2=int(input("please enter number"))
num3=int(input("please enter number"))
if num1>num2 and num1>num3:
    print(num1, "is greater")
elif num2>num1 and num2>num3:
    print(num2, "is greatest")
elif num3>num1 and num3>num2:
    print(num3,"is greatest")
else:
    print("all are equal")