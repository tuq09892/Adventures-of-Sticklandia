define a = Character('Artist')
define b = Character('Brute')
define d = Character('Dragon')
define g = Character('Gnome')
define k = Character('King')
define m = Character('Me')
define p = Character('Princess')
define s = Character('Server')
define t = Character('Troll')
define u = Character('Unknown')
define w = Character('Wizard')

label start:
    scene black
menu:
    "Wake up.":
        jump awake
    "Don't.":
        "I'm sorry, what?"
        "Why wouldn't you choose to wake up?"
        "The game literally has \"Adventure\" in the name."
        "How are you supposed to adventure if you're asleep."
        "You must've misclicked. Try again."

menu:
    "Wake up.":
        jump awake
    "Don't.":
        "So you meant to do this?"
        "Why would you choose to not play the game."
        "Oh, I know what's happening."
        "You're a speedrunner trying to get the world record time for this game."
        "You're probably like, \"What faster way to end the game than to not play it in the first place?\""
        "Wait..."
        "Do people even speedrun visual novels?"
        "Let me google it."
        "Huh."
        "It says the speedrun.com doesn't allow visual novel submissions."
        "Well then, what are you doing here?"
        "Oh, I know."
        "You must've completed all of the other endings and then realized that the total didn't add up to what it said on the title screen."
        "So..."
        "Did you complete all the other endings?"

menu:
    "Yes.":
        "I knew it."
        "Oh, you must have so many questions about the thoroughly crafted lore of this game."
        "I would give a spoiler warning, but you've already played the rest of the game, so there's nothing to spoil."
        "Go ahead. Ask me anything."
        "Or more accurately..."
        "Ask me one these pre-written questions."
        jump questions
    "No.":
        "Really?"
        "I can't think of any other reason why you would choose not to wake up on the first screen-"
        "Oh no."
        "Don't tell me that you chose to not wake up because the very first choice I gave you was so obvious that you purposefully picked wrong option to spite me."
        "I see how it is."
        "I suppose I can't blame you though."
        "It's my own fault for giving you such a non-consequential choice."
        "That's why you're playing a \"choose your own adventure\" game, right?"
        "You want consequences."
        "Okay."
        "Let me get back into my narrator voice."
        "The king must've noticed that you missed your morning assignment because someone came to knock on the door of your house."
        "After several minutes without a response, he busted your door open."
        "He ran to your bedroom to check on you, only to discover.."
        "You had passed in your sleep."
        "How did I do?"
        "Was that a satisfying ending?"

menu:
    "Yes.":
        jump eternal_sleep_ending
    "No.":
        jump eternal_sleep_ending

label questions:
menu:
    "Is this canon?":
        "Is what canon?"
        "Oh, these conversations between you and me?"
        "Yes. They're hallucinations that the knight has before he dies."
        "Speaking of him, you're probably wondering if he has an actual name. Or if any of the characters have names for that matter."
        "The answer is no."
        jump questions
    "What's up with Modern Times?":
        "It's a play on the restaurant Medieval Times."
        "I don't know if that's you meant by the question, but it's not that deep."
        jump questions
    "What's the deal with the artist?":
        "You want to know about the artist?"
        "There's a lot to unpack here."
        "First, there's the artist's role in this world."
        "The artist is essentially a god."
        "All of the storylines are sketches in their notebook."
        "They are responsible for creating and maintaining the world, yet they have no control over its inhabitants."
        "That is why in the \"Nose Ending\", the knight can defy the artist, yet the artist can freeze the world by refusing to draw it."
        "Second, there's the identity of the artist."
        "Honestly, I intentionally left the artist character vague so that it could be anyone from me to another college student to a first grader who thinks their schoolyard crush counts as a relationship."
        jump questions
    "Who kidnapped the princess?":
        "You want to know the mastermind behind the kidnapping of the princess, huh?"
        "The obvious answer is that the wizard was behind it."
        "He's pretty clearly evil and wishes harm to the royal family."
        "But the correct answer is often the one you'd least expect."
        "The truth is that it was all a hoax."
        "The princess was dissatisfied with her life in the castle."
        "She rarely got to leave and her father never paid attention to her."
        "She hired someone to kidnap her for a change of pace."
        "Also, she hoped her dad might care more if he thought he might lose her."
        "Unfortunately, she was wrong."
        jump questions
    "I'm done.":
        jump lore_dump_ending

label awake:
    python:
        have_rose = False
        seen_wizard = False
        seen_troll = False
    m "Is it morning already?"
    "You get out of bed and approach your mirror."
    scene mirror
    "Fresh out of bed, you're already prepared to serve the kingdom of Sticklandia."
    "People find it weird that you sleep with your helmet on, but you find it efficient."
    "One less thing to put on in the morning."
    m "I wonder what adventure today has in store."
    m "I guess I'd better see the king for my assignment."
    "It was a bit early, but you figured the king would admire your timeliness."
    scene throne
    "However, when you arrive, the throne is empty. Where could the king be?"
    "Did he sleep in? Was he kidnapped? Did the pub have a discount on chicken wings?"
    "Thankfully, he arrives within a few minutes."
    show king talking
    k "KNIIIIIIIIGHT!!!!!!"
    k "How many times do I have to tell you to stop arriving early for your morning assignment?"
    k "I had to abandon my scrambled eggs, which will be cold by the time I get back to them."
    show king silent
    m "I'm sorry your highness. I was just eager to serve you."
    show king talking
    k "I know. You said the same thing yesterday."
    show king silent
    "A long silence transpires, which the king breaks with long awaited news."
    show king talking
    k "Anyways. I assume you want to know what your assignment is."
    k "One of my daughters has been kidnapped. I need you to rescue her."
    show king silent
    m "I'm so sorry to hear that, your highness. Which daughter was it?"
    show king talking
    k "I don't know. I can't be bothered to keep track of them all."
    k "All I know is that she's been taken to a dragon-guarded tower."
    k "Only an award-winning knight such as yourself has the skill in combat to slay a dragon."
    show king silent
    m "I shall rescue your daughter at once. I will not rest until she is safe at home."
    show king talking
    k "Eh. You don't need to rush. I still have plenty of daughters left."
    "You find the king to be a terrible father, but that's not for you to judge."
    "At his orders, you walk out of the palace at a leisurely pace and set forth on your journey."
    scene path
    "Still, you wonder if you should rush a bit. The princess is in danger after all."
    "Maybe the wizard could teleport you directly to the princess."

menu:
    "Take your sweet time.":
        "You continue down the extraordinarily long path to the tower."
        jump rose
    "Go to the wizard.":
        jump wizard

label rose:
    scene path
    "A few minutes into your casual stroll, you pass a patch of roses."
    m "Since I'm in no rush, maybe I should stop to smell the roses."
    
menu:
    "Smell the roses.":
        if have_rose is True:
            scene rose picked
        else:
            scene rose patch
        "You take a whiff of the rosy air surrounding you, but unfortunately come to the realization you don't have a nose."
    "Don't smell the roses.":
        "You see no point in smelling any roses, as you don't have a nose."
        jump long_way

menu:
    "Keep smelling the roses.":
        "You decide to keep standing in one spot, even though you know very well that you are receiving no benefit from it."
        "Maybe you should just walk away."
    "Continue on your journey.":
        m "Good idea. I could end up stuck here all day."
        jump long_way

menu:
    "Keep smelling the roses.":
        "It occurs to you that maybe you could properly smell the roses if you kneel down closer to them."
        "Unfortunately, you still can't smell anything because you still don't have a nose."
        "You figure you should just cut your losses and move on."
    "Continue on your journey.":
        m "Good idea. I could end up stuck here all day."
        jump long_way

