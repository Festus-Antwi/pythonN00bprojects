no_time_to_die = "No Time To Die Lyrics\n\
[Verse 1]\n\
I should have known\n\
I'd leave alone\n\
Just goes to show\
That the blood you bleed is just the blood you owe\
We were a pair\n\
But I saw you there\n\
Too much to bear\n\
You were my life, but life is far away from fair\n\
Was I stupid to love you?\
Was I reckless to help?\n\
Was it obvious to everybody else?\n\
\n\
[Chorus]\n\
That I'd fallen for a lie\n\
You were never on my side\n\
Fool me once, fool me twice\n\
Are you death or paradise?\n\
Now you'll never see me cry\n\
There's just no time to die...\n\
"

happier_than_ever = "Happier Than Ever Lyrics\n\
[Chorus]\n\
When I'm away from you\n\
I'm happier than ever\n\
Wish I could explain it better\n\
I wish it wasn't true\n\
\n\
[Verse 1]\n\
Give me a day or two to think of something clever\n\
To write myself a letter\n\
To tell me what to do, mm-mm\n\
Do you read my interviews?\n\
Or do you skip my avenue?\n\
When you said you were passin' through\n\
Was I even on your way?\n\
I knew when I asked you to (When I asked you to)\n\
Be cool about what I was tellin' you\n\
You'd do the opposite of what you said you'd do (What you said you'd do)\n\
And I'd end up more afraid\n\
Don't say it isn't fair\n\
You clearly werеn't aware that you made me misеrable\n\
So if you really wanna know\n\
\n\
\n\
[Chorus]\n\
When I'm away from you (When I'm away from you)\n\
I'm happier than ever (Happier than ever)\n\
Wish I could explain it better (Wish I could explain it better)\n\
I wish it wasn't true, mm-mm...\n\
"


bad_guy = "Bad Guy Lyrics\n\
[Verse 1]\n\
White shirt now red, my bloody nose\n\
Sleepin', you're on your tippy toes\n\
Creepin' around like no one knows\n\
Think you're so criminal\n\
Bruises on both my knees for you\n\
Don't say thank you or please\n\
I do what I want when I'm wanting to\n\
My soul? So cynical\n\
\n\
[Chorus]\n\
So you're a tough guy\n\
Like it really rough guy\n\
Just can't get enough guy\n\
Chest always so puffed guy\n\
I'm that bad type\n\
Make your mama sad type\n\
Make your girlfriend mad tight\n\
Might seduce your dad type\n\
I'm the bad guy\n\
Duh...\
"

def select_song():
    try:
        song_choice = int(input("Use the numbers to select song lyrics.\n1. No Time To Die Lyrics\n2. Happier Than Ever Lyrics\n3. Bad Guy Lyrics\n-->"))
        if song_choice == 1:
            print(song_list[0])
        elif song_choice == 2:
            print(song_list[1])
        elif song_choice == 3:
            print(song_list[2])
        else:
            print("You entered an invalid choice, try again.")
    
    except ValueError:
        print("Skrrr...something went wrong on your side. Restart program.")


song_list = [no_time_to_die, happier_than_ever, bad_guy, ]