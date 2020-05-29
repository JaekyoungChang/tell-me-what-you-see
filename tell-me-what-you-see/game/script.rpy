# The script of the game goes in this file.

define b = Character("choice_name", image="boy", dynamic=True)
define g = Character("choice_name", image="girl", dynamic=True)
define bb = Character("choice_name", image="b-before", dynamic=True)
define gb = Character("choice_name", image="g-before", dynamic=True)
define f = Character("Father", image="father")
define hm = Character("Heart Monitor", image="heartmonitor")
define v6 = Character("Visual Six")

label start:
    
    scene room with dissolve
    play music "audio/memories_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
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
                 "You didn't type a name! You can go back and try again, otherwise we can name the character 'Jane Doe' for you!"
                 $ choice_name = "Jane Doe"
            $ p = g # This fixes the side image problem
            jump hospital_scene_1
            
        "Boy":
            hide girl with dissolve
            show boy before pose 1 at center with move
            $ choice_gender = "boy"
            $ choice_name = renpy.input("Choose your character's name!")
            if choice_name == "":
                 "You didn't type a name! You can go back and try again, otherwise we can name the character 'John Doe' for you!"
                 $ choice_name = "John Doe"
            $ p = b # This fixes the side image problem
            jump hospital_scene_1
            

label hospital_scene_1:
    
    $ renpy.music.set_volume(0.3, 0, channel="music")
    play music "audio/Art Of Silence_V2.mp3" fadeout 1.0 fadein 1.0
            
    scene black with fade
    
    play sound "audio/heartbeat_fast.mp3"
    p after "Am I awake? Am I alive?"
    p "Where am I? What happened to me?"
    p "It’s so dark, why is it so dark?"
    
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1, 0.5, channel="music")
    
    scene room closed with wipeleft
    
    if choice_gender == "girl":
        show girl hospital screaming at left with easeinleft
    else:
        show boy hospital screaming at left with easeinleft
    
    p "Dad!! Daddy!! Are you here?"
    play sound "audio/footsteps.mp3"
    show father standing at center with easeinright  
    if choice_gender == "girl":
        show girl hospital sad with move
    else:
        show boy hospital sad with move
    
    stop sound
    f "I’m here, %(choice_name)s.. I’m here sweetheart"
    f "You’re okay, it’s going to be okay."
    p "What happened to me? Where am I?"        
    f "You are at the hospital, sweetheart"
    p "I can feel the bandages on my eyes, why can't i see?"
    f  armcross right "I don't know, Do you remember anything?"
    
    menu:
        "Does %(choice_name)s remember what happened?"
        
        "No, %(choice_name)s doesn't remember":
            p "No dad, I don’t."
            jump window_scene
                
        "Yes, %(choice_name)s remembers":
            p "I think so..."
            jump flashback_scene_1
           
           
label flashback_scene_1:
    
    play music "audio/bensound-slowmotion.mp3" fadeout 1.0 fadein 1.0
    
    p "It was a beautiful day; the sun was shining brightly and..."
       
    menu:
        "What happened to %(choice_name)s?"
        
        "Fell in the lake":
            scene lake before with squares
            $ flashback = "fall"
            play sound "audio/splash.mp3"
            
            if choice_gender == "girl":
                show girl before pose 1 at center with easeinright
            else:
                show boy before pose 1 at center with easeinright
            show jimmy at right
            with dissolve 
            
            p "...the lake was beckoning, it was so hot we were just dying to jump in the water."
            p "The fish were splashing and bobbing around, relieved to be out of the sticky hot air."
            f "Are you sure the fish were splashing around?"
            stop sound fadeout 1.0
            p "Pretty sure, why do you ask?"
            f "Ah, no reason, please go on..."
            scene lake with dissolve
            p "I climbed up onto a big old gum tree and walked out on the biggest branch hanging over the lake."
            play sound "audio/light_wind.mp3"
            $ renpy.music.set_volume(0.3, 0, channel="music")
            p "I looked up and noticed dark storm clouds moving over us." #Need to change image: kid is scared
            p "They came so quickly and the wind got so strong and it felt so angry." 
            stop sound fadeout 1.0
            play sound "audio/medium-wind.mp3"
            p "I grabbed a notch on the branch and held it tightly." 
            play sound "audio/thunder.mp3"
            show jimmy scared
            p "I could hear thunder rolling in and started to feel like i was in danger."
            p "I couldn't get back in, I couldn't let go, I started to panic and shake..."
            stop sound fadeout 1.0
            $ renpy.music.set_volume(1, 0.5, channel="music")
                                                
            jump hospital_scene_2
        
        "A nuclear power plant accident":
            scene power plant with squares
            $ flashback = "accident"
            play sound "audio/bird1.wav"
            
            if choice_gender == "girl":
                show girl before pose 1 at center with easeinright
            else:
                show boy before pose 1 at center with easeinright
            show jimmy at right
            with dissolve 
            
            p "...the grass was long and tickling my knees and I think I heard the bird chirping, though It was far away...Hmmm"
            f "A bird? Are you sure?"
            stop sound fadeout 1.0
            p "pretty sure...Why do you ask?"
            f "Oh, ah, no reason, please go on..."
            p "We were walking past the old nuclear power plant, then we went inside the fence."
            p "I am not sure how or why we went inside, but I was scared." #Need to change image: kid is scared
            play sound "audio/can_kick.mp3"
            p "Jimmy was kicking an old can along the ground, he was not afraid." 
            p "I felt my legs shaking, something was wrong in there..."
            jump hospital_scene_2
          
          