menu:
    "Keep smelling the roses.":
        "You pick one of the roses to hold in front of your face."
        if have_rose is True:
            scene rose picked again
        else:
            scene rose picked
        "Still, you can't smell it."
        "It's kind of embarrassing that you thought there was anything you could do to get around the fact that you don't have a nose."
        if have_rose is True:
            jump rip_ending
        "Maybe it's not too late."
        "Maybe you can still go back."
        python:
            have_rose = True
    "Continue on your journey.":
        m "Good idea. I could end up stuck here all day."
        jump long_way

menu:
    "Keep smelling the roses.":
        jump nose_ending
    "Continue on your journey.":
        m "Good idea. I could end up stuck here all day."
        jump long_way

label long_way:
    scene path
    "You resume your saunter towards the tower."
    "Your trip is uneventful for about an hour until you come across a bridge."
    scene bridge
    "You attempt to cross, but a troll emerges from underneath to block your path."
    show troll talking
    if seen_troll is True:
        jump troll_again
    t "You shall not pass!"
    show troll silent
    m "Why not?"
    m "I need to get to a tower so I can save the princess of Sticklandia."
    show troll talking
    t "This is my bridge and if you want to use it, then you have to solve my riddle."
    show troll silent
    "You have already decided that you are in no hurry to reach the castle, so it couldn't hurt to try the riddle."
    "On the other hand, the riddle could be difficult and it's not like multiple choice answers will just magically appear in front of you."
    "Plus, if you get it wrong, it's not like you can turn back time and try again."
    "Maybe you could try going around the bridge."

menu:
    "Try to solve the riddle.":
        "You've got plenty of time on your hands, so you might as well try the riddle."
        m "Okay, troll. Hit me with your best shot."
        show troll talking
        t "You have three guesses."
        t "If you run out, you don't get to cross. Understood?"
        show troll silent
        m "Why only three guesses?"
        show troll talking
        t "You think just because I'm a troll living under a bridge that I can just stand here all day waiting for you to guess correctly."
        t "I've got better things to do."
        t "You either agree to the terms of the game or you turn around and go home."
        show troll silent
        m "Fine. Understood."
        show troll talking
        t "Good."
        t "It's more powerful than a dragon."
        t "It's more evil than the Devil."
        t "The poor have it."
        t "The rich need it."
        t "If you eat it, you will die."
        t "What is it?"
        show troll silent
    "Go around the bridge.":
        jump daredevil_ending

menu:
    "Me.":
        show troll talking
        t "Incorrect."
        t "How would it be you?"
        show troll silent
        m "I'm about to go slay a dragon."
        m "The king is rich and he needs me to save his daughter."
        m "And I'm pretty sure if I ate me, I'd die."
        show troll talking
        t "Are you evil?"
        show troll silent
        m "I guess not."
        jump me
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest
    "Disease.":
        show troll talking
        t "Incorrect."
        t "How would it be disease?"
        show troll silent
        m "The poor are super filthy and have a bunch of diseases."
        m "It can spread through food, so eating it would kill you."
        m "And do you know how many people plagues kill?"
        m "That's evil."
        show troll talking
        t "But do rich people need disease?"
        show troll silent
        m "Population control?"
        show troll talking
        t "That's a flimsy argument."
        show troll silent
        jump disease
    "Love.":
        show troll talking
        t "Incorrect."
        t "How would it be love?"
        show troll silent
        m "Love is evil because it makes you hurt like nothing else can."
        m "The rich need love because they've spent too much time focusing on money and need human connection."
        m "And love is the most powerful thing in the world."
        show troll talking
        t "That last part was pretty cheesy."
        t "Speaking of cheese, how does one eat love?"
        show troll silent
        m "Ummm..."
        show troll talking
        t "That's what I thought."
        show troll silent
        jump love

label me:
    "You should've thought that through a bit more."
    show troll talking
    t "You have two more guesses."
    show troll silent

menu:
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest
    "Disease.":
        show troll talking
        t "Incorrect."
        t "How would it be disease?"
        show troll silent
        m "The poor are super filthy and have a bunch of diseases."
        m "It can spread through food, so eating it would kill you."
        m "And do you know how many people plagues kill?"
        m "That's evil."
        show troll talking
        t "But do rich people need disease?"
        show troll silent
        m "Population control?"
        show troll talking
        t "That's a flimsy argument."
        show troll silent
        jump love_left
    "Love.":
        show troll talking
        t "Incorrect."
        t "How would it be love?"
        show troll silent
        m "Love is evil because it makes you hurt like nothing else can."
        m "The rich need love because they've spent too much time focusing on money and need human connection."
        m "And love is the most powerful thing in the world."
        show troll talking
        t "That last part was pretty cheesy."
        t "Speaking of cheese, how does one eat love?"
        show troll silent
        m "Ummm..."
        show troll talking
        t "That's what I thought."
        show troll silent
        jump disease_left

label disease:
    "You should've thought that through a bit more."
    show troll talking
    t "You have two more guesses."
    show troll silent

menu:
    "Me.":
        show troll talking
        t "Incorrect."
        t "How would it be you?"
        show troll silent
        m "I'm about to go slay a dragon."
        m "The king is rich and he needs me to save his daughter."
        m "And I'm pretty sure if I ate me, I'd die."
        show troll talking
        t "Are you evil?"
        show troll silent
        m "I guess not."
        jump love_left
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest
    "Love.":
        show troll talking
        t "Incorrect."
        t "How would it be love?"
        show troll silent
        m "Love is evil because it makes you hurt like nothing else can."
        m "The rich need love because they've spent too much time focusing on money and need human connection."
        m "And love is the most powerful thing in the world."
        show troll talking
        t "That last part was pretty cheesy."
        t "Speaking of cheese, how does one eat love?"
        show troll silent
        m "Ummm..."
        show troll talking
        t "That's what I thought."
        show troll silent
        jump me_left

label love:
    "You should've thought that through a bit more."
    show troll talking
    t "You have two more guesses."
    show troll silent

menu:
    "Me.":
        show troll talking
        t "Incorrect."
        t "How would it be you?"
        show troll silent
        m "I'm about to go slay a dragon."
        m "The king is rich and he needs me to save his daughter."
        m "And I'm pretty sure if I ate me, I'd die."
        show troll talking
        t "Are you evil?"
        show troll silent
        m "I guess not."
        jump disease_left
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest
    "Disease.":
        show troll talking
        t "Incorrect."
        t "How would it be disease?"
        show troll silent
        m "The poor are super filthy and have a bunch of diseases."
        m "It can spread through food, so eating it would kill you."
        m "And do you know how many people plagues kill?"
        m "That's evil."
        show troll talking
        t "But do rich people need disease?"
        show troll silent
        m "Population control?"
        show troll talking
        t "That's a flimsy argument."
        show troll silent
        jump me_left

label me_left:
    "You should've thought that through a bit more."
    show troll talking
    t "You have one more guess."
    show troll silent

menu:
    "Me.":
        show troll talking
        t "Incorrect."
        t "How would it be you?"
        show troll silent
        m "I'm about to go slay a dragon."
        m "The king is rich and he needs me to save his daughter."
        m "And I'm pretty sure if I ate me, I'd die."
        show troll talking
        t "Are you evil?"
        show troll silent
        m "I guess not."
        jump wrong
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest

label disease_left:
    "You should've thought that through a bit more."
    show troll talking
    t "You have one more guess."
    show troll silent

