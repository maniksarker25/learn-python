# <,>,<=,>=,== ,!=
a = 2
boss = True
if a > 5:
    print("5 ar basi")
    print("koto basi ka jana")
elif a > 3:
    print("3 ar chaita boro")
elif a == 2:
    print("Akdom 2 ar soman soman")
else:
    print("5 ar soto")


if boss is True:
    print("Tel ar bokso nia astasi , boss ra tel dimu ra")
else:
    print("Lunch er pora asen")

if boss is not True:
    print("Lunch ar pora achen")
else:
    print("Tel ar bokso nia astasi , boss ra tel dimu ra")

coin = 'head'
if boss == True:
    print("Boss you are joss")
    if coin == 'tail':
        print("Bating")
    else:
        print("Bowling")
else:
    print("You are loss to boss")