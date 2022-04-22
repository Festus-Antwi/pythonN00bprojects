from artists import drake, billie_eilish, childish_gambino


def select_artist(number):
    if number == 1:
        drake.select_song()
    elif number == 2:
        billie_eilish.select_song()
    elif number == 3:
        childish_gambino.select_song()
    

print("Welcome to the lyrics generator...")
try:
    user_choice = int(input( "Use numbers to select artist. \n[1]. Drake\n[2]. Billie Eilish\n[3]. Childish Gambino\n--> "))

    if user_choice == 1:
        select_artist(1)
    elif user_choice == 2:
        select_artist(2)
    elif user_choice == 3:
        select_artist(3)
    else:
        print("You made an invalid choice, try agian.")
except ValueError:
    print("Skrrr...something went wrong on your side. Restart program.")