menu:
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest
    "Disease.":
        show troll talking
        t "Incorrect."
        t "How would it be disease?"
        show troll silent
        m "The poor are super filthy and have a bunch of diseases."
        m "It can spread through food, so eating it would kill you."
        m "And do you know how many people plagues kill?"
        m "That's evil."
        show troll talking
        t "But do rich people need disease?"
        show troll silent
        m "Population control?"
        show troll talking
        t "That's a flimsy argument."
        show troll silent
        jump wrong

label love_left:
    "You should've thought that through a bit more."
    show troll talking
    t "You have one more guess."
    show troll silent

menu:
    "Nothing.":
        show troll talking
        t "Great job."
        t "Now you get to cross my bridge."
        hide troll talking
        "He steps aside and you continue on your merry way."
        jump day_forest
    "Love.":
        show troll talking
        t "Incorrect."
        t "How would it be love?"
        show troll silent
        m "Love is evil because it makes you hurt like nothing else can."
        m "The rich need love because they've spent too much time focusing on money and need human connection."
        m "And love is the most powerful thing in the world."
        show troll talking
        t "That last part was pretty cheesy."
        t "Speaking of cheese, how does one eat love?"
        show troll silent
        m "Ummm..."
        show troll talking
        t "That's what I thought."
        show troll silent
        jump wrong

label wrong:
    show troll talking
    t "That was three guesses."
    t "You can't cross."
    if seen_wizard is True:
        jump procrastinator_ending
    else:
        "Since you can't cross the bridge, you might as well try your other idea of asking the wizard if he can teleport you."
        python:
            seen_troll = True
        jump wizard

label troll_again:
    t "I told you that you can't cross."
    show troll silent
    m "What are you talking about?"
    show troll talking
    t "You got three guesses to solve my riddle and you failed."
    t "Turn around."
    show troll silent
    m "You must be thinking of someone else because I definitely haven't been here before."
    show troll talking
    t "You don't think anyone has tried that trick?"
    t "Believe me, it takes more than a day to forget someone's face."
    show troll silent
    m "Listen, I have a very important mission, so I don't appreciate whatever game you're playing."
    show troll talking
    t "You're trespassing on my home and I have the right to remove you."
    t "This is your last warning."
    show troll silent
    m "You're being really unreasonable. You can't just-"
    "You're cut off by the troll charging at you."
    "As a reflex, you draw your sword and make a counter attack."
    show troll dead
    "Your blows appeared to be lethal, as the troll collapses without making any more attacks."
    "You didn't want to resort to violence, but he left you no choice."
    "You were only acting in self defense."
    hide troll dead
    "You step over his corpse and continue on your merry way."
    jump night_forest

label day_forest:
    scene forest entrance
    "You continue your stroll to a forest entrance."
    "You decide to walk even slower to make a dramatic entrance into the forest."
    "If you had sunglasses, you'd be taking them off as you walked in."
    "If explosives were invented, there would be an explosion behind you."
    "However. without either of those, you just kind of look like an idiot."
    scene forest
    "Thankfully, no one seemed to be around to see your over the top entrance."
    "In fact, you wander through the entire forest without seeing so much as a trace of other sentient life."
    jump tower

label night_forest:
    scene forest entrance
    "As the sun sets, you arrive at the entrance of a forest."
    "Somewhat wary, you enter with caution."
    scene black
    "Without the light of day, you can't see where you're going, but you press forward."
    m "For the princess."
    "You barely make it a few steps before your legs are swept out from under you."
    "Almost immediately, you feel something hit your head."
    "Everything goes black."
    "Well, everything already was black."
    "But now you're unconscious."
    scene spit
    "When you come to, you feel really warm."
    "It's rather comforting..."
    "Until you realize you're being spun over a fire pit."
    m "AAAAHHHHH!!!!!!"
    m "Someone get me down."
    u "I'm afraid that won't be happening."
    "Your captor emerges."
    show gnome talking at left
    g "We don't often get humans to eat here."
    g "The tribe will be pleased with this feast."
    show gnome silent
    m "You can't eat me!"
    m "I'm a person!"
    show gnome talking
    g "Like this is any different than when you eat chickens or pigs."
    show gnome silent
    m "Well, I can talk and think."
    show gnome talking
    g "Just because you don't understand them, doesn't mean they don't talk."
    g "I personally don't care about sentience."
    g "When you live in a forest, you eat what you can get."
    g "Now if you'll excuse me, I don't like to talk to my food."
    show gnome silent
    "It's clear that he's about to leave."
    "You should really decide what you're going to do about this situation."

menu:
    "Try to escape.":
        jump extra_crispy_ending
    "Negotiate.":
        jump captive_ending

label tower:
    scene path
    "After emerging from the forest, you continue to meander down the path."
    scene tower
    "Finally, you arrive at the tower."
    "Sensing your presence, the dragon lands in front of you."
    show dragon normal
    d "RAAWWWRRR!!!!!"

menu:
    "Slay the dragon.":
        jump slay
    "Befriend the dragon.":
        jump befriend

label slay:
    "You plunge your sword deep into the dragon's stomach."
    show dragon dead
    "You expected more of a fight, but instead his body just falls to the ground."
    hide dragon dead
    m "Take that, foul beast!"
    scene tower close up
    "Victorious, you approach the tower and call out to the princess."
    m "Rapunzel! Rapunzel! Let down your hair!"
    p "Who's Rapunzel?"
    m "Uh..."
    m "Nevermind. Can you just let down your hair?"
    p "How long do you think my hair is?"
    m "I don't know, but how am I supposed to get up to you?"
    p "Maybe you don't have to. Maybe you can just get me down."
    "Get her down? An idea pops into your head."
    "You start to pull rocks out of the base of the tower."
    "Without a foundation, the tower tumbles to the ground."
    p "AAHHHHH!!!!!!!"
    scene tower fallen
    "And just like that..."
    "You failed."
    "On second thought, maybe bringing the tower to the ground wasn't the smartest idea."
    "You could've gone back to Sticklandia for backup. You could've gotten a ladder. Yet you chose the stupidest option possible."
    "The least you can do at this point is bring the princess back for a proper burial."
    jump failure_ending
    

label befriend:
    "You know that you're supposed to kill the dragon, but you can see a sadness deep within him."
    "Maybe he doesn't need to die."
    "Maybe he just needs a friend."
    m "Hello, Mr. Dragon. Is everything okay?"
    d "Huh?"
    m "Are you feeling okay?"
    d "Why do you care?"
    m "You looked a bit sad and I thought I could help cheer you up."
    d "You wanted to cheer me up?"
    m "Of course."
    d "But I'm keeping your princess prisoner. You should be attacking me."
    m "Well just because you're a criminal, doesn't mean you don't have feelings."
    show dragon crying
    "The dragon starts to cry."
    d "No one's ever wanted to know how I feel."
    d "It's not like I wanted this life."
    d "But the only job that hires dragons is guarding stolen princesses."
    m "I have some sway in Sticklandia. Maybe I could help you find a job there."
    d "Really? You'd do that for me?"
    m "It would be my honor."
    show dragon normal
    d "Thank you so much! How can I ever repay you?"
    m "A good start would be flying me up to the princess."
    d "Of course. It's the least I could do for you."
    "You hop on the dragon's back and he flies you up to the window of the tower."
    scene prison
    "You enter the tower through the window and see the barren room that's holding the princess."
    "You feel bad for her, even though she's been here less than a day and she's spent the last eighteen years sleeping in a luxurious bedroom."
    show princess talking
    p "Oh my god! Is someone here to rescue me?"

