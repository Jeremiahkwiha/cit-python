CELICIUS=1
FAHRANHEIT=2
temp = float(input("1 for celicius to fahranheit and 2 for fahranheit to celicius"))
if temp==CELICIUS:
    cel=(value-32)*9/5
    fah=(cel*1.8)+32
    print(str(cel) + "in celicius is equal to " + str(fah) + "in fahranheit")
elif temp==FAHRANHEIT:
    cel=(value-32)*9/5
    fah=(cel*1.8)+32
    print(str(fah) + "in fahranheit is equal to " + str(cel) + "in celicius")
else:
    print("Invalid choice, choose the given options!")