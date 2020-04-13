# The script of the game goes in this file.

define hm = Character("Heart Monitor", image="heartmonitor")
image side heartmonitor = im.Scale("images/heartmonitor.png", 250, 250, xoffset=0, yoffset=0)

# Father
define f = Character("Father", image="father")
image side father = im.Scale("images/father_pose_1.png", 250, 500, xoffset=0, yoffset=200)
image father armcross left = "father_pose_1.png"
image father armcross right= "father_pose_2.png"
image father standing = "father_pose_3.png"

# Boy
define b = Character("choice_name", image="boy", dynamic=True)
image side boy = im.Scale("boy_after_sad.png", 250, 500, xoffset=0, yoffset=200)
image side boy smiling = im.Scale("boy_after_smiling.png", 250, 500, xoffset=0, yoffset=200)
image boy before pose 1 = "boy_before_pose_1.png"
image boy before pose 2 = "boy_before_pose_2.png"
image boy after sad = "boy_after_sad.png"
image boy after smiling = "boy_after_smiling.png"
image boy hospital sad = "boy_hospital_sad.png"
image boy hospital screaming = "boy_hospital_screaming.png"

# Girl
define g = Character("choice_name", image="girl", dynamic=True)
image side girl = im.Scale("girl_after_sad.png", 250, 500, xoffset=0, yoffset=200)
image side girl smiling = im.Scale("girl_after_smiling.png", 250, 500, xoffset=0, yoffset=200)
image girl before pose 1 = "girl_before_pose_1.png"
# TODO: replace this
#image girl before pose 2 = Placeholder("girl")
image girl after sad = "girl_after_sad.png"
image girl after smiling = "girl_after_smiling.png"
image girl hospital sad = "girl_hospital_sad.png"
image girl hospital screaming = "girl_hospital_screaming.png"

# Backgrounds
image black = im.Scale("black.png", 1280, 720)
image woods = im.Scale("woods.jpg", 1280, 720) #To be replaced
#TODO: replace this
#image house = im.Scale("", 1280, 720)
image room = im.Scale("room.jpg", 1280, 720)
image hospital = im.Scale("hospital.png", 1280, 720)
image mind 1 = "mind_1.png"
image mind 2 = "mind_2.png"
image mind 3 = "mind_3.png"
image mind 4 = "mind_4.png"
image mind 5 = "mind_5.png"
image mind 6 = "mind_6.png"

# The game starts here.
label start:

    scene room

    menu:
        "Choose your character's gender!"
        
        "Girl":
            $ choice_gender = "girl"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                "You didnt type a name"
            $ p = g # This fixes the side image problem
            jump scene_1
        "Boy":
            $ choice_gender = "boy"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                "You didnt type a name"
            $ p = b #This fixes the side image problem
            jump scene_1
            
    label scene_1:
        
        #This can later be changed to a mute button option..  This can also count as customization? 
        #Sound effects are clearer and more engaging without music
        
        menu:
            # Start by playing some music.
            "Would you like music to play during this Visual Novel?" 
            
            "Yes":
                play music "audio/Art Of Silence_V2.mp3" fadeout 1.0 fadein 1.0
            
            "No":
                
        scene black
        
        #Add heartbeat sounds to indicate the kid is scared? just a suggestion 
        
        p after "Am I awake? Am I alive?"
        p "Where am I? What happened to me?"
        p "It’s so dark, why is it so dark?"
                
        scene room
        if choice_gender == "girl":
            show girl hospital screaming at left with easeinleft
        else:
            show boy hospital screaming at left with easeinleft
        
        p "Dad!! Daddy!! Are you here?"
        
        show father standing at center with easeinright  
        if choice_gender == "girl":
            show girl hospital sad
        else:
            show boy hospital sad
        
        #running footsteps sound effects?
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
                
                
                scene woods
                play sound "audio/bird1.wav"
                p "It was a beautiful day; the sun was shining brightly and..."
                stop sound
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
                    
                    "Accident":
                        $ flashback = "accident"
                        p "...the grass was long and tickling my knees and I think I heard the bird chirping, though It was far away...Hmmm"
                        f "A bird? Are you sure?"
                        p "pretty sure...Why do you ask?"
                        f "Oh, ah, no reason, please go on..."
                        p "We were walking past the old nuclear power plant, then we went inside the fence."
                        p "I am not sure how or why we went inside, but I was scared."
                        p "Jimmy was kicking an old can along the ground, he was not afraid." 
                        p "I felt my legs shaking, something was wrong in there..."
                        
                        jump cut_scene
                        
    label cut_scene:
        scene room #change to the hospital image
        
        if choice_gender == "girl":
            show girl hospital screaming at left with easeinleft
        else:
            show boy hospital screaming at left with easeinleft
        with dissolve  

        show father armcross right at center with easeinright

        #Add Sound effect of heart beeping
        play sound2 "audio/heartbeat_fast.mp3" #couldn't hear this
        play sound "audio/heart_monitor_beeps.mp3"
        hm " beep...beep...beep...beep.beep.beepbeepbeep"
        stop sound
        
        pause
        f "%(choice_name)s, please try and calm down, don't overdo it!"
        
        if choice_gender == "girl":
            show girl hospital sad
        else:
            show boy hospital sad 
        with dissolve
        p "I am okay, I want to remember!"
        
        if flashback == "accident":
             jump continue_flashback_accident
        
      
    label continue_flashback_accident:
    
    scene woods
    play sound "audio/buzzing.mp3"
    p "There was a loud buzzing sound, Jimmy wanted to go closer to check it out."
    p "I told him not to go...it wasn't safe...then i saw a light."
    p "It was so bright and beautiful, I couldn't look away..."
    stop sound
    
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
        p "Is there a window in here?"
        f "Yes there is."
        p "Please dad. Tell me what you see. Don’t leave out a thing!"
        f "Well, um, okay"
    
        play sound "audio/open_window.mp3"
        play music "audio/trust_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
        
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
