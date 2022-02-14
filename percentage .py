physics=int(input("please enter the marks"))        
chemistry=int(input("please enter the marks"))       
biology=int(input("please enter the marks"))      
mathematics=int(input("plaese enter the marks"))
computer=int(input("please enter the marks"))
total=physics+chemistry+biology+mathematics+computer
percentage=total/500*100
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("grade B")   
elif percentage>=70:
    print("grade C") 
elif percentage>=60:
    print("grade D")      
else:
    print("fail")                                                                                                                                                                                                                                                                                                                                                          