month=input("enter month:")
if month=="february":
    print("28 or 29 days")
elif month=="january"or "march"or "may"or "july"or "august"or "october"or "december":
    print("31 days")
elif month=="april"or "june"or "september"or "november":
    print("30 days")
else:
    print("wrong month")