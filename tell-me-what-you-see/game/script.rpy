# The script of the game goes in this file.

define b = Character("choice_name", image="boy", dynamic=True)
define g = Character("choice_name", image="girl", dynamic=True)
define f = Character("Father", image="father")
define hm = Character("Heart Monitor", image="heartmonitor")
define v6 = Character("Visual Six")

# The game starts here.
label start:
    scene room
    
    v6 "Hello there! Welcome to this visual novel! Please take a minute to customize your story by answering the following questions!"
    
    show girl before pose 1 at left with easeinleft
    show boy before pose 1 at right with easeinright

    menu:
        "Choose your character's gender!"
        
        "Girl":
            hide boy with dissolve
            show girl before pose 1 at center with move
            $ choice_gender = "girl"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                 "You didn't type a name! You can go back and try again, otherwise we can name the character 'Jane Doe' you!"
                 $ choice_name = "Jane Doe"
                
            $ p = g # This fixes the side image problem
            jump hospital_scene_1
            
        "Boy":
            hide girl with dissolve
            show boy before pose 1 at center with move
            $ choice_gender = "boy"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                 "You didn't type a name! You can go back and try again, otherwise we can name the character 'John Doe' you!"
                 $ choice_name = "John Doe"
                
            $ p = b #This fixes the side image problem
            jump hospital_scene_1
            
            
label hospital_scene_1:
    
    $ renpy.music.set_volume(0.3, 0, channel="music")
    play music "audio/Art Of Silence_V2.mp3" fadeout 1.0 fadein 1.0
            
    scene black
    
    play sound "audio/heartbeat_fast.mp3"
    p after "Am I awake? Am I alive?"
    p "Where am I? What happened to me?"
    p "It’s so dark, why is it so dark?"
    
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1, 0.5, channel="music")
    
    scene room
    
    if choice_gender == "girl":
        show girl hospital screaming at left with easeinleft
    else:
        show boy hospital screaming at left with easeinleft
    
    p "Dad!! Daddy!! Are you here?"
    #running footsteps sound effects
    play sound "audio/footsteps.mp3"
    show father standing at center with easeinright  
    if choice_gender == "girl":
        show girl hospital sad
    else:
        show boy hospital sad
    
    stop sound
    f "I’m here, %(choice_name)s.. I’m here sweetheart"
    f "You’re okay, it’s going to be okay."
    p "What happened to me? Where am I?"        
    f "You are at the hospital, sweetheart"
    p "I can feel the bandages on my eyes, why can't i see?"
    f "I don't know, Do you remember anything?"
    
    menu:
        "Does %(choice_name)s remember what happened?"
        
        "No, %(choice_name)s doesn't remember":
            p "No dad, I don’t."
            jump window_scene
                
        "Yes, %(choice_name)s remembers":
            p "I think so..."
            jump flashback_scene_1
           
           
label flashback_scene_1:
    
    scene woods
    play music "audio/bensound-slowmotion.mp3" fadeout 1.0 fadein 1.0
    
    p "It was a beautiful day; the sun was shining brightly and..."
    
    if choice_gender == "girl":
        show girl before pose 1 at center with easeinright
    else:
        show boy before pose 1 at center with easeinright
    with dissolve 
    
    menu:
        "What happened to the kid?"
        
        "Fell":
            $ flashback = "fall"
            p "I fell"
            jump hospital_scene_2
        
        "Accident":
            $ flashback = "accident"
            play sound "audio/bird1.wav"
            p "...the grass was long and tickling my knees and I think I heard the bird chirping, though It was far away...Hmmm"
            f "A bird? Are you sure?"
            stop sound fadeout 1.0
            p "pretty sure...Why do you ask?"
            f "Oh, ah, no reason, please go on..."
            p "We were walking past the old nuclear power plant, then we went inside the fence."
            p "I am not sure how or why we went inside, but I was scared."
            p "Jimmy was kicking an old can along the ground, he was not afraid." 
            p "I felt my legs shaking, something was wrong in there..."
            jump hospital_scene_2
          
          
