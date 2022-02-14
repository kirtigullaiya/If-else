water=int(input("please enter litres"))
if water<1:
    print("needs to be filled")
elif water<10:
    print("no need to be filled")
else:
    print("water will overflow")