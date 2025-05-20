import os
from _musicQuizSongGenerator import Generator

gen: Generator = Generator(os.path.dirname(os.path.realpath(__file__))+"/Quiz Songs.db")

packId = gen.CreatePack("Dad Songs", "MWitham")

gen.InsertSong("Live Forever", ["Oasis"], "Definitely Maybe", """Oh yeah
Maybe I don't really wanna know
How your garden grows
'Cause I just wanna fly
Lately, did you ever feel the pain
In the morning rain
As it soaks you to the bone?
Maybe I just wanna fly
Wanna live, I don't wanna die
Maybe I just wanna breathe
Maybe I just don't believe
Maybe you're the same as me
We see things they'll never see
You and I are gonna live forever
I said maybe I don't really wanna know
How your garden grows
'Cause I just wanna fly
Lately, did you ever feel the pain
In the morning rain
As it soaks you to the bone?
Maybe I will never be
All the things that I wanna be
Now is not the time to cry
Now's the time to find out why
I think you're the same as me
We see things they'll never see
You and I are gonna live forever
Maybe I don't really wanna know
How your garden grows
'Cause I just wanna fly
Lately, did you ever feel the pain
In the morning rain
As it soaks you to the bone?
Maybe I just wanna fly
Wanna live, I don't wanna die
Maybe I just wanna breathe
Maybe I just don't believe
Maybe you're the same as me
We see things they'll never see
You and I are gonna live forever
Gonna live forever
Gonna live forever
We're gonna live forever
Gonna live forever
Gonna live forever
Gonna live forever""", [packId, 15, 2]) # garden



gen.InsertSong("Stop Crying Your Heart Out", ["Oasis"], "Heathen Chemistry", """Hold up
Hold on
Don't be scared
You'll never change what's been and gone
May your smile (may your smile)
Shine on (shine on)
Don't be scared (don't be scared)
Your destiny may keep you warm
'Cause all of the stars
Are fading away
Just try not to worry
You'll see them someday
Take what you need
And be on your way
And stop crying your heart out
Get up (get up)
Come on (come on)
Why you scared? (I'm not scared)
You'll never change what's been and gone
'Cause all of the stars
Are fading away
Just try not to worry
You'll see them someday
Take what you need
And be on your way
And stop crying your heart out
'Cause all of the stars
Are fading away
Just try not to worry
You'll see them someday
Just take what you need
And be on your way
And stop crying your heart out
We're all of us stars
We're fading away
Just try not to worry
You'll see us someday
Just take what you need
And be on your way
And stop crying your heart out
Stop crying your heart out
Stop crying your heart out
Stop crying your heart out""", [packId, 11, 3]) # someday


gen.InsertSong("Maybe Tomorrow", ["Stereophonics"], "You Gotta Go There To Come Back", """I've been down and I'm wondering why
These little black clouds keep walking around
With me
With me
It wastes time and I'd rather be high
Think I'll walk me outside and buy a rainbow smile
But be free
They're all free
So maybe tomorrow
I'll find my way home
So maybe tomorrow
I'll find my way home
I look around at a beautiful life
I've been the upper side of down
Been the inside of out
But we breathe
We breathe
I wanna breeze and an open mind
I wanna swim in the ocean
Wanna take my time for me
All me
So maybe tomorrow
I'll find my way home
So maybe tomorrow
I'll find my way home
So maybe tomorrow
I'll find my way home
So maybe tomorrow
I'll find my way home
So maybe tomorrow
I'll find my way home
So maybe tomorrow
I'll find my way home""", [packId, 9, 4]) # home


gen.InsertSong("With Or Without You", ["U2"], "The Joshua Tree", """See the stone set in your eyes
See the thorn twist in your side
I'll wait for you
Sleight of hand and twist of fate
On a bed of nails she makes me wait
And I'll wait without you
With or without you
With or without you
Through the storm we reach the shore
You give it all but I want more
And I'm waiting for you
With or without you
With or without you
I can't live
With or without you
And you give yourself away
And you give yourself away
And you give, and you give
And you give yourself away
My hands are tied
My body bruised, she got me with
Nothing to win and nothing left to lose
And you give yourself away
And you give yourself away
And you give, and you give
And you give yourself away
With or without you
With or without you, oh-oh
I can't live
With or without you
Oh, oh, oh
Oh, oh, oh
Oh, oh, oh
Oh, oh
With or without you
With or without you, oh
I can't live, with or without you
With or without you""", [packId, 8, 2]) # storm



gen.InsertSong("Naive", ["The Kooks"], "Inside In / Inside Out", """I'm not saying it was your fault
Although you could have done more
Oh, you're so naïve, yet so
How could this be done
By such a smiling sweetheart?
Oh, and your sweet and pretty face
In such an ugly way
Something so beautiful
Oh, that every time I look inside
I know she knows that I'm not fond of asking
True or false, it may be
Well, she's still out to get me
And I know she knows that I'm not fond of asking
True or false, it may be
She's still out to get me
I may say it was your fault
Because I know you could have done more
Oh, you're so naïve, yet so
How could this be done
By such a smiling sweetheart?
Oh, and your sweet and pretty face
In such an ugly way something so beautiful
Oh, that every time I look inside
I know she knows that I'm not fond of asking
True or false, it may be
Well, she's still out to get me
And I know she knows that I'm not fond of asking
True or false, it may be
She's still out to get me
Ooh
So how could this be done
By such a smiling sweetheart?
Oh, you're so naïve, yet so
It's such an ugly thing
For someone so beautiful
I'll die every time you're on his side
I know she knows that I'm not fond of asking
True or false, it may be 
Well, she's still out to get me
And I know she knows that I'm not fond of asking
True or false, it may be 
She's still out to get me
Just don't let me down
So just don't let me down
Hold on to your kite
Just don't let me down
Just don't let me down
Hold on to your kite
Just don't let me down, oh
Just don't let me down
Hold on to this kite
Just don't let me down
Just don't let me down""", [packId, 9, 9]) # asking


