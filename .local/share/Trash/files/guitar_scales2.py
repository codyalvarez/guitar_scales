def major():
    print("\nChoose A Major Scale")
    print("C | C#/D♭ | D | D#/E♭ | E | F | F#/G♭ | G | G#/A♭ | A | A#/B♭ | B")

    answer = input(">")

    if answer == "C":
        c()
    elif answer == "C#/D":
        c_sharp_d()
    elif answer == "D":
        d()
    elif answer == "D#/E":
        d_sharp_e()
    elif answer == "E":
        e()
    elif answer == "F":
        f()
    elif answer == "F#/G":
        f_sharp_g()
    elif answer == "G":
        g()
    elif answer == "G#/A":
        g_sharp_a
    elif answer == "A":
        a()
    elif answer == "A#/B":
        a_sharp_b()
    elif answer == "B":
        b()
    else:
        print("Thats not an option...")

def c():
    print("\nC")
    print("e|-------------------------------7-8-|")
    print("B|--------------------------8-10-----|")
    print("G|-------------------7-9-10----------|")
    print("D|------------7-9-10-----------------|")
    print("A|-----7-8-10------------------------|")
    print("E|8-10-------------------------------|")


major = {"C": "e|-------------------------------7-8-| B|--------------------------8-10-----| G|-------------------7-9-10----------| D|------------7-9-10-----------------| E|8-10-------------------------------| " }