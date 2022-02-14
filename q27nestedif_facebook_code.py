name=input("plese enter name:")
if name==name:
    print("next")
    DOB=(input("please enter DOB:"))
    if DOB==DOB:
        print("next")
        gender=input("please enter gender:")
        if gender=="male" or "female" or "custom":
            print("next")
            mobile_no=int(input("please enter number:"))
            if mobile_no>=10:
                print("next")
                email=input("please enter email:")
                if email and "@gmail.com"in email:
                    print("next")
                    password=int(input("please enter password:"))
                    if password>="a" and  password<="z" and password=="numbers":
                        print("next")
                        sign_up=input("please confirm your details:")
                        if sign_up=="confirmed":
                            print("signup finish")
                        else:
                            print("not valid")
                    else:
                        print("not valid")
                else:
                    print("not valid")        
            else:
                print("not valid") 
        else:
            print("not valid")  
    else:
        print("not valid")
else:
    print("not valid")                             