name=input("enter the name:")
basic_salary=int(input("enter salary"))
if basic_salary<=10000:
    hra=basic_salary*20/100
    da=basic_salary*80/100
    gross_salary=basic_salary+hra+da
    print(gross_salary,"salary")
elif basic_salary<=20000:
    hra=basic_salary*25/100
    da=basic_salary*90/100
    gross_salary=basic_salary+hra+da
    print(gross_salary,"salary")
elif basic_salary>20000:
    hra=basic_salary*30/100
    da=basic_salary*95/100
    gross_salary=basic_salary+hra+da
    print(gross_salary,"salary")
else:
    print("not valid")