label hospital_scene_2:
    
    scene room closed with dissolve
    
    if choice_gender == "girl":
        show girl hospital screaming at left with easeinleft
    else:
        show boy hospital screaming at left with easeinleft
    with dissolve  

    show father armcross right at center with easeinright

    stop music fadeout 1.0
    $ renpy.music.set_volume(0.6, 0.5, channel="sound2")
    play sound "audio/heartbeat_fast.mp3"
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
    jump flashback_scene_2
    
    
label flashback_scene_2:
    
        if flashback == "fall":
            
            scene lake after with dissolve
            
            play music "audio/life_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
            $ renpy.music.set_volume(0.3, 0.5, channel="music")
            play sound "audio/thunderstorm.mp3"
            p "There was a loud crack, I saw sparks and a flash of light."     
            p "The branch started moving and swaying."
            
            menu:
             "Does %(choice_name)s hold on to the branch?"
             "No, %(choice_name)s doesn't":
                
              p "I quickly let go of the branch and jumped to the bank."
              play sound "audio/running.mp3"
              p "We ran as fast as we could, Jimmy was faster than me,"
              p "I was trying to keep up but I couldn't"
              p "I was losing my breath, the thunder was so loud, it was starting to rain."
              play sound "audio/thunderstorm.mp3"

              p "I felt my feet slip on the muddy track.."
              scene black with dissolve
              jump wakeup_scene
                
             "Yes, %(choice_name)s does":
                     
              play sound "audio/wood_crack.mp3"
              p "Oh no I think it's falling, I think I'm falling.."
              show jimmy scared
              p "I felt the breeze through my hair and in my face."
              stop sound fadeout 1.0
              scene underwater with fade
              stop music fadeout 1.0
              play sound "audio/falling_water.mp3"
              p "Then the coolness of the water..I'm going under, it's so calm and tranquil here..."
              play music "audio/life_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
              f "It's okay, %(choice_name)s it's all over now, it's okay!"
              stop sound fadeout 1.0
              jump hospital_scene_3
        
        elif flashback == "accident":
            
            scene power plant with irisin
            
            play music "audio/bensound-slowmotion.mp3" fadeout 1.0 fadein 1.0
            $ renpy.music.set_volume(0.3, 0.5, channel="music")
            play sound "audio/buzzing.mp3"
            p "There was a loud buzzing sound, Jimmy wanted to go closer to check it out."
            
            menu:
             "Does %(choice_name)s get closer to the power plant?"
             "Yes, %(choice_name)s does":
              p "I told him not to go...it wasn't safe...then i saw a light."
              p "It was so bright and beautiful, I couldn't look away..."
             
              stop sound fadeout 1.0
              $ renpy.music.set_volume(0.6, 0.5, channel="music")
            
              #show bright light
              scene black with fade
                
              p "Then...then, it got dark...all dark...the light is gone"
              jump hospital_scene_3
        
             "No, %(choice_name)s doesn't":
                p "I yelled out to Jimmy and told him it's too dangerous and we need to leave now!"
                play sound "audio/running.mp3"
                p "We ran as fast as we could, Jimmy was faster than me,"
                p "I was trying to keep up but I couldn't"
                play sound "audio/thunderstorm.mp3"
                p "I was losing my breath, the thunder was so loud, it was starting to rain."
                p "I felt my feet slip on the muddy track.."
                scene black with dissolve
                jump wakeup_scene
                

