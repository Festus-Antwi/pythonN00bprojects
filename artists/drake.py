gods_plan ="God’s Plan Lyrics\n\
[Intro]\n\
And they wishin' and wishin'\n\
And wishin' and wishin', they wishin' on me\n\
Yeah\n\
\n\
[Verse 1]\n\
I been movin' calm, don't start no trouble with me\n\
Tryna keep it peaceful is a struggle for me\n\
Don't pull up at 6 AM to cuddle with me\n\
You know how I like it when you lovin' on me\n\
I don't wanna die for them to miss me\n\
Yes, I see the things that they wishin' on me\n\
Hope I got some brothers that outlive me\n\
They gon' tell the story, shit was different with me\n\
\n\
[Chorus]\n\
God's plan, God's plan\n\
I hold back, sometimes I won't, yeah\n\
I feel good, sometimes I don't (Ayy, don't)\n\
I finessed down Weston Road (Ayy, 'nessed)\n\
Might go down a G.O.D. (Yeah, wait)\n\
I go hard on Southside G (Yeah, wait)\n\
I make sure that north-side eat\n\
And still..."




hotline = "Hotline Bling Lyrics\n\
[Intro]\n\
You used to call me on my\n\
You used to, you used to\n\
Yeah\n\
\n\
[Chorus]\n\
You used to call me on my cell phone\n\
Late-night when you need my love\n\
Call me on my cell phone\n\
Late-night when you need my love\n\
And I know when that hotline bling\n\
That can only mean one thing\n\
I know when that hotline bling\n\
That can only mean one thing\n\
\n\
[Verse 1]\n\
Ever since I left the city, you\n\
Got a reputation for yourself now\n\
Everybody knows and I feel left out\n\
Girl, you got me down, you got me stressed out\n\
'Cause ever since I left the city, you\n\
Started wearing less and goin' out more\n\
Glasses of champagne out on the dance floor\n\
Hangin' with some girls I've never seen before\n\
\n\
\n\
[Chorus]\n\
You used to call me on my cell phone\n\
Late-night when you need my love\n\
Call me on my cell phone\n\
Late-night when you need my love\n\
I know when that hotline bling\n\
That can only mean one thing\n\
I know when that hotline bling\n\
That can only mean one thing...\
"




in_my_feelings = "In My Feelings Lyrics\n\
[Intro: Drake]\n\
Trap, TrapMoneyBenny\n\
This shit got me in my feelings\n\
Gotta be real with it, yeah\n\
\n\
[Chorus: Drake]\n\
Kiki, do you love me? Are you riding?\n\
Say you'll never ever leave from beside me\n\
'Cause I want ya, and I need ya\n\
And I'm down for you always\n\
KB, do you love me? Are you riding?\n\
Say you'll never ever leave from beside me\n\
'Cause I want ya, and I need ya\n\
And I'm down for you always\n\
\n\
[Verse: Drake]\n\
Look, the new me is really still the real me\n\
I swear you gotta feel me before they try and kill me\n\
They gotta make some choices, they runnin' out of options\n\
'Cause I've been goin' off and they don't know when it's stoppin'\n\
And when you get to toppin', I see that you've been learnin'\n\
And when I take you shoppin', you spend it like you earned it\n\
And when you popped off on your ex he deserved it\n\
I thought you were the one from the jump, that confirmed it\n\
TrapMoneyBenny, ayy\n\
I buy you Champagne but you love some Henny\n\
From the block like you Jenny\n\
I know you special, girl, 'cause I know too many\n\
\n\
\n\
[Chorus: Drake]\n\
'Resha, do you love me? Are you riding?\n\
Say you'll never ever leave from beside me\n\
'Cause I want ya, and I need ya\n\
And I'm down for you always\n\
JT, do you love me? Are you riding?\n\
Say you'll never ever leave from beside me\n\
'Cause I want ya, and I need ya\n\
And I'm down for you always..."




know_yourself = "Know Yourself Lyrics\n\
[Part 1]\n\
\n\
[Intro]\
Hol' it yute, hol' it, hol' it, hol' it, hol' it, hol' it\n\
No sleepin' in the streets!\n\
Shaky warrior\n\
Yeah, this that Oliver, 40, Niko shit man\n\
15 Fort York shit, y'know?\n\
Boi-1da, what's poppin'?\n\
Yeah, yeah\n\
\n\
[Verse 1]\n\
Runnin' through the 6 with my woes\n\
Countin' money, you know how it goes\n\
Pray the real live forever, man\n\
Pray the fakes get exposed\n\
I want that Ferrari, then I swerve\n\
I want that Bugatti, just to hurt\n\
I ain't rockin' my jewelry, that's on purpose\n\
Niggas want my spot and don't deserve it\n\
I don't like how serious they take themselves\n\
I've always been me, I guess I know myself\n\
Shakiness, man, I don't have no time for that\n\
My city too turned up, I'll take the fine for that\n\
This been where you find me at\n\
That's been where you find me at\n\
I know a nigga named Johnny Bling\n\
He put me on to the finer things\
Had a job sellin' Girbaud jeans\n\
I had a yellow TechnoMarine\n\
Then Kanye dropped, it was polos and backpacks\n\
Man, that was when Ethan was pushin' a Subaru hatchback\n\
Man, I'm talkin' way before hashtags\n\
I was runnin' through the 6 with my woes\n\
(Yeah!)\n\
\n\
\n\
\n\
[Part 2]\n\
\n\
[Beat Switch]\n\
\n\
[Chorus]\n\
I was runnin' through the 6 with my woes\n\
You know how that shit go\n\
You know how that shit go\n\
You know how that shit go\n\
Runnin' through the 6 with my woes\n\
You know how that shit go\n\
You know how that shit go\n\
You know how that shit go\n\
Don't fuck with them niggas, they too irrational, woah..."


def select_song():
    try:
        song_choice = int(input("Use the numbers to select song lyrics.\n1. God’s Plan Lyrics\n2. Hotline Bling Lyrics\n3. In My Feelings Lyrics\n4. Know Yourself Lyrics\n-->"))
        if song_choice == 1:
            print(song_list[0])
        elif song_choice == 2:
            print(song_list[1])
        elif song_choice == 3:
            print(song_list[2])
        elif song_choice == 4:
            print(song_list[3])
        else:
            print("You entered an invalid choice, try again.")
    
    except ValueError:
        print("Skrrr...something went wrong on your side. Restart program.")
    

song_list = [gods_plan, hotline, in_my_feelings, know_yourself]


