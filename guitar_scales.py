def main_menu():
    print("\nMAIN MENU")
    print("\nChoose A Scale to get rocking.")
    print("Major | Minor | Major Pentatonic | Minor Pentatonic | Minor Harmonic | Melodic Minor | Blues | Mixolydian | Dorian | Lydian")
    print("\nType 'exit' to exit program.")

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
    elif answer == "exit" or answer == "Exit":
        exit
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

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

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

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
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

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d()

def d_sharp_e():
    print("\nD#/E♭")
    print("e|-----------------------------8-10-11-|")
    print("B|----------------------8-9-11---------|")
    print("G|---------------7-8-10----------------|")
    print("D|--------6-8-10-----------------------|")
    print("A|-6-8-10------------------------------|")
    print("E|-------------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d_sharp_e()

def e():
    print("\nE") 
    print("e|------------------------------9-11-12-|")
    print("B|----------------------9-10-12---------|")
    print("G|---------------8-9-11-----------------|")
    print("D|--------7-9-11------------------------|")
    print("A|-7-9-11-------------------------------|")
    print("E|--------------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        e()

def f():
    print("\nF")

    print("e|-------------------------------|")
    print("B|-------------------------3-5-6-|")
    print("G|-------------------2-3-5-------|")
    print("D|-------------2-3-5-------------|")
    print("A|-------1-3-5-------------------|")
    print("E|-1-3-5-------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        f()

def f_sharp_g():
    print("\nF#/G♭") 
    print("e|---------------------------1-2-|")
    print("B|-----------------------2-4-----|")
    print("G|-----------------1-3-4---------|")
    print("D|-----------1-3-4---------------|")
    print("A|-----1-2-4---------------------|")
    print("E|-2-4---------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        f_sharp_g()
 
def g():
    print("\nG")    
    print("e|----------------------------2-3-|")
    print("B|------------------------3-5-----|")
    print("G|------------------2-4-5---------|")
    print("D|------------2-4-5---------------|")
    print("A|-----2-3-5----------------------|")
    print("E|-3-5----------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        g()

def g_sharp_a():
    print("G#/A♭") 
    print("e|---------------------------3-4-|")
    print("B|-----------------------4-6-----|")
    print("G|-----------------3-5-6---------|")
    print("D|-----------3-5-6---------------|")
    print("A|-----3-4-6---------------------|")
    print("E|-4-6---------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        g_sharp_a()

def a():
    print("\nA") 
    print("e|---------------------------4-5-|")
    print("B|-----------------------5-7-----|")
    print("G|-----------------4-6-7---------|")
    print("D|-----------4-6-7---------------|")
    print("A|-----4-5-7---------------------|")
    print("E|-5-7---------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        a()

def a_sharp_b():
    print("\nA#/B♭")
    print("e|---------------------------5-6-|")
    print("B|-----------------------6-8-----|")
    print("G|-----------------5-7-8---------|")
    print("D|-----------5-7-8---------------|")
    print("A|-----5-6-8---------------------|")
    print("E|-6-8---------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        a_sharp_b()

def b():
    print("\nB")
    print("e|---------------------------6-7-|")
    print("B|-----------------------7-9-----|")
    print("G|-----------------6-8-9---------|")
    print("D|-----------6-8-9---------------|")
    print("A|-----6-7-9---------------------|")
    print("E|-7-9---------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        b()
    
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