gen.InsertSong("Can't Stop", ["Red Hot Chili Peppers"], "By The Way", """Can't stop, addicted to the shindig
Chop Top, he says I'm gonna win big
Choose not a life of imitation
Distant cousin to the reservation
Defunkt, the pistol that you pay for
This punk, the feelin' that you stay for
In time I want to be your best friend
East side lovers living on the West End
Knocked out, but, boy, you better come to (oh, oh-oh)
Don't die, you know the truth as some do (oh-oh)
Go write your message on the pavement (oh-oh)
Burn so bright, I wonder what the wave meant
White heat is screamin' in the jungle (oh, oh-oh)
Complete the motion if you stumble (oh-oh)
Go ask the dust for any answers (oh-oh)
Come back strong with fifty belly dancers
The world I love, the tears I drop
To be part of the wave, can't stop
Ever wonder if it's all for you?
The world I love, the trains I hop
To be part of the wave, can't stop
Come and tell me when it's time to
Sweetheart is bleeding in the snow cone
So smart, she's leading me to ozone
Music, the great communicator
Use two sticks to make it in the nature
I'll get you into penetration
The gender of a generation
The birth of every other nation
Worth your weight, the gold of meditation
This chapter's gonna be a close one (oh, oh-oh)
Smoke rings, I know your gonna blow one (oh-oh)
All on a spaceship, persevering (oh-oh)
Use my hands for everything but steering
Can't stop the spirits when they need you (oh, oh-oh)
Mop tops are happy when they feed you (oh-oh)
J. Butterfly is in the treetop (oh-oh)
Birds that blow the meaning into bebop
The world I love, the tears I drop
To be part of the wave, can't stop
Ever wonder if it's all for you?
The world I love, the trains I hop
To be part of the wave, can't stop
Come and tell me when it's time to
Wait a minute I'm passin' out, win or lose
Just like you
Far more shockin' than anything I ever knew
How 'bout you?
Ten more reasons why I need somebody new
Just like you
Far more shockin' than anything I ever knew
Right on cue
Can't stop, addicted to the shindig
Chop Top, he says I'm gonna win big
Choose not a life of imitation
Distant cousin to the reservation
Defunkt the pistol that you pay for (oh, oh-oh)
This punk, the feelin' that you stay for (oh-oh)
In time I want to be your best friend (oh-oh)
East side lovers living on the West End
Knocked out, but, boy, you better come to (oh, oh-oh)
Don't die, you know the truth as some do (oh-oh)
Go write your message on the pavement (oh-oh)
Burn so bright, I wonder what the wave meant
Kick start the golden generator
Sweet talk but don't intimidate her
Can't stop the gods from engineering
Feel no need for any interfering
Your image in the dictionary
This life is more than ordinary
Can I get two, maybe even three of these?
Comin' from space to teach you of the Pleiades
Can't stop the spirits when they need you
This life is more than just a read-through""", [packId, 17, 5]) # wave


gen.InsertSong("The Pretender", ["Foo Fighters"], "Echoes, Silence, Patience & Grace", """Keep you in the dark
You know they all pretend
Keep you in the dark
And so it all began
Send in your skeletons
Sing as their bones go marching in again
They need you buried deep
The secrets that you keep are ever ready
Are you ready?
I'm finished making sense
Done pleading ignorance
That old defense
Spinning infinity, boy
The wheel is spinning me
It's never-ending, never-ending
Same old story
What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender
What if I say I will never surrender?
What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender
What if I say that I never surrender?
In time, or so I'm told,
I'm just another soul for sale, oh well
The page is out of print
We are not permanent
We're temporary, temporary
Same old story
What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender
What if I say I will never surrender?
What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender
What if I say I will never surrender?
I'm the voice inside your head you refuse to hear
I'm the face that you have to face mirrorin' your stare
I'm what's left; I'm what's right; I'm the enemy
I'm the hand that'll take you down and bring you to your knees
So, who are you?
Yeah, who are you?
Yeah, who are you?
Yeah, who are you?
Keep you in the dark
You know they all pretend
What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender
What if I say I will never surrender?
What if I say I'm not like the others?
What if I say I'm not just another one of your plays?
You're the pretender
What if I say that I'll never surrender?
What if I say I'm not like the others?
(Keep you in the dark)
What if I say I'm not just another one of your plays?
(You know they all)
You're the pretender
(Pretend)
What if I say I will never surrender?
What if I say I'm not like the others?
(Keep you in the dark)
What if I say I'm not just another one of your plays?
(You know they all)
You're the pretender
(Pretend)
What if I say I will never surrender?
So, who are you?
Yeah, who are you?
Yeah, who are you?""", [packId, 17, 11]) # plays

gen.LinkSongToPack(packId, gen.GetSongId("My Number", "Foals"), 15, 2) # wolf