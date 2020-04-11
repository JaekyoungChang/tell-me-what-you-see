# The script of the game goes in this file.

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
image greenbg = im.Scale("greenbg.jpg", 1280, 720)
#TODO: replace this
#image house = im.Scale("", 1280, 720)
image room = im.Scale("room.jpg", 1280, 720)
image woods = im.Scale("woods.jpg", 1280, 720)
image mind 1 = "mind_1.png"
image mind 2 = "mind_2.png"
image mind 3 = "mind_3.png"
image mind 4 = "mind_4.png"
image mind 5 = "mind_5.png"
image mind 6 = "mind_6.png"

# The game starts here.
label start:

    scene greenbg

    menu:
        "Choose your character's gender!"
        
        "Girl":
            $ choice_gender = "girl"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                "You didnt type a name"
            $ p = g
            jump scene_1
            
        "Boy":
            $ choice_gender = "boy"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                "You didnt type a name"
            $ p = b
            jump scene_1
             
    
    
    label scene_1:
        
        # Start by playing some music.
        play music "audio/Art Of Silence_V2.mp3" fadeout 1.0 fadein 1.0

        scene black
        
        p  "Am I awake? Am I alive?"
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
        
        f "I’m here, %(choice_name)s.. I’m here sweetheart"
        p "What happened to me? Where am I?"
        f "You’re at the hospital, sweetheart"
        p"I can feel the bandages on my eyes, why can't i see?"
        f "I don’t know. Do you remember anything?"
        
        menu:
            "Does %(choice_name)s remember what happened?"
            
            "No":
                p "No, I dont"
                jump after_flashback
                
            "Yes":
                 p "The last i remember.. "
                 scene woods
                 p "It was a beautiful day; the sun was shining brightly and…"
                 menu:
                    "What happened to %(choice_name)s?"
                    
                    "Fell":
                        p "I fell"
                        #TO BE CONTINUED
                        jump after_flashback
                        
                    "Got in an accident":
                        scene woods
                        p "I got in an accident"
                        #TO BE CONTINUED
                        jump after_flashback
          
        
        label after_flashback:
        scene room
        show father standing at center with easeinright  
        if choice_gender == "girl":
            show girl hospital sad at left with easeinleft
        else:
            show boy hospital sad at left with easeinleft
            
        p "I can feel the bandages on my eyes and my eyes are closed."
        p "Will I see when they take them off and my eyes are open?"
        f "%(choice_name)s, the doctors really don’t know, they’re hoping you will but it’s just too early to say. I’m sorry darling."
        p "Oh Dad, I will see again, I know I will!"
        p "I have to be okay. my eyes have to be okay. I need to see. I need to see."
        p "Dad"
        f "Yes %(choice_name)s"
        p "Is there a window in here?"
        f "Yes there is."
        p "Please tell me what you see. Don’t leave out a thing!"
        f "Well, um, okay"

        play sound "audio/open_window.mp3"
        play music "audio/trust_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
        
        scene mind 1
        play sound "audio/bird1.wav"
        f "well…the grass is really green, it’s like miles and miles of it…"

        scene mind 2
        play sound "audio/wave_ocean.mp3"
        f "there’s a couple of rivers/lakes that run across it. beautiful and calm."

        scene mind 3
        f "The sky is a solid baby blue, there’s a couple of clouds up in the sky but not too many, just enough"
        p smiling"That's nice. Tell me more.."
        
        scene mind 4
        f "And if you look closely you can see a few mountains peeking behind a cluster of trees. It’s extraordinary…"

        scene mind 5
        f "Oh and the flowers! they’re so beautiful. It's spring now so they’re fully bloomed and in so many different colors, they’re pink..."

        scene mind 6
        f "...yellow and even purple."
        
        p "that sounds like something straight out of a movie! Are you sure you’re not just seeing things?"
        jump after_choices

    label after_choices:
        scene black
        "The End"

return # This ends the game.