menu:
    "Talk to her.":
        m "No fear princess. I was sent here by your father to bring you home."
        p "I knew my father would send a brave knight after me. He cares about me so much."
        show princess silent
        m "Ummm..."
    "Kiss her.":
        jump date

menu:
    "Tell her the truth.":
        jump stitches_ending
    "Lie to her.":
        jump winner_ending

label date:
    "You pucker your lips and lean for a kiss, but the princess blocks you."
    show princess talking
    p "Woah, woah, woah."
    p "Did you think you could kiss me just because you're rescuing me."
    p "We just met!"
    show princess silent
    "You internally face palm."
    "How could you have been so inconsiderate?"
    m "My apologies, your highness. I just got caught up in the heat of the moment."
    m "Please allow me to treat you to dinner so we can become properly acquainted."
    "She takes a moment to consider your offer."
    show princess talking
    p "Ok, I'll allow it."
    p "Despite the awkward first impression, I do still appreciate you rescuing me."
    p "I suppose only a bold knight, such as yourself, could be capable of such a feat."
    show princess silent
    m "You flatter me, your highness."
    m "As for our date, let me take you to my favorite restaurant."
    show princess talking
    p "That sounds great."
    show princess silent
    m "I'm glad you're excited. Let us begin the night with a ride on dragonback."
    "The two of you exit through the window and ride the dragon back to your restaurant of choice."
    scene restaurant front
    show dragon normal
    "The dragon drops you off in front of the restaurant."
    m "Thanks for the ride!"
    d "No problem."
    hide dragon normal
    "He flies off to... somewhere."
    p "So this is the place?"
    m "Yup."
    "Ahh, Modern Times."
    "Modern Times Dinner & Tournament is a fun family dinner theater themed as a royal banquet and tournament of jousting, sword fighting, and games of skill."
    "Before you became a knight, you used to work here as part of the show."
    "However, you wonder if the princess might think less of you if she found out you worked in the service industry."
    python:
        date_fail = False
        knows_past = True

menu:
    "Keep quiet.":
        "There's no way that she'd want to be with you if you told her."
        "You figure it's best to keep it to yourself."
        python:
            date_fail = True
            knows_past = False
    "Tell her about your past.":
        "While you're not sure how she'll react, you figure honesty is the best policy."
        m "I actually used to work here."
        p "Really? What did you do?"
        m "I was part of the jousting event."
        p "I bet that was fun."
        "She seemed to take that pretty well."

label date_2:
    m "Let's head inside."
    scene restaurant tickets
    show princess silent
    "Since you don't have a reservation, you need to pay for tickets."
    "As you approach the counter, you notice the princess pull some gold coins out of her pocket."

menu:
    "Offer to pay.":
        "The gentleman that you are, you don't believe that the woman should pay on the first date."
        m "No need, princess. I can cover it."
        show princess talking
        p "Thank you, but it's really no big deal to me."
        p "I am royalty, after all."
        p "This is not even my week's allowance."
        show princess silent
        "She does make a good point, as you aren't sure how much you have on you."
    "Let her pay.":
        "You figure that, as a princess, she can afford this more than you."
        show princess back at right
        "She walks up to the counter and holds out her money."
        p "Two, please."
        "The person at the counter, takes her money and hands her two tickets."
        jump date_3

menu:
    "Insist on paying.":
        "Regardless of the wealth gap between the two of you, you believe it's improper for a woman to have to pay for the first date."
        m "I insist, princess. I've got this."
        "You fish around in your pockets for whatever change you have."
        "The princess looks uncomfortable, as she waits over a minute for you to cobble together enough money for two tickets."
        "You walk up to the counter and hold out your money."
        m "Two, please."
        "The person at the counter, takes your money and hands you two tickets."
        python:
            date_fail = True
    "Let her pay.":
        m "Thank you, your highness. I appreciate that."
        "She walks up to the counter and holds out her money."
        p "Two, please."
        "The person at the counter, takes her money and hands her two tickets."
        jump date_3

label date_3:
    "You promptly enter the main room and find your seats."
    scene restaurant inside
    show princess silent at right
    if have_rose is True:
        "You remember that you picked a rose that morning in the rose patch along the path to the tower."
        "You suppose that now would be a good occasion to use it for."
        m "I picked a rose earlier today. I'd like to think fate wanted me to give it to you."
        "You hand her the rose and notice her cheeks blush."
        show princess talking
        p "How thoughtful of you."
        show princess silent
    else:
        "You want to give her some kind of gift, but unfortunately don't have anything."
    "You have some time before the show begins, so you start up some small talk."

menu:
    "How was your day?":
        m "So, how has your day been so far?"
        show princess talking
        p "Terrible. I was kidnapped."
        show princess silent
        "You feel stupid for not assuming that's how she would answer."
        "You were literally the one to rescue her."
        "An awkward silence follows, which is broken by the sound of a familiar voice."
        python:
            date_fail = True
    "Lovely weather we're having.":
        m "Lovely weather we're having today, right?"
        show princess talking
        p "I know."
        p "That's what I was thinking as we were flying on the back of that dragon."
        p "Speaking of which..."
        p "How did you get him to give us a ride?"
        show princess silent
        m "He was only keeping you prisoner because he was having trouble finding a better job."
        m "So I offered to help him find a job here in Sticklandia."
        show princess talking
        p "How kind of you to look past his scary exterior and offer to help him."
        p "If it's a job he's looking for, maybe he could work here."
        p "I'm sure a live dragon would be great entertainment."
        show princess silent
        m "That's a great idea."
        "You would love to keep talking, but your conversation is interrupted by the sound of a familiar voice."
    "What do you do for a living?":
        m "So, what do you for a living?"
        show princess talking
        p "I'm a princess, so nothing."
        p "I just get an allowance from my dad."
        show princess silent
        "You feel stupid for asking that kind of question."
        "The royal family doesn't work like the common population."
        "An awkward silence follows, which is broken by the sound of a familiar voice."
        python:
            date_fail = True

label date_4:
    s "Hey, how's it going?"
    show server talking at left
    "You recognize this server from when you used to work here."
    "You would talk a lot during your breaks."
    s "It's been a while, hasn't it?"
    show server silent
    show princess talking
    p "Who's this, sir knight?"
    "You start to open your mouth, but your friend answers first."
    show princess silent
    show server talking
    s "Me and him go way back."
    s "When he worked here a couple years ago, we were great friends."
    show server silent
    if knows_past is True:
        show princess talking
        p "That's cool."
        show princess silent
        m "Yeah, it has been way too long though."
        m "Things have been great. I'm an actual knight now."
        show server talking
        s "You're kidding! That's incredible!"
    else:
        show princess talking
        p "I didn't know you worked here."
        show princess silent
        show server talking
        s "Really? He worked here for several years back in the day."
        s "He was the best jouster we've ever had."
        show server silent
        show princess talking
        p "Why wouldn't you mention any of that?"
        show princess silent
        "The tension in there is palpable and your friend seems to pick up on it."
        show server talking
    s "Would you look at that? The show is starting."
    s "It was nice catching up, but I've got to go."
    s "Have fun, you two."
    hide server talking
    "The two of you eat your meals and watch the show."
    "Now the night is wrapping up."
    show princess talking
    p "Listen..."
    if date_fail is False and have_rose is True:
        jump true_ending
    elif date_fail is False:
        jump friend_zone_ending
    else:
        jump deja_vu_ending