label hospital_scene_2:
    
    scene room #change to the hospital image
    
    if choice_gender == "girl":
        show girl hospital screaming at left with easeinleft
    else:
        show boy hospital screaming at left with easeinleft
    with dissolve  

    show father armcross right at center with easeinright

    #Add Sound effect of heart beeping
    stop music 
    $ renpy.music.set_volume(0.6, 0.5, channel="sound2")
    play sound "audio/heartbeat_fast.mp3" #couldn't hear this
    play sound2 "audio/heart_monitor_beeps.mp3"
    hm " beep...beep...beep...beep..."
    
    pause
    
    f "%(choice_name)s, please try and calm down, don't overdo it!"
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.3, 0.5, channel="sound2")
    if choice_gender == "girl":
        show girl hospital sad
    else:
        show boy hospital sad 
    with dissolve
    p "I am okay, I want to remember!"
    stop sound2 fadeout 1.0
    if flashback == "fell":
        jump flashback_scene_2
    elif flashback == "accident":
        jump flashback_scene_2
    
label flashback_scene_2:

    scene woods
    play music "audio/bensound-slowmotion.mp3" fadeout 1.0 fadein 1.0
    $ renpy.music.set_volume(0.3, 0.5, channel="music")
    play sound "audio/buzzing.mp3"
    p "There was a loud buzzing sound, Jimmy wanted to go closer to check it out."
    p "I told him not to go...it wasn't safe...then i saw a light."
    p "It was so bright and beautiful, I couldn't look away..."
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.6, 0.5, channel="music")
    
    #show bright light
    scene black
    with fade
        
    p "Then...then, it got dark...all dark...the light is gone and Jimmy's gone..."
    
    scene room
    with fade
    
    show father armcross right at center 
    with dissolve
    
    if choice_gender == "girl":
        show girl hospital sad at left
    else:
        show boy hospital sad at left
    with dissolve
    
    f "It's okay, %(choice_name)s it's all over now, it's okay!"
    p "Will I be able to see when they take the bandages off and my eyes are open?"
    
    menu:
        "Will %(choice_name)s see again?"
        
        "No":
            f "%(choice_name)s, the doctors really don’t know, they’re hoping you will, but it’s just too early to say. I’m sorry darling."
            p "Oh Dad, I will see again, I know I will!"
            p "I have to be okay. my eyes have to be okay. I need to see. I need to see."
            p "Dad"
            f "Yes %(choice_name)s"
            jump window_scene
           
        "Yes":
            f "Yes %(choice_name)s, Yes! of course you will, you just need time to heal. We have to be patient"
            jump window_scene

                                             
label window_scene:         
    
    scene room
    
    p "Is there a window in here?"
    f "Yes there is."
    p "Please dad. Tell me what you see. Don’t leave out a thing!"
    f "Well, um, okay"

    play music "audio/trust_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
    play sound "audio/open_window.mp3"
    
    pause
    
    scene mind 1
    play sound "audio/bird1.wav"
    f "Well...the grass is really green, it's like miles and miles of it..."
    
    scene mind 2
    play sound "audio/wave_ocean.mp3"
    f "There's a couple of rivers that run across it. beautiful and calm."
    
    scene mind 3
    f "The sky is a solid baby blue, there's a couple of clouds up in the sky but not too may, just enough."
    p "That's nice. Tell me more."
    
    scene mind 4
    f "And if you look closely you can see a few mountains peeking behind a cluster of trees. It's extraordinary..."

    scene mind 5
    f "Oh and the flowers! they are so beautiful."

    scene mind 6
    f "It's spring now so they're fully bloomed and in so many different clours, they are pink, yellow and even purple."
    p "That sounds like something straight out of a movie! Are you sure you're not just seeing things?"
    
    menu:
        "Is that what the parent really sees?"
        
        "Yes, it is":
            f "That's exactly what i'm seeing, %(choice_name)s. The view is lovely"
            p "I really miss looking out the window..I took that for granted."
            p "I would give anything just to look out the window right now.."
            jump ending
            
        "No, the parent is lying":
            f "Nature is beautiful, %(choice_name)s"
            p "I really miss looking out the window..I took that for granted."
            p "I would give anything just to look out the window right now.."
            jump ending_plottwist
            
            
label ending:
    
    scene black #need to be changed to window scene
    
    "The End"        


label ending_plottwist:
    
    scene black #need to be changed to window scene with the transitioning/hover Feature
    
    "The End"
        
stop music

return # This ends the game.
