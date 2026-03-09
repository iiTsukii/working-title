init:
    $ c = Character("Claudia", color=(250, 203, 252))

init:
    $ s = Character("Sienna", color=(203, 252, 211))

init:
    $ a = Character("Ashlynn", color=(180, 216, 255))

init:
    $ n = Character("Nila", color=(198, 180, 255))

init:
    $ cr = Character("Christine", color=(126, 9, 36, 255))

default start = False

default scienceone = False

default englishone = False

default artone  = False

default enjoyart = False

default noenjoyart = False

default normalclay = False

default notnormalclay = False

default continueart = False

default phoneleft = False

default phonetaken = False

default lunch = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hallway

    "Miss Peak" "Are you Schwa?"

    "Schwa" "Yeah?"

    "Miss Peak" "Okay, Well, I’m Miss Peak, the vice principal."

    "Miss Peak" "I’m sure your teachers will go over all the school values and all that with you."

    "Schwa" "Yes, I was wondering who my teachers are since I never actually got a timetable."

    "Miss Peak" "Yeah I don’t really care."

    "Schwa" "What?"

    "Miss Peak" "I have things to do."

    "Schwa" "I don’t know- where to go?"

    "Miss Peak" "Can you not raise your voice at me, thank you?"

    "Miss Peak" "I don't get paid to care about your problems okay? Goodbye."

    "Miss Peak turns around and struts out, leaving me very confused."

    "I should really just go home now, school sucks anyway."

    "???" "Hey, are you alright?"

    "Woah! Who’s this mega hot girl?"

    "Maybe school doesn’t suck. Heh."

    "Schwa" "Hey- Yeah, I mean it’s my first day of school and I’m already getting screwed over."

    "Christine" "That sucks, yeah Miss Peak is not the best."

    "Christine" "I didn’t know we had a new student, let alone such a handsome one..."

    "Christine is super hot, and super into me. Score."


    Girl 1 "It’s the new guy!"

    Girl 2 "He’s so hot!"

    Girl 3 "And nonchalant!"

    "Schwa" "Ladies, Ladies, I’m very busy here with one special girl."

    Girl 1 "Of course!"

    Girl 2 "See you in class tiger, rawrr."

    "Normaly I would’ve jumped right at those girls, but right now my vision is occupied."

    "Christine" "Hey if you don’t know where your classes are I could totally help you out!"

    "She’s basically begging for me to ask for her number at this point."

    "Schwa" "That would be fantastic."

    "Christine bites her lip and glances up at me."

    "Christine" "What class did you want to try out first?"

    menu:

        "English":
            jump englishone

        "Science":
            jump scienceone

        "Art":
            jump artone

label englishone:
    #  anyone can start writing this
label scienceone:
    #  anyone can start writing this
label artone:
    #  anyone can continue writing this
    "Christine" "Awesome, Art’s in the east building, I can show some stuff to you on the way too."

    "Christine slips her small, soft hand over mine and leads me out of the hallway."

    "Christine" "I’m not very good at art but I do really enjoy it."

    "Christine" "Do you like art, Schwa?"

    menu:

        "Yes":
            jump enjoyart
            
        "No":
            jump noenjoyart

label enjoyart: 
    "Christine" "That’s really nice, hey…"

    "Christine" "Maybe I could do modeling for you sometime."

    "Christine runs her hand down her thigh and I can’t help but to follow with my eyes."

    jump continueartone

label noenjoyart:     
    
    "Christine" "You know you didn’t have to choose art."
            
    "Christine" "I hope you’ll still have fun with me though."

    jump continueartone

