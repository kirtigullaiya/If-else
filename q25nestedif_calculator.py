num1=int(input("please enter the number"))
num2=int(input("please enter the number"))
operators=("+,-,*,**,/,//,%,==,<,>")
if num1+num2:
    print("add=",num1+num2)
    if num1-num2:
        print("subtract=",num1-num2)
        if num1*num2:
            print("multipy=",num1*num2)
            if num1**num2:
                print("exponents",num1**num2)
                if num1/num2:
                    print("exponents=",num1**num2)
                    if num1//num2:
                        print("floordivision=",num1//num2)
                        if num1%num2:
                            print("modulus=",num1%num2)
                            if num1==num2:
                                print("equalto=",num1==num2)
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

