total=50000
print("welcome to SBI")
card=input("enter the card:")
if card=="debit card" or "credit card":
    print("Next")
    language=input("enter the language:")
    if language=="hindi" or "english":
        print("you can proceed further")
        pin=int(input("please enter the pin:"))
        if pin>=5:
            print("Next")
            transaction=input("enter your type of transaction:")
            if transaction=="deposit" or "withdrawal" or "transfer" or "balance":
                print("next")
                account=(input("enter the type of account:"))
                if account=="saving account" or "current account":
                    print("you can proceed further")
                    withdrawal=int(input("enter amount to be withdrawal:"))
                    if withdrawal<=15000:
                        print("your transaction is processing")
                        print("your remaining balance is", total-withdrawal)
                         #balance=int(input(" enter the ammount :"))
                         #if balance==50000:
                        #print(withdrawal-balance)
                        reciept=input("do you want reciept:")  
                        if reciept=="yes":
                            print("thank you")
                            thank_you=input("visit again")
                            if thank_you=="Okay":
                                print("Okay")   
                            else:
                                    print("not required")
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
                                                               
                           
                        




    

