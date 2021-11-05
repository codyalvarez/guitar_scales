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

def minor():
    print("\nChoose A Minor Scale")
    print("C | C#/D♭ | D | D#/E♭ | E | F | F#/G♭ | G | G#/A♭ | A | A#/B♭ | B")

    answer = input(">")

    if answer == "C":
        c1()
    elif answer == "C#/D":
        c_sharp_d1()
    elif answer == "D":
        d1()
    elif answer == "D#/E":
        d_sharp_e1()
    elif answer == "E":
        e1()
    elif answer == "F":
        f1()
    elif answer == "F#/G":
        f_sharp_g1()
    elif answer == "G":
        g1()
    elif answer == "G#/A":
        g_sharp_a1()
    elif answer == "A":
        a1()
    elif answer == "A#/B":
        a_sharp_b1()
    elif answer == "B":
        b1()
    else:
        print("Thats not an option...")

def c1():
    print("\nC")
    print("e|-------------------------------------8-|")
    print("B|------------------------------8-9-11---|")
    print("G|-------------------------8-10----------|")
    print("D|-----------------8-10-12---------------|")
    print("A|---------8-10-11-----------------------|")
    print("E|-8-10-11-------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        c1()
 
def c_sharp_d1():    
    print("C#/D♭")
    print("e|--------------------------------------9-|")
    print("B|------------------------------9-10-12---|")
    print("G|-------------------------9-11-----------|")
    print("D|-----------------9-11-13----------------|")
    print("A|---------9-11-12------------------------|")
    print("E|-9-11-12--------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        c_sharp_d1()
 
def d1():
    print("\nD")
    print("e|---------------------------6-8-10-|")
    print("B|-------------------6-8-10---------|")
    print("G|-------------5-7-9----------------|")
    print("D|-------5-7-8----------------------|")
    print("A|-5-7-8----------------------------|")
    print("E|----------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d1()

def d_sharp_e1():
    print("\nD#/E♭") 
    print("e|---------------------------7-9-11-|")
    print("B|--------------------7-9-11--------|")
    print("G|-------------6-8-10---------------|")
    print("D|-------6-8-9----------------------|")
    print("A|-6-8-9----------------------------|")
    print("E|----------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d_sharp_e1()
 
def e1():
    print("\nE")    
    print("e|------------------------------8-10-12-|")
    print("B|----------------------8-10-12---------|")
    print("G|---------------7-9-11-----------------|")
    print("D|--------7-9-10------------------------|")
    print("A|-7-9-10-------------------------------|")
    print("E|--------------------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        e1()
 
def f1():
    print("\nF")
    print("e|-----------------------------1-|")
    print("B|-----------------------1-2-5---|")
    print("G|-------------------1-3---------|")
    print("D|-------------1-3-5-------------|")
    print("A|-------1-3-4-------------------|")
    print("E|-1-3-4-------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        f1()

def f_sharp_g1():
    print("\nF#/G♭") 
    print("e|-----------------------------2-|")
    print("B|-----------------------2-3-5---|")
    print("G|-------------------2-4---------|")
    print("D|-------------2-4-6-------------|")
    print("A|-------2-4-5-------------------|")
    print("E|-2-4-5-------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        f_sharp_g1()
 
def g1():
    print("\nG")
    print("e|-----------------------------3-|")
    print("B|-----------------------3-4-6---|")
    print("G|-------------------3-5---------|")
    print("D|-------------3-5-7-------------|")
    print("A|-------3-5-6-------------------|")
    print("E|-3-5-6-------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        g1()

def g_sharp_a1():
    print("\nG#/A♭")
    print("e|-----------------------------4-|")
    print("B|-----------------------4-5-7---|")
    print("G|-------------------4-6---------|")
    print("D|-------------4-6-8-------------|")
    print("A|-------4-6-7-------------------|")
    print("E|-4-6-7-------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        g_sharp_a1()
        
def a1():
    print("\nA") 
    print("e|-----------------------------5-|")
    print("B|-----------------------5-6-8---|")
    print("G|-------------------5-7---------|")
    print("D|-------------5-7-9-------------|")
    print("A|-------5-7-8-------------------|")
    print("E|-5-7-8-------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        a1()

def a_sharp_b1():
    print("\nA#/B♭") 
    print("e|------------------------------6-|")
    print("B|------------------------6-7-9---|")
    print("G|--------------------6-8---------|")
    print("D|-------------6-8-10-------------|")
    print("A|-------6-8-9--------------------|")
    print("E|-6-8-9--------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        a_sharp_b1()

def b1():
    print("\nB")
    print("e|---------------------------------7-|")
    print("B|--------------------------7-8-10---|")
    print("G|----------------------7-9----------|")
    print("D|---------------7-9-11--------------|")
    print("A|--------7-9-10---------------------|")
    print("E|-7-9-10----------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Minor Scale")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        minor()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        b1()

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

def c2():
    print("\nC")
    print("e|-------------------5-8-|")
    print("B|---------------5-8-----|")
    print("G|-----------5-7---------|")
    print("D|-------5-7-------------|")
    print("A|---5-7-----------------|")
    print("E|-8---------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Pentatonic")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major_pentatonic()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        c2()
 
def c_sharp_d2():
    print("\nC#/D♭")
    print("e|-------------------6-9-|")
    print("B|---------------6-9-----|")
    print("G|-----------6-8---------|")
    print("D|-------6-8-------------|")
    print("A|---6-8-----------------|")
    print("E|-9---------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Pentatonic")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major_pentatonic()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        c_sharp_d2()

def d2():
    print("\nD")
    print("e|-------------------------|")
    print("B|--------------------7-10-|")
    print("G|---------------7-10------|")
    print("D|-----------7-9-----------|")
    print("A|-------7-9---------------|")
    print("E|-5-7-9-------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Pentatonic")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major_pentatonic()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d2()

def d_sharp_e2():
    print("\nD#/E♭")
    print("e|-----------------------8-11-|")
    print("B|------------------8-11------|")
    print("G|-------------8-10-----------|")
    print("D|--------8-10----------------|")
    print("A|-6-8-10---------------------|")
    print("E|----------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Pentatonic")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major_pentatonic()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        d_sharp_e2()

def e2():
    print("\nE")
    print("e|-----------------------9-12-|")
    print("B|------------------9-12------|")
    print("G|-------------9-11-----------|")
    print("D|--------9-11----------------|")
    print("A|-7-9-11---------------------|")
    print("E|----------------------------|")

    print("\nType '1' or '2'.")
    print("1. ) Choose another Major Pentatonic")
    print("2. ) Return To Main Menu")
    print("\nType 'exit' to exit program.")

    answer = input(">")

    if "1" in answer:
        major_pentatonic()
    elif "2" in answer:
        main_menu()
    elif "exit" in answer:
        exit
    else:
        print("Thats not an option...")
        e2()

def f2():


 
#   F
# e|-----------------------|
# B|-------------------3-6-|
# G|---------------2-5-----|
# D|-----------3-5---------|
# A|-------3-5-------------|
# E|-1-3-5-----------------|
 
#   F#/G♭
# e|----------------------2-|
# B|------------------2-4---|
# G|-------------1-3--------|
# D|---------1-4------------|
# A|-----1-4----------------|
# E|-2-4--------------------|
 
#   G
# e|---------------------3-|
# B|-----------------3-5---|
# G|-------------2-4-------|
# D|---------2-5-----------|
# A|-----2-5---------------|
# E|-3-5-------------------|
 
#   G#/A♭
# e|---------------------4-|
# B|-----------------4-6---|
# G|-------------3-5-------|
# D|---------3-6-----------|
# A|-----3-6---------------|
# E|-4-6-------------------|
 
#   A
# e|---------------------4-|
# B|-----------------5-7---|
# G|-------------4-6-------|
# D|---------4-7-----------|
# A|-----4-7---------------|
# E|-5-7-------------------|
 
#   A#/B♭
# e|---------------------6-|
# B|-----------------6-8---|
# G|-------------5-7-------|
# D|---------5-8-----------|
# A|-----5-8---------------|
# E|-6-8-------------------|
 
#   B
# e|---------------------7-|
# B|-----------------7-9---|
# G|-------------6-8-------|
# D|---------6-9-----------|
# A|-----6-9---------------|
# E|-7-9-------------------|
 

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

# Minor Pentatonic
 
#   C
# e|--------------------------8-|
# B|---------------------8-11---|
# G|----------------8-10--------|
# D|-----------8-10-------------|
# A|------8-10------------------|
# E|-8-11-----------------------|
 
#   C#/D♭
# e|--------------------------9-|
# B|---------------------9-12---|
# G|----------------9-11--------|
# D|-----------9-11-------------|
# A|------9-11------------------|
# E|-9-12-----------------------|
 
#   D
# e|---------------------8-10-|
# B|----------------8-10------|
# G|---------5-7-10-----------|
# D|-----5-7------------------|
# A|-5-8----------------------|
# E|--------------------------|
 
#   D#/E♭
# e|---------------------9-12-|
# B|----------------9-12------|
# G|---------6-8-12-----------|
# D|-----6-8------------------|
# A|-6-9----------------------|
# E|--------------------------|
 
#   E
# e|-----------------------10-12-|
# B|-----------------10-12-------|
# G|----------7-9-12-------------|
# D|------7-9--------------------|
# A|-7-10------------------------|
# E|-----------------------------|
 
#   F
# e|---------------------1-|
# B|-----------------1-4---|
# G|-------------1-3-------|
# D|---------1-3-----------|
# A|-----1-3---------------|
# E|-1-4-------------------|
 
#   F#/G♭
# e|---------------------2-|
# B|-----------------2-5---|
# G|-------------2-4-------|
# D|---------2-4-----------|
# A|-----2-4---------------|
# E|-2-5-------------------|
 
#   G
# e|---------------------3-|
# B|-----------------3-6---|
# G|-------------3-5-------|
# D|---------3-5-----------|
# A|-----3-5---------------|
# E|-3-6-------------------|
 
#   G#/A♭
# e|---------------------4-|
# B|-----------------4-7---|
# G|-------------4-6-------|
# D|---------4-6-----------|
# A|-----4-6---------------|
# E|-4-7-------------------|
 
#   A
# e|---------------------5-|
# B|-----------------5-8---|
# G|-------------5-7-------|
# D|---------5-7-----------|
# A|-----5-7---------------|
# E|-5-8-------------------|
 
#   A#/B♭
# e|---------------------6-|
# B|-----------------6-9---|
# G|-------------6-8-------|
# D|---------6-8-----------|
# A|-----6-8---------------|
# E|-6-9-------------------|
 
#   B
# e|-----------------------7-|
# B|------------------7-10---|
# G|--------------7-9--------|
# D|----------7-9------------|
# A|------7-9----------------|
# E|-7-10--------------------|
 

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

# Minor Harmonic
 
#   C
# e|-------------------------------------8-|
# B|------------------------------8-9-12---|
# G|-------------------------8-10----------|
# D|-----------------9-10-12---------------|
# A|---------8-10-11-----------------------|
# E|-8-10-11-------------------------------|
 
#   C#/D♭
# e|---------------------------------------9-|
# B|-------------------------------9-10-13---|
# G|--------------------------9-11-----------|
# D|-----------------10-11-13----------------|
# A|---------9-11-12-------------------------|
# E|-9-11-12---------------------------------|
 
#   D
# e|--------------------------6-9-10-|
# B|-------------------6-8-10--------|
# G|-------------6-7-9---------------|
# D|-------5-7-8---------------------|
# A|-5-7-8---------------------------|
# E|---------------------------------|
 
#   D#/E♭
# e|---------------------------7-10-11-|
# B|--------------------7-9-11---------|
# G|-------------7-8-10----------------|
# D|-------6-8-9-----------------------|
# A|-6-8-9-----------------------------|
# E|-----------------------------------|
 
#   E
# e|------------------------------8-11-12-|
# B|----------------------8-10-12---------|
# G|---------------8-9-11-----------------|
# D|--------7-9-10------------------------|
# A|-7-9-10-------------------------------|
# E|--------------------------------------|
 
#   F
# e|-----------------------------1-|
# B|-----------------------1-2-5---|
# G|-------------------1-3---------|
# D|-------------2-3-5-------------|
# A|-------1-3-4-------------------|
# E|-1-3-4-------------------------|
 
#   F#/G♭
# e|-----------------------------2-|
# B|-----------------------2-3-6---|
# G|-------------------2-4---------|
# D|-------------3-4-6-------------|
# A|-------2-4-5-------------------|
# E|-2-4-5-------------------------|
 
#   G
# e|-----------------------------3-|
# B|-----------------------3-4-7---|
# G|-------------------3-5---------|
# D|-------------4-5-7-------------|
# A|-------3-5-6-------------------|
# E|-3-5-6-------------------------|
 
#   G#/A♭
# e|-----------------------------4-|
# B|-----------------------4-5-8---|
# G|-------------------4-6---------|
# D|-------------5-6-8-------------|
# A|-------4-6-7-------------------|
# E|-4-6-7-------------------------|
 
#   A
# e|-----------------------------5-|
# B|-----------------------5-6-9---|
# G|-------------------5-7---------|
# D|-------------6-7-9-------------|
# A|-------5-7-8-------------------|
# E|-5-7-8-------------------------|
 
#   A#/B♭
# e|-------------------------------6-|
# B|------------------------6-7-10---|
# G|--------------------6-8----------|
# D|-------------7-8-10--------------|
# A|-------6-8-9---------------------|
# E|-6-8-9---------------------------|
 
#   B
# e|---------------------------------7-|
# B|--------------------------7-8-11---|
# G|----------------------7-9----------|
# D|---------------8-9-11--------------|
# A|--------7-9-10---------------------|
# E|-7-9-10----------------------------|
 

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

# Melodic Minor
 
#   C
# e|-------------------------5-7-8-|
# B|---------------------6-8-------|
# G|---------------5-7-8-----------|
# D|---------5-7-9-----------------|
# A|---5-6-8-----------------------|
# E|-8-----------------------------|
 
#   C#/D♭
# e|--------------------------6-8-9-|
# B|----------------------7-9-------|
# G|----------------6-8-9-----------|
# D|---------6-8-10-----------------|
# A|---6-7-9------------------------|
# E|-9------------------------------|
 
#   D
# e|--------------------------7-9-10-|
# B|-------------------6-8-10--------|
# G|-------------6-7-9---------------|
# D|-------5-7-9---------------------|
# A|-5-7-8---------------------------|
# E|---------------------------------|
 
#   D#/E♭
# e|----------------------------8-10-11-|
# B|---------------------7-9-11---------|
# G|--------------7-8-10----------------|
# D|-------6-8-10-----------------------|
# A|-6-8-9------------------------------|
# E|------------------------------------|
 
#   E
# e|------------------------------9-11-12-|
# B|----------------------8-10-12---------|
# G|---------------8-9-11-----------------|
# D|--------7-9-11------------------------|
# A|-7-9-10-------------------------------|
# E|--------------------------------------|
 
#   F
# e|-----------------------------1-|
# B|-----------------------1-3-5---|
# G|-------------------1-3---------|
# D|-------------2-3-5-------------|
# A|-------1-3-5-------------------|
# E|-1-3-4-------------------------|
 
#   F#/G♭
# e|-----------------------------2-|
# B|-----------------------2-4-6---|
# G|-------------------2-4---------|
# D|-------------3-4-6-------------|
# A|-------2-4-6-------------------|
# E|-2-4-5-------------------------|
 
#   G
# e|-----------------------------3-|
# B|-----------------------3-5-7---|
# G|-------------------3-5---------|
# D|-------------4-5-7-------------|
# A|-------3-5-7-------------------|
# E|-3-5-6-------------------------|
 
#   G#/A♭
# e|-----------------------------4-|
# B|-----------------------4-6-8---|
# G|-------------------4-6---------|
# D|-------------5-6-8-------------|
# A|-------4-6-8-------------------|
# E|-4-6-7-------------------------|
 
#   A
# e|-----------------------------5-|
# B|-----------------------5-7-9---|
# G|-------------------5-7---------|
# D|-------------6-7-9-------------|
# A|-------5-7-9-------------------|
# E|-5-7-8-------------------------|
 
#   A#/B♭
# e|--------------------------------6-|
# B|-------------------------6-8-10---|
# G|---------------------6-8----------|
# D|--------------7-8-10--------------|
# A|-------6-8-10---------------------|
# E|-6-8-9----------------------------|
 
#   B
# e|---------------------------------7-|
# B|--------------------------7-9-11---|
# G|----------------------7-9----------|
# D|---------------8-9-11--------------|
# A|--------7-9-11---------------------|
# E|-7-9-10----------------------------|
 

    

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

# Blues
 
#   C
# e|-------------------------------8-|
# B|--------------------------8-11---|
# G|------------------8-10-11--------|
# D|-------------8-10----------------|
# A|------8-9-10---------------------|
# E|-8-11----------------------------|
 
#   C#/D♭
# e|--------------------------------9-|
# B|---------------------------9-12---|
# G|-------------------9-11-12--------|
# D|--------------9-11----------------|
# A|------9-10-11---------------------|
# E|-9-12-----------------------------|
 
#   D
# e|-------------------------8-10-|
# B|------------------8-9-10------|
# G|-----------5-7-10-------------|
# D|-----5-6-7--------------------|
# A|-5-8--------------------------|
# E|------------------------------|
 
#   D#/E♭
# e|--------------------------9-11-|
# B|------------------9-10-11------|
# G|-----------6-8-11--------------|
# D|-----6-7-8---------------------|
# A|-6-9---------------------------|
# E|-------------------------------|
 
#   E
# e|----------------------------10-12-|
# B|-------------------10-11-12-------|
# G|------------7-9-12----------------|
# D|------7-8-9-----------------------|
# A|-7-10-----------------------------|
# E|----------------------------------|
 
#   F
# e|-------------------------1-|
# B|---------------------1-4---|
# G|---------------1-3-4-------|
# D|-----------1-3-------------|
# A|-----1-2-3-----------------|
# E|-1-4-----------------------|
 
#   F#/G♭
# e|-------------------------2-4-|
# B|---------------------2-5-----|
# G|---------------2-4-5---------|
# D|-----------2-4---------------|
# A|-----2-3-4-------------------|
# E|-2-5-------------------------|
 
#   G
# e|-------------------------3-|
# B|---------------------3-6---|
# G|---------------3-5-6-------|
# D|-----------3-5-------------|
# A|-----3-4-5-----------------|
# E|-3-6-----------------------|
 
#   G#/A♭
# e|-------------------------4-|
# B|---------------------4-7---|
# G|---------------4-6-7-------|
# D|-----------4-6-------------|
# A|-----4-5-6-----------------|
# E|-4-7-----------------------|
 
#   A
# e|-------------------------5-|
# B|---------------------5-8---|
# G|---------------5-7-8-------|
# D|-----------5-7-------------|
# A|-----5-6-7-----------------|
# E|-5-8-----------------------|
 
#   A#/B♭
# e|-------------------------6-|
# B|---------------------6-9---|
# G|---------------6-8-9-------|
# D|-----------6-8-------------|
# A|-----6-7-8-----------------|
# E|-6-9-----------------------|
 
#   B
# e|----------------------------7-|
# B|-----------------------7-10---|
# G|----------------7-9-10--------|
# D|------------7-9---------------|
# A|------7-8-9-------------------|
# E|-7-10-------------------------|

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

# Mixolydian
 
#   C
# e|-------------------------5-6-8-|
# B|-------------------5-6-8-------|
# G|---------------5-7-------------|
# D|---------5-7-8-----------------|
# A|---5-7-8-----------------------|
# E|-8-----------------------------|
 
#   C#/D♭
# e|-------------------------6-7-9-|
# B|-------------------6-7-9-------|
# G|---------------6-8-------------|
# D|---------6-8-9-----------------|
# A|---6-8-9-----------------------|
# E|-9-----------------------------|
 
#   D
# e|--------------------------7-8-10-|
# B|-------------------7-8-10--------|
# G|-------------5-7-9---------------|
# D|-------5-7-9---------------------|
# A|-5-7-9---------------------------|
# E|---------------------------------|
 
#   D#/E♭
# e|-----------------------------8-9-11-|
# B|----------------------8-9-11--------|
# G|---------------6-8-10---------------|
# D|--------6-8-10----------------------|
# A|-6-8-10-----------------------------|
# E|------------------------------------|
 
#   E
# e|------------------------------9-10-12-|
# B|----------------------9-10-12---------|
# G|---------------7-9-11-----------------|
# D|--------7-9-11------------------------|
# A|-7-9-11-------------------------------|
# E|--------------------------------------|
 
#   F
# e|-----------------------------1-|
# B|-----------------------1-3-4---|
# G|-------------------2-3---------|
# D|-------------1-3-5-------------|
# A|-------1-3-5-------------------|
# E|-1-3-5-------------------------|
 
#   F#/G♭
# e|-----------------------------2-|
# B|-----------------------2-4-5---|
# G|-----------------1-3-4---------|
# D|-----------1-2-4---------------|
# A|-----1-2-4---------------------|
# E|-2-4---------------------------|
 
#   G
# e|-----------------------------3-|
# B|-----------------------3-5-6---|
# G|-----------------2-4-5---------|
# D|-----------2-3-5---------------|
# A|-----2-3-5---------------------|
# E|-3-5---------------------------|
 
#   G#/A♭
# e|-----------------------------4-|
# B|-----------------------4-6-7---|
# G|-----------------3-5-6---------|
# D|-----------3-4-6---------------|
# A|-----3-4-6---------------------|
# E|-4-6---------------------------|
 
#   A
# e|-----------------------------5-|
# B|-----------------------5-7-8---|
# G|-----------------4-6-7---------|
# D|-----------4-5-7---------------|
# A|-----4-5-7---------------------|
# E|-5-7---------------------------|
 
#   A#/B♭
# e|-----------------------------6-|
# B|-----------------------6-8-9---|
# G|-----------------5-7-8---------|
# D|-----------5-6-8---------------|
# A|-----5-6-8---------------------|
# E|-6-8---------------------------|
 
#   B
# e|------------------------------7-|
# B|-----------------------7-9-10---|
# G|-----------------6-8-9----------|
# D|-----------6-7-9----------------|
# A|-----6-7-9----------------------|
# E|-7-9----------------------------|

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

#     Dorian
 
#   C
# e|--------------------------------------8-|
# B|------------------------------8-10-11---|
# G|-------------------------8-10-----------|
# D|-----------------8-10-12----------------|
# A|---------8-10-12------------------------|
# E|-8-10-11--------------------------------|
 
#   C#/D♭
# e|--------------------------------------9-|
# B|------------------------------9-11-12---|
# G|-------------------------9-11-----------|
# D|-----------------9-11-13----------------|
# A|---------9-11-13------------------------|
# E|-9-11-12--------------------------------|
 
#   D
# e|--------------------------7-8-10-|
# B|-------------------6-8-10--------|
# G|-------------5-7-9---------------|
# D|-------5-7-9---------------------|
# A|-5-7-8---------------------------|
# E|---------------------------------|
 
#   D/E♭
# e|----------------------------8-9-11-|
# B|---------------------7-9-11--------|
# G|--------------6-8-10---------------|
# D|-------6-8-10----------------------|
# A|-6-8-9-----------------------------|
# E|-----------------------------------|
 
#   E
# e|------------------------------9-10-12-|
# B|----------------------8-10-12---------|
# G|---------------7-9-11-----------------|
# D|--------7-9-11------------------------|
# A|-7-9-10-------------------------------|
# E|--------------------------------------|
 
#   F
# e|-----------------------------1-|
# B|-----------------------1-3-4---|
# G|-------------------1-3---------|
# D|-------------1-3-5-------------|
# A|-------1-3-5-------------------|
# E|-1-3-4-------------------------|
 
#   F#/G♭
# e|-----------------------------2-|
# B|-----------------------2-4-5---|
# G|-------------------2-4---------|
# D|-------------2-4-6-------------|
# A|-------2-4-6-------------------|
# E|-2-4-5-------------------------|
 
#   G
# e|-----------------------------3-|
# B|-----------------------3-5-6---|
# G|-------------------3-5---------|
# D|-------------3-5-7-------------|
# A|-------3-5-7-------------------|
# E|-3-5-6-------------------------|
 
#   G#/A♭
# e|-----------------------------4-|
# B|-----------------------4-6-7---|
# G|-------------------4-6---------|
# D|-------------4-6-8-------------|
# A|-------4-6-8-------------------|
# E|-4-6-7-------------------------|
 
#   A
# e|-----------------------------5-|
# B|-----------------------5-7-8---|
# G|-------------------5-7---------|
# D|-------------5-7-9-------------|
# A|-------5-7-9-------------------|
# E|-5-7-8-------------------------|
 
#   A#/B♭
# e|-------------------------------6-|
# B|-------------------------6-8-9---|
# G|---------------------6-8---------|
# D|--------------6-8-10-------------|
# A|-------6-8-10--------------------|
# E|-6-8-9---------------------------|
 
#   B
# e|--------------------------------7-|
# B|-------------------------7-9-10---|
# G|---------------------7-9----------|
# D|--------------7-9-11--------------|
# A|-------7-9-11---------------------|
# E|7-9-10----------------------------|
 

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

    Lydian
 
#   C
# e|-------------------------------7-8-|
# B|------------------------7-8-10-----|
# G|--------------------7-9------------|
# D|-------------7-9-10----------------|
# A|------7-9-10-----------------------|
# E|-8-10------------------------------|
 
# C#/D♭
 
# e|----------------------------------8-9-|
# B|---------------------------8-9-11-----|
# G|----------------------8-10------------|
# D|--------------8-10-11-----------------|
# A|------8-10-11-------------------------|
# E|-9-11---------------------------------|
 
#   D
# e|--------------------------7-9-10-|
# B|-------------------7-9-10--------|
# G|-------------6-7-9---------------|
# D|-------6-7-9---------------------|
# A|-5-7-9---------------------------|
# E|---------------------------------|
 
#   D#/E♭
# e|------------------------------8-10-11-|
# B|----------------------8-10-11---------|
# G|---------------7-8-10-----------------|
# D|--------7-8-10------------------------|
# A|-6-8-10-------------------------------|
# E|--------------------------------------|
 
#   E
# e|------------------------------9-11-12-|
# B|----------------------9-11-12---------|
# G|---------------8-9-11-----------------|
# D|--------8-9-11------------------------|
# A|-7-9-11-------------------------------|
# E|--------------------------------------|
 
#   F
# e|-----------------------------1-|
# B|-------------------------3-5---|
# G|-------------------2-4-5-------|
# D|-------------2-3-5-------------|
# A|-------2-3-5-------------------|
# E|-1-3-5-------------------------|
 
#   F#/G♭
# e|---------------------------1-2-|
# B|---------------------1-2-4-----|
# G|-----------------1-3-----------|
# D|-----------1-3-4---------------|
# A|-----1-3-4---------------------|
# E|-2-4---------------------------|
 
#   G
# e|---------------------------2-3-|
# B|---------------------2-3-5-----|
# G|-----------------2-4-----------|
# D|-----------2-4-5---------------|
# A|-----2-4-5---------------------|
# E|-3-5---------------------------|
 
#   G#/A♭
# e|---------------------------3-4-|
# B|---------------------3-4-6-----|
# G|-----------------3-5-----------|
# D|-----------3-5-6---------------|
# A|-----3-5-6---------------------|
# E|-4-6---------------------------|
 
#   A
# e|---------------------------4-5-|
# B|---------------------4-5-7-----|
# G|-----------------4-6-----------|
# D|-----------4-6-7---------------|
# A|-----4-6-7---------------------|
# E|-5-7---------------------------|
 
#   A#/B♭
# e|---------------------------5-6-|
# B|---------------------5-6-8-----|
# G|-----------------5-7-----------|
# D|-----------5-7-8---------------|
# A|-----5-7-8---------------------|
# E|-6-8---------------------------|
 
#   B
# e|---------------------------6-7-|
# B|---------------------6-7-9-----|
# G|-----------------6-8-----------|
# D|-----------6-8-9---------------|
# A|-----6-8-9---------------------|
# E|-7-9---------------------------|

    main_menu()    

main_menu()



