permission=input("please enter permission:")
if permission=="disco permission":
    print("yes,you can go")
    sanitizer=input("enter sanitizer:")
    mask=input("enter mask:")
    if sanitizer=="yes we have" and mask=="yes we have":
        print("you can go")
        ng_work=input("enter ng_work reason:")
        if ng_work=="going to dmart":
            print("okk you can go") 
            coming_time=float(input("enter your coming_time:"))
            if coming_time<=6.00:
                print("you can go if coming time will be between",coming_time) 
                not_on_time=float(input("enter when not on time:"))
                if not_on_time>6.00:
                    print("you will have to qurantined in room")
        personal=input("enter personal reason:")
        if personal=="going to market":
            print("you can go but")
            coming_time=float(input("enter coming_time:"))
            if coming_time<=6.00:
                print("you can go if coming time will be between",coming_time)
                not_on_time=float(input("enter when not on time:"))
                if not_on_time>6.00:
                    print("you will have to quarantined in room")
                else:
                    print("no you can't go.")  
            else:
                print("no you can't go.")  
        else:
            print("no you can't go.")
    else:
        print("no you can't go.")
else:
    print("no you can't go")
