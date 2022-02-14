a=int(input("please enter number:"))
b=int(input("please enter number:"))
c=int(input("please enter number:"))
if a==b and b==c:
    print("equilateral triangle")
elif a==b or b==c:
    print("isoceles triangle") 
else:
    print("scalene triangle")