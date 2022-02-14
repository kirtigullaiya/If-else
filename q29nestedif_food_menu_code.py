day=input("please enter day:")
meal=input("please enter meal:")
if day=="monday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("daal chawal")
    elif meal=="dinner":
        print("aalu roti")
    else:
        print("malpua")
elif day=="tuesday":
    if meal=="breakfast" :
        print("sabudana")      
    elif meal=="lunch":
        print("chole chawal")
    elif meal=="dinner":
        print("bhindi roti")
    else:
        print("barfi")
elif day=="wednesday":
    if meal=="breakfast":
        print("oats")
    elif meal=="lunch":
        print("pulao")
    elif meal=="dinner":
        print("shepu roti")
    else:
        print("fried rice")
elif day=="thursday":
    if meal=="breakfast":
        print("upma")
    elif meal=="lunch":
        print("baigan roti")
    elif meal=="dinner":
        print("rajma chawal")
    else:
        print("paranthe")
elif day=="friday":
    if meal=="breakfast":
        print("idli")
    elif meal=="lunch":
        print("loki roti")
    elif meal=="dinner":
        print("paneer roti")
    else:
        print("murmure")
elif day=="saturday":
    if meal=="beakfast":
        print("kadha")
    elif meal=="lunch":
        print("soyabean roti")
    elif meal=="dinner":
        print("lobhia chawal")
    else:
        print("chivda")
elif day=="sunday":
    if meal=="breakfast":
        print("vada")
    elif meal=="lunch":
        print("tamatar pyaaj")
    elif meal=="dinner":
        print("gobhi")
    else:
        print("maggi")
else:
    print("thali")        

