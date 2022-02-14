year=input("please enter year:")
month=input("please enter month:")
date=int(input("please enter date:"))
if date>1 and date<31 or month>1 and month<12 :
    print(date,"/",month,"/",year)
else:
    print("incorrect")
