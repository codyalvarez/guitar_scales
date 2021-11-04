def main_menu():
    print("\nMAIN MENU")
    print("\nChoose A Scale to get rocking.")
    print("Major | Minor | Major Pentatonic | Minor Pentatonic | Minor Harmonic | Melodic Minor | Blues | Mixolydian | Dorian | Lydian")

    answer = input(">")

    if answer == "Major":
        major()
    elif answer == "Minor":
        minor()
    elif answer == "Major Pentatonic":
        major_pentatonic()
    elif answer == "Minor Pentatonic":
        minor_pentatonic()
    elif answer == "Minor Harmonic":
        minor_harmonic()
    elif answer == "Melodic Minor":
        melodic_minor()
    elif answer == "Blues":
        blues()
    elif answer == "Mixolydian":
        mixolydian()
    elif answer == "Dorian":
        dorian()
    elif answer == "Lydian":
        lydian()
    else:
        print("Thats not an option..")
        main_menu()

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

    print("\nType '1' or '2' or type exit to exit program.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        c()

def c_sharp_d():
    print("\nC#/D♭")
    print("e|---------------------------------8-9-|")
    print("B|----------------------------9-11-----|")
    print("G|--------------------8-10-11----------|")
    print("D|------------8-10-11------------------|")
    print("A|-----8-9-11--------------------------|")
    print("E|8-11---------------------------------|")

    print("\nType '1' or '2' or type exit to exit program.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")

    answer = input(">")

    if "1" in answer:
        c_sharp_d()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        c_sharp_d()

def d():
    print("\nD")
    print("e|--------------------------7-9-10-|")
    print("B|-------------------7-8-10--------|")
    print("G|-------------6-7-9---------------|")
    print("D|-------5-7-9---------------------|")
    print("A|-5-7-9---------------------------|")
    print("E|---------------------------------|")

    print("\nType '1' or '2' or type exit to exit program.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")

    answer = input(">")

    if "1" in answer:
        d()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d()


 
#   D#/E♭
# e|-----------------------------8-10-11-|
# B|----------------------8-9-11---------|
# G|---------------7-8-10----------------|
# D|--------6-8-10-----------------------|
# A|-6-8-10------------------------------|
# E|-------------------------------------|
 
#   E
# e|------------------------------9-11-12-|
# B|----------------------9-10-12---------|
# G|---------------8-9-11-----------------|
# D|--------7-9-11------------------------|
# A|-7-9-11-------------------------------|
# E|--------------------------------------|
 
#   F
# e|-------------------------------|
# B|-------------------------3-5-6-|
# G|-------------------2-3-5-------|
# D|-------------2-3-5-------------|
# A|-------1-3-5-------------------|
# E|-1-3-5-------------------------|
 
#   F#/G♭
# e|---------------------------1-2-|
# B|-----------------------2-4-----|
# G|-----------------1-3-4---------|
# D|-----------1-3-4---------------|
# A|-----1-2-4---------------------|
# E|-2-4---------------------------|
 
#   G
# e|----------------------------2-3-|
# B|------------------------3-5-----|
# G|------------------2-4-5---------|
# D|------------2-4-5---------------|
# A|-----2-3-5----------------------|
# E|-3-5----------------------------|
 
#   G#/A♭
# e|---------------------------3-4-|
# B|-----------------------4-6-----|
# G|-----------------3-5-6---------|
# D|-----------3-5-6---------------|
# A|-----3-4-6---------------------|
# E|-4-6---------------------------|
 
#   A
# e|---------------------------4-5-|
# B|-----------------------5-7-----|
# G|-----------------4-6-7---------|
# D|-----------4-6-7---------------|
# A|-----4-5-7---------------------|
# E|-5-7---------------------------|
 
#   A#/B♭
# e|---------------------------5-6-|
# B|-----------------------6-8-----|
# G|-----------------5-7-8---------|
# D|-----------5-7-8---------------|
# A|-----5-6-8---------------------|
# E|-6-8---------------------------|
 
#   B
# e|---------------------------6-7-|
# B|-----------------------7-9-----|
# G|-----------------6-8-9---------|
# D|-----------6-8-9---------------|
# A|-----6-7-9---------------------|
# E|-7-9---------------------------|
    




    main_menu()

def minor():
    print("\nChoose A Minor Scale")
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


    main_menu()

def major_pentatonic():
    print("Choose a Major Pentatonic Scale")
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


    main_menu()

def minor_pentatonic():
    print("\nChoose A Minor Pentatonic Scale")
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


    main_menu()

def minor_harmonic():
    print("\nChoose A Minor Harmonic")
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


    main_menu()

def melodic_minor():
    print("\nChoose A Melodic Minor Scale")
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


    main_menu()

def blues():
    print("\nChoose A Blues Scale")
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


    main_menu()

def mixolydian():
    print("\nChoose A Mixolydian Scale")
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


    main_menu()

def dorian():
    print("\nChoose A Dorian Scale")
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


    main_menu()

def lydian():
    print("\nChoose A Lydian Scale")
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


    main_menu()    

main_menu()