label wizard:
    "You make your way to the wizard's hut."
    scene home
    show wizard silent at right
    m "Hello wizard! How are you today?"
    show wizard talking
    w "I'm doing alright, how are you Sir Knight?"
    show wizard silent
    m "Honestly, I could be better."
    if seen_troll is True:
        m "The king gave me a quest to save tne princess from a dragon-guarded tower."
        m "However, I got stopped by a troll because I couldn't solve his riddle."
    else:
        m "I just received terrible news that the princess has been kidnapped."
        m "Now she's being held prisoner in a dragon-guarded tower."
    m "Do you think you could teleport me to the princess?"
    show wizard talking
    w "Do you always do what the king asks you to do?"
    show wizard silent
    if seen_troll is True:
        m "Yes."
        m "The king told me to not to rush, so I have taken my time every step of this journey."
    else:
        m "No."
        m "Just now, the king told me not to rush, but I decided to come to you so you could teleport me to the princess and get me to her as soon as possible."
    show wizard talking
    w "That's the funny thing isn't it?"
    w "The king doesn't seem to care that much about his daughter, does he?"
    w "You'd think he'd want his daughter back as soon as possible."
    show wizard silent
    m "It's not my place to judge his majesty's family dynamics."
    show wizard talking
    w "Then whose place is it?"
    w "He is in charge of your home. I think that gives you right to judge him."
    w "If he doesn't care about his daughter, how much do you think he cares about Sticklandia?"
    show wizard silent
    m "What is it you're saying wizard? This sounds like treason."
    show wizard talking
    w "This isn't treason."
    w "This is thinking clearly."
    w "Treason is sitting on your throne getting fat from the most luxurious foods in all the lands while many live off of scraps."
    show wizard silent
    m "First of all, I'm pretty sure the king is as thin as any of us."
    m "Second, what else is a king supposed to do?"
    show wizard talking
    w "You're so naive."
    w "You look up to the king, but you have no idea how terrible of a leader he is compared to kings past."
    w "You are being tasked with rescuing the princess under the current king's reign, but his father..."
    w "He would've gone to rescue his daughter himself the very moment he learned of her disappearance."
    show wizard silent
    m "What are you getting at?"
    show wizard talking
    w "We need a change in leadership."
    show wizard silent
    m "YOU WANT TO OVERTHROW THE KING?!?!"
    show wizard talking
    w "Keep your voice down."
    w "We have to keep a low profile."
    show wizard silent
    m "We? What do you mean \"we?\""
    show wizard talking
    w "I'm offering you a choice."
    w "Do you want to join the uprising?"
    show wizard silent
    "You feel conflicted."
    "You've sworn an oath to serve the king..."
    "But Sticklandia might be better off without him."

menu:
    "Join the wizard.":
        jump revolution
    "Remain loyal.":
        m "No, I can't betray the king."
        show wizard talking
        w "Very well, it was worth a try."
        w "I'll give you this potion that I had prepared."
        w "It'll take you where you need to go."
        show wizard silent
        "He hands you a blue potion."
    
menu:
    "Drink the potion.":
        "You can't be sure this potion will make you teleport, but you have to try."
        "You gulp down the potion, but you don't go anywhere."
        "You're confused. The wizard told you..."
        "Wait... what did the wizard tell you?"
        "For that matter, what are you doing inside the wizard's hut?"
        m "Excuse me, what am I doing here?"
        show wizard talking
        w "You're on a mission from the king to save the princess from a dragon-guarded tower."
        w "You came here for a teleportation potion, but I informed you that there was nothing I could do."
        show wizard silent
        m "Oh..."
        m "I guess I should resume my journey then."
        show wizard talking
        w "Don't rush."
        show wizard silent
        "You look at the wizard, perplexed."
        show wizard talking
        w "King's orders."
        show wizard silent
        "You shrug and nonchalantly walk towards the path to the tower."
        python:
            seen_wizard = True
        jump rose
    "Attack him.":
        jump death_by_magic_ending

label revolution:
    m "Count me in."
    show wizard talking
    w "Splendid."
    show wizard silent
    m "So what's the plan?"
    show wizard talking
    w "I'm glad you asked."
    w "First we enter the castle through the secret underground tunnel that I have hired a brute to dig for the past year."
    w "Next, we each take a swig of my invisibility potion, which I have spent years perfecting."
    w "This will allow us to move around the castle without being noticed."
    w "Once invisible, we will sneak into the king's private dining room."
    w "We will wait for his taster to have a sip of his chosen beverage."
    w "After the drink passes inspection and the taster leaves, you will create a distraction to draw the king's attention."
    w "Then, while he is distracted, I will swap out the drink for this vial of poison."
    "He gestures to a green, fizzling potion on his shelf."
    w "It took several months just to brew that one dose."
    w "Once the poison is in place, all we have to do is wait for him to collapse."
    w "Then the throne will be all mine."
    w "Mwah-hah-hah-hah."
    show wizard silent
    m "This is about the people, though. Right?"
    show wizard talking
    w "Of course."
    w "My own glory will simply be a byproduct of turning Sticklandia into the greatest empire the world has ever seen."
    show wizard silent
    m "Okaaaaay..."
    "You get the sense that the wizard's intentions might not be as pure as he claims."
    "But that's a drastic accusation to make, so you play along."
    m "I have some notes."
    show wizard talking
    w "I have spent years devising this plan. What flaws could you possibly have found?"
    show wizard silent
    m "First of all, that poison is way too on the nose."
    m "There's no way that anyone would drink that, thinking that it's anything but a one way trip to the afterlife."
    m "Second, this plan seems too complicated."
    m "Why don't we just walk into the throne room and stab him?"
    show wizard talking
    w "Just walk in..."
    w "and stab him?"
    show wizard silent
    m "Yeah."
    show wizard talking
    w "That's idiotic."
    w "He has dozens of guards."
    show wizard silent
    m "One of which is me."
    m "Besides what reason would any of them have to suspect us?"
    show wizard talking
    "The wizard opens his mouth to respond, but no sound comes out."
    "At first, he is dumbfounded by how foolproof your plan is."
    "Then, he becomes angry with the simplistic nature."
    w "I did not spend years on this plan just for you to show up and simply decide to stab him."
    w "This is my revolution so we should go with my plan."
    show wizard silent
    m "Isn't the important thing that the tyrannical king is removed from power?"
    m "Does it really matter who gets the credit?"
    show wizard talking
    w "Yes, it does."
    w "How will my subjects praise my intellect if I'm not the mastermind behind this operation?"
    w "I mean, my plan is more subtle and therefore more reliable."
    show wizard silent
    "He is seeming really suspicious now."
    "However, it's too late to back out now."
    "Maybe you should just go with his plan to make him feel better."
    "Then again, you're really proud of your plan and it's like a child to you."

