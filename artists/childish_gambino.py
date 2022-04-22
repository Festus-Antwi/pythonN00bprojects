feels_like_summer = "Feels Like Summer Lyrics\n\
[Chorus]\n\
You can feel it in the streets\n\
On a day like this, the heat\n\
It feel like summer\n\
I feel like summer\n\
I feel like summer\n\
You can feel it in the streets\n\
On a day like this, the heat\n\
I feel like summer\n\
She feel like summer\n\
This feel like summer\n\
I feel like summer\n\
\n\
[Verse 1]\n\
Seven billion souls that move around the sun\n\
Rolling faster, fast and not a chance to slow down\n\
Slow down\n\
Men who made machines that want what they decide\n\
Parents tryna tell their children please slow down\n\
Slow down...\
"




redbone = "Redbone Lyrics\n\
    [Verse 1]\n\
    Daylight\n\
    I wake up feeling like you won't play right\n\
    I used to know, but now that shit don't feel right\n\
    It made me put away my pride\n\
    So long\n\
    You made a nigga wait for some, so long\n\
    You make it hard for boy like that to go on\n\
    I'm wishing I could make this mine, oh\n\
    \n\
    [Pre-Chorus]\n\
    If you want it, yeah\n\
    You can have it, oh, oh, oh\n\
    If you need it, ooh\n\
    We can make it, oh\n\
    If you want it\n\
    You can have it\n\
    \n\
    [Chorus]\n\
    But stay woke\n\
    Niggas creepin'\n\
    They gon' find you\n\
    Gon' catch you sleepin', ooh\n\
    Now stay woke\n\
    Niggas creepin'\n\
    Now don't you close your eyes..."

def select_song():
    try:
        song_choice = int(input("Use the numbers to select song lyrics.\n1. Feels Like Summer Lyrics\n2. Redbone Lyrics\n-->"))
        if song_choice == 1:
            print(song_list[0])
        elif song_choice == 2:
            print(song_list[1])
        else:
            print("You entered an invalid choice, try again.")
    
    except ValueError:
        print("Skrrr...something went wrong on your side. Restart program.")


song_list = [feels_like_summer, redbone]