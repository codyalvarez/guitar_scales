def play_again():
    print("\nDo you want to play again (y or n)")

    # convert player input
    answer = input(">").lower()

    if "y" in answer:
        start()
    elif "n" in answer:
        print("So long traveler!")
        exit
    else:
        exit

def game_over(reason):
    # print the "reason" in a new line (\n)
    print("\n" + reason)
    print("Game Over!")
    # ask player to play again
    play_again()


def sun_death():
    print("\nIt feels like its been hours...")
    print("Your starting to feel dizzy, falling in and out of consciosness.")
    print("Its probably a good idea to stay hydrated.")
    print("1. ) Its probably not the best but you need fluids. - *proceed to drink ocean water* ")
    print("2. ) Find the strength to stand up and walk towards the jungle.")
    print("\nChoose option '1' or '2'")

    # get input
    answer = input(">").lower()

    if answer == "1":
        # the player died
        game_over("You drank ocean water and immediately died of either heat stroke, deydration, but most likley a mixture of the two.")
    elif answer == "2":
        # jungle_line
        jungle_line()
    else:
        # call game_over() function with the "reason" arg
        game_over("Havent you ever watched bear grillz?")

def jungle_line():
    print("\nAfter what seems like an eternity, you finally made it to the jungle.")
    print("Standing in front of you: a vast tropical forest, thick with trees, plants, wild animals, nasty insects, and scally reptiles.")
    print("You have no phone, no maps, nothing to eat, no water, nor shelter, and to make things worse, the sun is going down.")
    print("1. Go into the jungle in search for food and water.")
    print("2. Stay put, now that you have the shade from the jungle, you decide to make a small shelter for the night.)")
    print("\nChoose option '1' or '2' ")

    # get user input
    answer = input(">").lower()

    if answer == "1":
        game_over("An hour into exploring the jungle it gets dark, you find your self lost, and without shelter have zero defense against the wild. \nYou end up getting attacked and eaten by a jaguar.")
    elif answer == "2":
        shelter()
    else:
        # call game_over() function with the "reason" arg
        game_over("Havent you ever watched bear grillz?")

def shelter():
    print("\nWith only an hour or so before the sun goes down, you dont have much time to build a shelter, plus your tired from the walk from the beach.")
    print("1. ) Work diligently, forge sturdy pieces of scrap wood from branches near by and build a solid plat form bed, to keep you off the ground. Use large evergreen leaves from near by palm trees to soften the bed up.")
    print("2. ) You've been walking all day, you need rest more then anything.  Lie down, and go to sleep.")
    print("\nChoose option '1' or '2' ")
    
    # get user input
    answer = input(">").lower()

    if answer == "1":
        day_1()
    elif answer == "2":
        # call game_over() function with the "reason" arg
        game_over("Sleeping on the ground has its downfalls. An amazonian giant centipede crawled through the sand and ate you.")

def day_1():
    print("\nDAY TWO")
    print("\nYou wake up feeling well rested but sore, and very thirsty. You decide to venture into the jungle in search of supplies, food, and most importanly, water.")
    print("1. ) While walking in the jungle you notice some large lookin fruits hanging below the tree tops, close to some what appears to be, climbable vines... You choose to climb.) ")
    print("2. ) The first sign of life, you stand very still as you notice a deer appear from under the canopy.  You decide to follow it.")
    print("\nChoose option '1' or '2' ")

    # convert the players input() to lower_case
    answer = input(">").lower()

    if answer == "1":
        fruit()
    elif answer == "2":
        deer()
    else:
        game_over("You must have eaten some bad berries or something...")

def fruit():
    print("\nYou start climbing the vines. About halfway up you find one peice of fruit within arms reach, but if you climb a little higher, there are a 3 or more of the same fruit.")
    print("1. Confident in your climbing abilities and trust in the vine, you decide to climb higher to the next bundle of fruits.) ")
    print("2. Fear of heights keeps you content with just one piece of fruit.)")
    print("\nChoose option '1' or '2' ")

    # convert the players input() to lower_case
    answer = input(">").lower()

    if answer == "1":
        game_over("Just as you climb to the top, and reach for the bundle, the vine snaps, and you fall to your death.")
    elif answer == "2":
        game_over("You shimmy your way down. Take a bite of the fruit and instantly your mouth goes numb, then your throat drys up, and before you know it, you die. ")
    else:
        game_over("You must have eaten some bad berries or something...")