menu:
    "Go with the wizard's plan.":
        jump cellmates_ending
    "Go with your plan.":
        m "Hmmmmm..."
        m "No thanks."
        "You leave the wizard's hut and walk towards the castle."
        show wizard talking
        w "Hey! Wait up!"
        scene throne
        show king silent
        "You arrive in the throne room with wizard nervously following behind you."
        show king talking
        k "Not that I care, but I'm obliged to ask.."
        k "Why have you returned without my daughter?"
        show king silent
        m "It's kind of a long story, but I went to the wizard for a teleportation potion and he convinced me to kill you."
        show king talking
        k "Is that so?"
        show king silent
        show wizard talking at left
        w "Of course not, your majesty."
        w "I would never dream of doing anything to harm you."
        show wizard silent
        m "What happened to not thinking he was a competent ruler?"
        show king talking
        k "You said what about me?"
        k "You really think you could do a better job by waving your little wand around and shouting \"Bippity Boppity Boo?\""
        show king silent
        show wizard talking
        w "Don't you mock my magic, old fool!"
        w "I could reduce this castle to ash! I could blast your head clean off! I could-"
        show king talking
        k "But what policy changes would you make to better the kingdom?"
        show king silent
        w "Anything would be better than what you're doing!"
        show wizard silent
        m "The king actually makes a good point."
        m "What would you do better?"
        show wizard talking
        w "Why does it matter? This imbecile will run this kingdom into the ground if we don't overthrow him!"
        show wizard silent
        show king talking
        k "We're still waiting to hear how you're going to do better."
        show king silent
        show wizard talking
        w "Enough dilly dally!"
        w "I've spent years plotting for the moment I'd seize the throne for myself!"
        w "I'm not letting anything stop me now!"
        "You can tell that the wizard is about to cast some spell."
        "If you want to stop him, now is the time, but you're not sure what to do."
        "The king seems quite apathetic, but the wizard might actually be evil."

menu:
    "Let the wizard kill the king.":
        jump hostile_takeover_ending
    "Kill the wizard.":
        jump loyalist_ending
    "Kill them both.":
        "These two can't be the only candidates for ruler of Sticklandia."
        "There has to be another way."
        "Before the wizard can speak a word, you slice his head off."
        show wizard dead
        "His headless body drops to the floor."
        hide wizard dead
        show king talking
        k "Marvelous work, young knight."
        k "Let us celebrate-"
        "You plunge your sword deep into the king's chest."
        "It isn't long before he bleeds out."
        show king dead
        "You're left alone in the throne room and you feel a sense of hope."
        "You know just how to improve Sticklandia..."

menu:
    "Take the crown.":
        jump king_ending
    "Destroy the crown.":
        jump democracy_ending

label eternal_sleep_ending:
    "Doesn't matter."
    "You made your bed and now you have to lie in it."
    "Eternal Sleep Ending"
    return

label lore_dump_ending:
    "I'm glad I could answer all of your questions."
    "At least I answered all of the questions that I predicted you might ask."
    "Thank you for playing through all of my game."
    "Lore Dump Ending"
    return

label nose_ending:
    "There's no turning back."
    "This is your life now."
    "You honestly can't remember what you did before this anyways."
    "All that matters to you now is figuring out how to smell these roses."
    "At this point, there's only one thing left that you haven't tried."
    m "Almightly artist..."
    m "You are the creator of the world that I inhabit."
    m "You hold the power of life and death in your pen."
    m "I have not desired much before, but now I humbly beg of you..."
    m "Please let me have a nose."
    "You pause and await a response, hoping that you did not make your request in vain."
    "A booming voice beckons to you."
    a "What the hell?"
    m "What is the matter, oh great one?"
    a "What's the matter? I just spent an hour of my life drawing you try to smell roses."
    a "Now you have the nerve to try to ruin the consistency of this game's art style by requesting a nose?"
    m "Yes?"
    a "You ungrateful twig!"
    a "I'm done."
    a "I started doodling you because I thought it would be fun to draw a medieval adventure."
    a "Instead you sidetracked the whole thing by sitting around in a patch of roses that you couldn't even smell."
    a "I have a life you know."
    a "I go to school, I'm in a relationship, and I have many other hobbies."
    a "I take time out of my busy schedule to give you life and all you want to do is sit among flowers."
    a "Fine."
    a "I don't have to keep drawing you."
    m "I'm sorry. I didn't mean to be so disruptive. I can..."
    a "Save it."
    a "I've already had enough of you."
    a "I hope you enjoy your roses."
    "A nose suddenly appears on your face."
    "The scent of the roses begins to fill your nose."
    "You try to open your mouth to thank the artist, but you can't."
    "In fact, you can't move any part of your body."
    "It seems like your nose is the last thing he'll ever draw for you."
    "You drew a nose for you and now he'll never draw you again."
    "Well, this is what you get for pissing off the creator of your world."
    "At least, you can smell the roses now."
    "You focus on the scent, but you tire of it within minutes."
    "This is life now."
    "Stopping to smell the roses."
    "Nose Ending"
    return

label rip_ending:
    "You move to stow the rose away, but you feel something already in your pocket."
    m "Another rose?"
    "There appears to be another rose missing from the patch."
    m "I wonder..."
    "You pull the mysterious rose out and compare the stem to the uprooted one."
    "It's a match."
    "You are overwhelmed with confusion."
    "You've clearly been here before, since you took a rose from here."
    "However, you have no memory of being here."
    m "What is real?"
    m "Are my actions my own if I have no recollection of taking them?"
    "You're driven insane by this discrepancy between your memory and the material world."
    "Your body walks back to the kingdom, spouting nonsense about existence and agency."
    "Your mind, however, was left behind in the rose patch."
    "Rose Induced Psychosis Ending"
    return

label daredevil_ending:
    "You know there has to be a better way out of this than solving a stupid riddle."
    m "If the books are correct, then you live under this bridge."
    show troll talking
    t "Not all trolls live under bridges, you know."
    t "That's just a stereotype."
    show troll silent
    "The troll is silent for a bit, but eventually sighs."
    show troll talking
    t "Yes, I live under this bridge."
    show troll silent
    m "And you can't breathe underwater, can you?"
    show troll talking
    t "No, why?"
    show troll silent
    m "The river must not be that deep, then."
    m "Otherwise, you'd surely drown in your sleep."
    "You walk down towards the river bank."
    show troll talking
    t "No, it's not that deep, but-"
    m "And if you can stand in one place, the current must not be that strong."
    t "Well-"
    m "I don't need your bridge then, I can just-"
    "As you say that, you take your first two steps into the river and are immediately swept away by the current."
    scene river
    "It occurs to you as float down the river that troll has quite a bit of mass."
    "Meanwhile, you are as light as a stick."
    "Maybe you should've thought this through a bit more."
    "You try to swim to the bank, but your noodle arms don't have the strength."
    "All that you can do is wait to see where the river leads."
    "Within a few minutes, you get your answer."
    "As you start to hear water crashing, you realize that you're headed towards a waterfall."
    "Your last thoughts as go off the edge are that you wish you had a barrel."
    "Daredevil Ending"
    return

label procrastinator_ending:
    "You've already seen the wizard and know that you can't teleport your way to the princess."
    m "Listen..."
    m "I'm on an important quest and this is the only path to my destination."
    m "Is there anything I can do?"
    show troll talking
    t "Rules are rules."
    t "You got the riddle the wrong."
    t "Now you have to turn around and go back to wherever you came from."
    show troll silent
    m "Can I try again tomorrow?"
    show troll talking
    t "Pardon?"
    show troll silent
    m "Can I get three more tries tomorrow?"
    show troll talking
    t "Absolutely not."
    t "You got three attempts to cross this bridge. That's it."
    show troll silent
    m "There's no way you can remember every single person that's ever tried to cross your bridge."
    m "How would you know if any given person has already failed, already succeeded, or hasn't tried yet?"
    show troll talking
    t "Ummm..."
    show troll silent
    m "If I came back in a few months, you probably wouldn't remember and would just let me try again, right?"
    show troll talking
    t "I suppose."
    show troll silent
    m "So if it's fair for me to get more tries again far enough into the future where you don't remember me, how is it unfair that I don't get to try again any time sooner?"
    show troll talking
    t "I suppose you make a good argument."
    t "But you can't try again tomorrow."
    t "This cannot become a daily routine."
    t "I'll let you have three guesses per week."
    show troll silent
    m "That's fair enough."
    m "I'll see you next week!"
    "Now all you need to do is get an extension from the king."
    scene throne
    show king talking
    k "You need another week to save my daughter?"
    k "Okay."
    k "Take all the time you need."
    show king silent
    "That was easier than expec-"
    "Who are you kidding?"
    "You knew it would be that easy."
    "All you need to do now is figure out what you're gonna do for the next week."
    "Procrastinator Ending"
    return