label continueartone:
        
    "Christine" "Our homerooms are up in the north building, I guess you could just join with mine tomorrow morning."

    "Christine stops outside a red brick building and lets go of my hand to knock on the door."

    "A (describe teacher here) Opens up the door and beams upon seeing Christine."

    "???" "Christine! I was worried you weren’t going to be here today."

    "Christine" "Sorry miss, I’ve just been helping out our new student Schwa"

    "Schwa" "Hey what’s good bro."

    "???" "Oh I’m sorry Schwa, I don’t seem to have you on my roll for this class"

    "Christine" "We’re manifesting Schwa being in art class."

    "Schwa" "Cause I didn’t really get a timetable or whatever."

    "???" "Well, the more the merrier!"

    "Christine" "Oh! Are we doing clay today?"

    "???" "We are! Come right in."

    "Christine and I enter into the art room"

    "???" "Hey bitch"

    "Christine" "Hey Selena."

    "Selena" "Woah who’s this?"

    "Schwa" "Heyyy what’s up, I’m Schwa."

    "Selena" "Why don’t you two sit with us?"

    "Selena motions to her 6 seater table where a girl and a guy are already sitting."

    "Christine" "Thanks, but you better lay off Schwa."

    "What."

    "Selena licks her lips and starts looking me up and down."

    "Schwa" "Uh- I- uh I can’t no read good, so we should sit closer to the board."

    "It scares me when girls are too into me, like I get it ladies but let me do the work."

    "Christine" "Oh we can totally sit near the board."

    "Selena" "Yeah… I guess you can."

    "Christine and I go to sit at the front of class where I can now see what I assume to be the teachers name, Pablo Picasso."

    "Christine" "I got aprons, let me tie yours up for you!"

    "Christine takes her hand around my large, and manly 50 inch waist."

    "I go to her back to tie up her apron."

    "???" "Allow me m’lady."

    "Before I can even touch her back some guys zips behind her and ties up her apron."

    "Christine" "..."

    "Christine" "Thanks Dante…"

    "Dante" "Ah, always a pleasure to serve, now make sure to keep that up tight."

    "Dante tips an imaginary hat to Christine and reaches out his hand to me."

    "Dante" "Dab me up bro."

    "I stare at him."

    "Dante" "Not to worry, I know there are those out there with Hand and mind disabilities."

    "Dante saunters away as he takes a puff from his vape, the strawberry flavour filling the room causing multiple small children to start coughing."

    "Christine" "Dante’s really something"

    "Christine looks up at me smiling as she subtly undoes the back of her apron."

    "Christine" "Oh Schwa… my apron seems to have gotten loose, do you reckon you could help?"

    # super sexy cutscene of her back 

    "Mrs Picasso" "Okay class! Welcome back to school, if you don’t know who I am, I’m…"

    "Blah, Blah, Blah, yeah I’m not listening to all that."

    "Christine gets up to grab something and comes back with a big bag of brown… muck?"

    "Christine" "Oh Schwa! I love clay!"

    "Christine hands me a lump from the bag."

    "Christine" "What do you think you’ll make Schwa?"

    menu:

        "A dog":
            jump normalclay
            
        "My peenar":
            jump notnormalclay

        "A bowl":
            jump normalclay
            
        "A flower":
            jump normalclay

label normalclay:

    "Christine" "That’s really nice Schwa."

    "Christine" "Would’ve been funnier if you made a penis though."

    "Dammit she’s right."

    jump continueart

label notnormalclay:

    "Schwa" "Yeah I’m gonna make my Peenar"

    "Christine" "What? What is that- Use your big boy words Schwa."

    "Schwa" "... My Penis."

    "Christine" "Oh yeah! That would’ve been funny but cause you explained it it’s not."

    "Dammit she’s right."

    jump continueart

label continueart:

        # sort of want to add a minigame where you just tap the clay with a mouse to shape it

    "Christine" "Well I finished what I made if you want to see it."

    "I nod in agreement."

    "Christine holds out her new creation in her hands." # still image / cutscene of this

    "Schwa" "It’s me!"

    "Christine" "Oh I’m so glad you could tell, like I said I’m not great at art."

    "Schwa" "Christine! That looks exactly like me. #end cutscene

    "Christine" "You’re far too nice."

    "Christine" "And cool and funny and…"

    "Christine" "Hey, do you think you could grab a carving tool from Selena’s table for me?"

    "I get up to cross the classroom and look back at Christine to see the look in her eyes…"

    "That look means I’m totally gonna get banged."

    "Selena" "Heyyyy"

    "Schwa" "Nah, just give me the carving tool."

    "As I wait for Selena to find where she put the tool I spot a phone sticking out of a bag at their table."

    "The guy from before is gone, whose phone I’m assuming it is."

    "It’s just all so tempting, I mean I’ve gotta use it."

    "Or maybe this is like undertale where I gotta do all the good stuff+"

    menu:
        
        "Take the phone":
            jump phonetaken

        "Don’t take the phone":
            jump phoneleft

label phonetaken:

    "I nonchalantly reach down into the bag to grab out the phone."

    "Of course the passwords 6967, pretty awesome password."

    "I’m in the phone so right away I,"

    #could code in the menu being the apps on the phone screen


label phoneleft:

    "I decide to not take the phone, there’s probably nothing good that will come out of it anyway."

    "I grab the carving tool as Selena hands it to me and head back to Christine."

    "Christine" "Hey schwa! While you weren't here we got invited to a murder mystery party!"

    "Schwa" "wow that sounds fun! When is it?"

    "Christine" "Tonight after school, I really hope you come."

    "Schwa" "yeah of course, anything for you christine!"

    "Gee golly I really hope I get laid at this party" 

    "Ding Dong Bing Bong"

    "Christine" "That's the bell, it's time for lunch!"

    jump lunch

label lunch:

    "Instead of heading home I head straight to the party with Christine"

    "Christine" "Im so excited for this party shwa!" 

    "Christine" "oh by the way I got us outfits!"

    "We stop at the school bathrooms before leaving and Christine goes in to change."

    "Christine comes out wearing a sleek black dress"

    "Christine" "how do I Look?"

    "Schwa" "Great!" 

    "Let me hit pls pls pls"

    "Christine blushes and looks shy"

    "Christine" "oh wait! I almost forgot to give you your outfit!"

    "She takes out a detective outfit from her bag."

    "Christine" "here! You're the detective so I thought this might look nice."







    return

    # blahblahblah