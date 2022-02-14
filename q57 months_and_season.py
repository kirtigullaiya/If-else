month=input("please enter month:")
season=input("please enter season:")
if month=="may" or "june" or "july" and season=="summer":
    print("it's very hot in these days")
    month=input("please enter month:")
    season=input("please enter season:")
    if month=="october" or "november" or "december" or "january" or "february" and season=="winter":
        print("it's very cold in delhi these days")
        month=input("please enter month:")
        season=input("please enter season:")
        if month=="august" or "september" and season=="monsoon":
            print("it's very sliparry on the roads.")
            month=input("plaese enter month:")
            season=input("please enter season:")
            if month=="march" or "april" and season=="spring":
                print("very beautiful season ")
            else:
                print("incorrect input")
        else:
            print("incorrect input")   
    else:
        print("incorrect input")
else:
    print("incorrect input")     