label extra_crispy_ending:
    "You wait for the gnome to be out of sight."
    hide gnome silent
    "Then, you reach for your sword."
    "You manage to successfully grab it and use it to cut yourself down."
    scene fire
    m "AAAAAAHHHHHHHH!!!!!!"
    "Unfortunately you landed directly into the fire."
    "You may be down, but you're still tangled in rope."
    "It doesn't seem like you're gonna be able to get out of this."
    "Before you perish, the last thing you hear is the gnome."
    g "Oh no!"
    g "The king doesn't like his food charred."
    "Extra Crispy Ending"
    return

label captive_ending:
    m "Wait!"
    "The gnome stops."
    show gnome talking
    g "What is it?"
    show gnome silent
    m "Maybe there's a way that I could help you and then you don't have to eat me."
    show gnome talking
    g "I doubt that."
    g "You're gonna provide us with a lot of meat."
    show gnome silent
    m "What if I helped you hunt?"
    m "I notice that, with all due respect, you are pretty small."
    m "Having someone of my size around could help you get larger prey."
    m "In enough time, I'll be able to get you even more meat than you would from eating me."
    show gnome talking
    g "That is a decent idea."
    g "Let me check with the king."
    hide gnome talking
    "The gnome leaves for several minutes before returning."
    show gnome talking at left
    g "The king accepts your proposal."
    show gnome silent
    "He helps you down from the spit."
    show gnome talking
    g "I'll take you to your accommodations."
    scene tent
    g "Get a good night's rest."
    g "You start in the morning."
    g "If this doesn't work, you're back on the menu."
    "He leaves you alone in your tent."
    "You saved your life, but at what cost?"
    "How long will it take to pay off your debt?"
    "If you ever do, who's to say they'll let you free."
    "You just hope that someday you'll be able to save the princess."
    "Captive Ending"
    return

label death_by_magic_ending:
    "You don't know whether that's a teleportation potion or not, but it doesn't matter."
    "You can't just ignore the fact that the wizard is plotting a revolution."
    "Instead of drinking the potion, you draw your sword."
    m "I won't let you live as long as you pose a threat to the crown."
    show wizard talking
    w "So that's how it's going to be?"
    "He opens his mouth to speak an incantation."
    "You charge him in hopes that you can land a hit before he does whatever he's planning, but..."
    w "Abra Cadabra!"
    show wizard silent
    "Less than a foot from the wizard, you collapse to the ground."
    "Your heart isn't beating like it should."
    "You're falling in and out of consciousness."
    "As you feel your life force fleeting, all you can think about is how you failed the crown."
    "The wizard is free to enact his sinister plot and the knowledge of it dies with you."
    "The kingdom will have to stop him without you."
    "Death By Magic Ending"
    return

label loyalist_ending:
    "Whatever the wizard plans to do, it can't be good."
    "Before the wizard can speak a word, you slice his head off."
    show wizard dead
    "His headless body drops to the floor."
    hide wizard dead
    show king talking
    k "Marvelous work, young knight."
    k "Let us celebrate this victory with a feast."
    show king silent
    m "You're not mad at me for wanting to kill you?"
    show king talking
    k "Eh..."
    k "Who doesn't want to kill me?"
    k "The important thing is that you saved me from the wizard."
    show king silent
    m "Don't you want me to resume my mission of saving your daughter?"
    show king talking
    k "She can wait for another time. Meanwhile, what you did today. That was heroic."
    "His praise means the world to you."
    "Or does it?"
    "The wizard may have had ulterior motives, but at least he would've been a more effective leader."
    "It makes you wonder..."
    "Did you make the right choice?"
    "Loyalist Ending"
    return

label hostile_takeover_ending:
    "You're unsure about the wizard, but anyone has to be better than the current king, right?"
    w "Maxima Inferno!"
    show wizard silent
    "To your bewilderment, the wizard sets the castle ablaze."
    "The fire spreads and castle begins to crumble."
    "A piece of the ceiling falls and crushes the king."
    hide king silent
    m "Isn't this overkill?"
    m "I thought you wanted to be subtle."
    show wizard talking
    w "A silent coup has its purpose, but sometimes you need to send a message."
    show wizard silent
    m "A message to who?"
    show wizard talking
    w "To everyone."
    w "No one messes with me and walks away."
    "You're not sure what to say, but you don't get the chance anyways."
    scene black
    "A smaller rock lands on your head and knocks you out."
    scene throne ruined
    show wizard king
    "You come to and see the wizard sitting on the throne, surrounded by ash and rubble."
    "Was this violence a means to an end..."
    "Or is this the beginning of tyranny?"
    "It makes you wonder..."
    "Did you make the right choice?"
    "Hostile Takeover Ending"
    return

label king_ending:
    "There's nothing standing in your way."
    "You reach down to the king's corpse and move the crown to your own head."
    hide king dead
    "You take your seat on the throne."
    "It feels..."
    "right."
    "Almost like this seat has been waiting for you since it was crafted."
    "The power of the throne is intoxicating."
    "Now that you've tasted it, there's no way you're going to let it go."
    m "Guards!"
    "Your once coworkers now arrive to carry out your will."
    m "Find the princess in her tower..."
    m "and kill her."
    "They seem confused by your orders at first, but oblige nonetheless."
    "A wide grin overtakes your face."
    "You could get used to this."
    "King Ending"
    return

label democracy_ending:
    "There has been so much fighting over this crown."
    "It has to end."
    "You walk over to the wizard's corpse and grab his staff."
    "You raise it up high and bring it down onto the crown."
    "Over and over again, you break the crown into bits until there is nothing left of it."
    hide king dead
    m "Guards!"
    show one at left
    show two
    show three at right
    "Your coworkers arrive to hear what you have to say."
    m "Spread the word through the kingdom."
    m "The monarchy is over."
    m "In one week's time, we will hold our very first election for the President of Sticklandia."
    m "While you do that, I have a former princess to rescue."
    hide one
    hide two
    hide three
    "You and your fellow knights all exit the castle, hopeful of what the future will bring."
    "Democracy Ending"
    return

