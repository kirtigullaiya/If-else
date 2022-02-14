sell_price=int(input("please enter price:"))
cost_price=int(input("please enter price:"))
amount=sell_price-cost_price
if amount>=cost_price:
    print("you have gain profit")
elif amount<=cost_price:
    print("you have gain loss")
else:
    print("nuetral")


