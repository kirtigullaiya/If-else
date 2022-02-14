alphabet=input("enter letters:")
if "A"<="Z" or "a"<="z":
    print("next")
    numbers=int(input("please enter numbers:"))
    if numbers>=1 and numbers<=99999:
        print("next")
        ch=input("enter special character:")
        if ch=="@" or "#" and "$":
            print("next")
            sum=alphabet+str(numbers)+ch
            if sum==sum:
                print("your password is:",sum)
            verification_code=int(input("plese enter code:"))
            if verification_code>=10 and verification_code<=200:
                print("confirmed")
                print("congo!")