label cellmates_ending:
    m "Okay. You've won me over."
    m "Let's do your plan."
    show wizard talking
    w "Excellent. Let me grab my potions and we'll make our way to the tunnel."
    show wizard silent
    "You and the wizard arrive at the tunnel and meet the brute that dug the tunnel."
    scene tunnel
    show brute silent
    show wizard talking at right
    w "Thank you for your hard work."
    show wizard silent
    "He slips the brute a handful of coins."
    show brute talking
    b "This isn't the amount we agreed to."
    show brute silent
    show wizard talking
    w "You'll get the rest soon."
    w "For now, show me to the other end of this tunnel."
    show wizard silent
    show brute talking
    b "Very well then."
    b "This way."
    show brute silent
    "You follow the brute all the way through the tunnel and climb out of the hole at the end."
    scene dungeon
    show brother silent at right
    show wizard talking at left
    w "Wait a second..."
    "As you unpack your surroundings, you feel something hit your head."
    scene black
    "You're out cold."
    scene dungeon filled
    "By the time you come to, the hole that you climbed through has mostly been filled in."
    "Through a small crack, you can see the brute and the strange man that was once in the room shoveling dirt towards your hole."
    "The wizard wakes up a moment later."
    show wizard talking empty
    w "You backstabber!"
    w "You think you can get away with this? Just wait until I-"
    "He looks around, but realizes that his staff and potions were gone."
    b "Missing something?"
    w "You pest! Years of planning are now down the drain because of your insolence."
    show wizard silent empty
    b "Years of your planning, at least."
    b "But for me, I've been waiting years to get my brother out of this dungeon."
    b "He was supposed to serve a few years for stealing a loaf of bread for us to survive."
    b "Instead, the king decided to let him rot in here for life."
    b "When you offered me a job to tunnel into the castle, I knew this was my chance to free him."
    show wizard talking empty
    w "After all that, why wouldn't you just join my revolution?"
    w "Why did you double cross me?"
    show wizard silent empty
    b "I did what you asked."
    b "I dug you a tunnel into the castle."
    b "You just never specified where in the castle."
    b "As for why I'm leaving you here, you've made it plenty clear that you don't care about people like me and my brother."
    b "You just want power."
    b "You'd tear this castle to the ground with my brother in it."
    b "I'm doing the world a favor by leaving you here."
    m "Please don't do this!"
    m "I just wanted a better Sticklandia!"
    m "Don't leave me here!"
    b "How am I supposed to trust you?"
    b "You came here with him."
    b "You can stay here with him."
    "The brute and his brother finish closing off the hole and leave the two of you in the dungeon."
    "You're infuriated that the wizard got you into this situation."
    "Thankfully, the two of you have plenty of time to sort out your differences."
    "Cellmates Ending"
    return

label failure_ending:
    scene throne
    "The king doesn't look happy."
    show king talking
    k "Listen, I'm not mad."
    k "I'm just disappointed."
    k "I know I said she didn't matter that much because I had other daughters, but..."
    k "I can't let you walk free knowing you killed a member of the royal family."
    k "I hereby sentence you to death."
    k "Thank you for your service."
    "Failure Ending"
    return

label winner_ending:
    m "He sure does."
    "You feel about bad lying, but you don't want the king to be mad at you for ratting him out."
    "After all, snitches get stitches."
    "Or in the case of the king, snitches lose their heads."
    m "Well then, princess. Shall I take you home?"
    show princess talking
    p "Yes, brave knight. I'm ready to leave this place."
    "The two of you exit through the window and ride the dragon back to Sticklandia."
    scene throne
    show king talking
    show princess silent at right
    k "Congratulations knight! You successfully rescued my daughter from the dragon."
    k "I am so grateful that I am going to award you with Knight of the Year for the second year in a row!"
    "Winner Ending"
    return

label stitches_ending:
    m "Actually..."
    scene throne
    show king silent
    show princess talking at right
    p "How could you say that about me?"
    show princess silent
    show king talking
    k "Well..."
    k "I do have a lot of daughters-"
    show princess talking
    p "I only have one sister!"
    show princess silent
    k "If it makes you feel any better, I would say the same about her if she was the one kidnapped."
    show king silent
    show princess talking
    p "I never want to see you again!"
    "She storms off to her room."
    hide princess talking
    show king talking
    k "Look what you've done, knight!"
    k "Now my daughter is mad at me!"
    k "This is worse than when she was kidnapped."
    show king silent
    m "I'm sorry, your highness."
    m "I just thought that she deserved to know."
    show king talking
    k "I'm sure you're sorry."
    k "Just like you're sorry for showing up early to your morning assignment."
    k "You need to be punished if you're ever going to learn a lesson."
    k "I hereby demote you to squire."
    show king silent
    m "Your majesty, please."
    m "I'm the most dedicated knight in the order, I'll do anything to make this up to you."
    m "Just please don't strip me of my title."
    show king talking
    k "My decision is final."
    show king silent
    "You feel distraught as your whole life crumbles around you."
    "You should've known better than to speak ill of the king."
    "After all, snitches get stitches."
    "Stitches Ending"
    return
    
label deja_vu_ending:
    p "I don't think this is gonna work out."
    show princess silent
    "Your heart breaks, but you don't want her to see."
    m "That's ok."
    m "Can I at least walk you home?"
    show princess talking
    p "That's alright."
    p "I can get home myself."
    hide princess talking
    "She gets up and walks out of the restaurant."
    "You bury your head into your hands and wonder where you went wrong."
    "However, your pity party is quickly interrupted."
    p "AAAAAHHHHHHH!!!!!!!"
    m "Princess?!?!"
    scene restaurant front
    "You run outside as fast as you can, but the princess is nowhere in sight."
    "Someone must've taken her."
    m "I have a feeling what my assignment will be tomorrow."
    "Deja Vu Ending"
    return

label friend_zone_ending:
    p "You seem like a good guy, but I think we'd be better as friends."
    "Your heart sinks, as she says that."
    scene throne
    show king talking
    show princess silent at right
    "You return the princess to the king and he says something about being grateful."
    "You can't pay attention, though."
    "Your brain is still caught up on the princess."
    "You really fell for her."
    "Is there a worse feeling than loving someone who doesn't love you back?"
    "Friend Zone Ending"
    return

label true_ending:
    p "You seem like a great guy..."
    p "and I had an amazing time tonight."
    p "I would like to see where this goes."
    show princess silent
    m "Me too."
    show princess talking
    p "Great!"
    p "Just one thing..."
    p "Can we take things slow?"
    p "I've never really been in a relationship before."
    show princess silent
    m "Of course, your high-"
    show princess talking
    p "Please."
    p "No more formalities."
    p "You're my boyfriend now."
    p "You can call me babe."
    show princess silent
    m "Okay, babe."
    m "How do you think your dad will react?"
    show princess talking
    p "I don't know. He's very overprotective of me."
    scene throne
    show king talking
    show princess silent at right
    k "How exciting!"
    "That went better than you thought it would."
    k "We'll start wedding preperation at once."
    show king silent
    "Maybe it went a bit too well."
    show princess talking
    p "Dad..."
    p "We're not engaged. We're just dating."
    show princess silent
    show king talking
    k "Are you sure?"
    k "Everyone loves a royal wedding."
    k "The cake, the decorations, the cake, the gorgeous dress, the cake, the-"
    show princess talking
    p "I'm sure, dad."
    show princess silent
    k "Okay, sweetie. If you're sure."
    "He turns his attention back to you."
    k "Now, knight..."
    k "I'm proud of the work that you've done today."
    k "Whether you're marrying my daughter or not, you're family now."
    show king silent
    m "Thank you, your majesty. That means a lot."
    show princess talking
    p "Dad? Can I have my boyfriend now?"
    show princess silent
    show king talking
    k "Very well."
    k "You're dismissed."
    show king silent
    "You leave the throne room and walk the princess up to her bedroom."
    scene door
    show princess talking
    p "Well, this is me."
    p "I had a lovely time with you today."
    p "I can't wait to see where things go from here."
    show princess silent
    "She plants a kiss on your lips and then enters her room."
    hide princess silent
    "You can't help but smile wide."
    "That was the best kiss you've ever had."
    "It also happened to be your first."
    "Either way, it was a perfect end to a perfect day."
    "Thinking about everything that you've done today makes you smile even wider."
    m "What an adventure today was."
    "True Ending"
    return
    

