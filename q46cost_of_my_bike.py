cost_of_bike=int(input("enter price:"))
tax=cost_of_bike*int(input("enter percentage:"))/100
if cost_of_bike>100000 and tax==tax:
    print("road tax wil be",tax)
elif cost_of_bike>50000 and cost_of_bike<=100000 and tax==tax:
    print("road tax wil be",tax)
elif cost_of_bike<=50000 and tax==tax:
    print("road tax will be",tax)
else:
    print("not purcharsing bike")