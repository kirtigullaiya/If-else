name=input("please enter name:")
if name==name:
    print("next")
    user_name=input("please enter user_name:")
    if user_name==user_name:
        print("next")
        password=input("enter password:")
        if password<="letters" and "numbers" and "special characters":
            print("next")
            phone_number=int(input("enter the phone number:"))
            if phone_number>=10:
                print("next")
                verification_code=int(input("enter verification_code:"))
                if verification_code>=3:
                    print("next")
                    DOB=int(input("enter DOB:"))
                    if DOB==DOB:
                        print("next")
                        gender=input("enter gender:")
                        if gender=="male" or "female" or "custom" or "third gender":
                            print("next")
                            sign_up=input("enter signing:")
                            if sign_up==("completed"):
                                print("congratulations")
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
else:
    print("not valid")                                                    