def deer():
    print("\nStaying low, and keeping a fair distance, you follow the deer for about an hour, when to your suprise leads you to a pond.")
    print("1. ) Your so thirsty, you walk over to the pond, dip your hands in, and drink the water.")
    print("2. ) The pond appears to be stagnat, your unsure if the water is safe to drink. You decide to move on, without drink the pond water.")
    print("\nChoose option '1' or '2' ")

    # convert the players input() to lower_case
    answer = input(">").lower()

    if answer == "1":
        game_over("Without first filtering the water, you drink the bacteria filled pond water and die slowly of leptospirosis.")
    elif answer == "2":
        plane_crash()
    else:
        game_over("Its only been two days, you cant be this confused...")


def plane_crash():
    print("\nWhile rummaging through the thick forest, a hole in the tree tops allows a beam of sun light to peirce through and thats when you fix your focus on a wrecked aircraft.")
    print("1. Eager for supplies, you climb up into the downed aircraft and begin searching the bay for any food or water.")
    print("2. You notice a burning smell coming from the tail of the aircraft. You approach cautiously only to find the burner on the rear jet is still lit with flame.")
    print("\nChoose option '1' or '2' ")

    answer = input(">").lower()

    if answer == "1":
        game_over("They say patience is a virue... The rear jet was still glowing hot and with the fuel lines leaking, the minute you stepped into the aircraft in changed the pressure slightly causing the rear jets to explode in flames.")
    elif answer == "2":
        avoid_boom()
    else:
        game_over("Even the monkeys know thats not an option...")


def avoid_boom():
    print("\nThank god you didnt climb into the aircraft. The rear fuel line was leaking and caught fire from the still burning jet resulting in an explosion. Although you were dangerously injured, a piece of shrapnel found its way into the side of your ribs.")
    print("1. Leave the peice of metal inside you until you have the proper medical supplies to clean and bandage the wound.")
    print("1. Go rambo, bite down on stick and pull the shrapnel out now, you can barely walk with it still in.")
    print("\nChoose option '1', or '2' ")

    answer = input(">").lower()

    if answer == "1":
        find_supplies()
    elif answer == "2":
        game_over("You obviously didnt watch enough grays anatomy.. Pulling out the metal badly damaged the lining of your stomach. You bleed out in a matter of minutes.")
    else:
        game_over("Where is your mind...")

def find_supplies():
    print("\nAlthough the explosion blew the plane to bits, there are some salvageable items near by, you just have to look around.")
    print("\nYou notice a badly burned airline trolley to the right of you.")
    print("\nYou also notice a tactical looking backpack to your left.")
    print("1. )See if you can unlock the airline trolley compartments.")
    print("2. )Open up the tactical backpack.") 

    answer = input(">").lower()

    if answer == "1":
        airline_trolley()
    elif answer == "2":
        tactical_backpack()
    else:
        game_over("You must have lost alot of blood!")

def airline_trolley():
    print("\nYou manage to open up one of the drawers to find a stock of 12 water bottles, and 10 bags of chips. The second drawer is full of coffee filters and cups. While the third is empty.")
    print("\nYou quickly crack one of the waters and drink. Thats 11 left.")
    print("\nThe peice of shrapnel sticking into your stumach is starting to bleed again... You need medical attention quickly.")
    print("1. Take a break, drink another bottle of water, and open up a bag of chips.  You need to refuel.")
    print("2. Use your shirt to gather the items. And make your way back to the shelter.")

    answer = input(">").lower()

    if answer == "1" or "2":
        game_over("You probably should have checked the backpack for any medical supplies, you bled out on your walk back to the shelter.")
    else:
        game_over("I remember my first bag of lays potato chips.")

def tactical_backpack():
    print("\nThe backpack must have belonged too an emergancy personel. Inside you find a medic box, 5 waters, and 2 rations of food, along with some rope.")
    print("1. ) Take out the medic box, you need to pull that shrapnel out now.")
    print("2. ) Open up one of the waters, refuel, back everything back in the bag and make your way back to the shelter, the sun is going down.")

    answer = input(">").lower()

    if answer == "1":
        medic()
    elif answer == "2":
        game_over("You should have taken care of your wound, you bled out on your walk back to the shelter")
    else:
        game_over("You must have lost alot of blood!")

def medic():
    print("")

def start():
    print("\nYou wake up on a stranded Island.")
    print("You can see where the beach ends, and the jungle begins.")
    print("1. ) Stay put, someone will rescue you soon.")
    print("2. ) Make your way to the jungle.")
    print("\nChoose option '1' or '2' ")

    # convert the players input() to lower_case
    answer = input(">").lower()

    if "1" in answer:
        sun_death()
    elif "2" in answer:
        jungle_line()
    else:
        # call game_over() function with the "reason" argument
        game_over("You survival skills need some work.")
        
# start game
start()

# minor changes made 