label hospital_scene_3:
    
    scene room closed with fade
    show father armcross right at center with dissolve
    
    if choice_gender == "girl":
        show girl hospital sad at left
    else:
        show boy hospital sad at left
    with dissolve
    
    p "Dad?"
    f "Yes, %(choice_name)s?"
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
    
    show father standing at center

    p "Is there a window in here?"
    f "Yes there is."
    p "Please dad. Tell me what you see. Don’t leave out a thing!"
    show father armcross right at center
    f "Well, um, okay"

    play music "audio/trust_by MrBusiness.mp3" fadeout 1.0 fadein 1.0
    show room open
    play sound "audio/open_window.mp3"
 
    pause
    
    scene mind 1 with dissolve
    play sound "audio/bird1.wav"
    f smiling "The sky is a solid baby blue, there's a couple of clouds up in the sky but not too may, just enough."

    scene mind 2 with dissolve
    play sound "audio/wave_ocean.mp3"
    f smiling "Well...the grass is really green, it's like miles and miles of it..."
   
    scene mind 3 with dissolve
    f smiling "There's a river that runs across it. Beautiful and calm."
    p smiling "That's nice. Tell me more."
    
    scene mind 4 with dissolve
    f smiling "And if you look closely you can see a few mountains peeking behind a cluster of trees. It's extraordinary..."
    
    scene mind 5 with dissolve
    f smiling "Oh and the flowers! they are so beautiful."
    f smiling"It's spring now so they're fully bloomed and in so many different clours, they are pink, yellow and even purple."
    p "That sounds like something straight out of a movie! Are you sure you're not just seeing things?"
    
    menu:
        "Is that what the parent really sees?"
        
        "Yes, it is":
            $ windowview = "truth"
            f smiling "That's exactly what i'm seeing, %(choice_name)s. The view is lovely"
            p "I really miss looking out the window..I took that for granted."
            p  "I would give anything just to look out the window right now.."
            jump ending
            
        "No, the parent is lying":
            $ windowview = "lie"
            f  "Nature is beautiful, %(choice_name)s"
            p "I really miss looking out the window..I took that for granted."
            p "I would give anything just to look out the window right now.."
            jump ending
            

label wakeup_scene:
    
    if choice_gender == "girl":
        $ p = gb
        scene bedroom 1 blinds with fade
        show girl wakeup screaming at right
    else:
        $ p = bb
        scene bedroom 2 blinds with fade
        show boy wakeup screaming at right
    with dissolve
    
    play sound "audio/thunderstorm.mp3"

    p "Dad, dad where are you?"
    play sound "audio/footsteps.mp3"
    show father pjs at center with dissolve # Different clothes (PJs) for parent
    f "I am here %(choice_name)s, what's wrong?" 
    
    if choice_gender == "girl":
        show girl wakeup  at right
    else:
        show boy wakeup  at right
    with dissolve
    
    # Reminder: Side images need to change here!
    p "Oh, Dad, I had the scariest dream!!"  
    p "I was in the hospital, It was dark and I couldn't see, It was awful!"    
    p "Dad, can you please open my blinds, I really need to see what is outside my window." 
    
    if choice_gender == "girl":
        scene bedroom 1  
        show father pjs at center
        show girl wakeup  at right
        
    else:
        scene bedroom 2
        show father pjs at center
        show boy wakeup  at right
    pause
    
    $ windowview = "truth"
    jump ending                                                                                      
    

label ending:
    
    if windowview == "truth":
        show windowscene pretty with dissolve
         
    elif windowview == "lie":
        scene windowscene pretty
        show screen windowscene_overlay
        pause
    
    "The End"
        
stop music

return # This ends the game.
