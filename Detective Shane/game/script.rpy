# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Shane", color="#FFFF00")
define sv = Character("Shane (V.O)", color="#FFCC00")
define a = Character("Andre", color="#FF0000")
define av = Character("Andre (V.O)", color="#FF5353")
define m = Character("Mom", color="#33CCFF")
define d = Character("Dad", color="#33CC00")
define y = Character("Yoko", color="#FF0099")

image dad normal = im.Scale("sprites/dad/dad normal.png", 550, 1050)
image dad shocked = im.Scale("sprites/dad/dad shocked.png", 550, 1000)
image dad angry = im.Scale("sprites/dad/dad angry.png", 550, 1000)

image yoko normal = im.Scale("sprites/yoko/yoko normal.png", 700, 1150)
image yoko happy = im.Scale("sprites/yoko/yoko happy.png", 700, 1150)
image yoko very happy = im.Scale("sprites/yoko/yoko very happy.png", 700, 1150)
image yoko angry = im.Scale("sprites/yoko/yoko happy.png", 700, 1150)



# The game starts here.

label start:

    scene bg car seat
    "The car is moving on the road."
    show shane normal
    "Shane is looking out the window."
    
    "Trees and grass are whooshing past."
    "Houses are coated in different colours as Dad drives past them."

    scene bg car seat
    show mom normal at left
    m "How are you guys doing back there?"
    show andre normal at right
    a "I think we're doing alright."
    a "Right, Shane?"

    "Andre looks over to Shane."
    "Shane looks away from the window and joins the conversation."

    show shane normal
    s "Hm?... Oh yeah, we're doing fine."

    "Shane looks back out the window with his hand against his cheek and his elbow resting on the side of the window."

    sv "Andre is my little brother. He is chill and sometimes has to care for me."
    sv "I work too hard sometimes since I have a secret power nobody knows about and I am always involved in cases I don't want to do in some situations."
    sv "I could... sense things. I always push myself to find the core of a situation."
    sv "He has to stop me most of the time and I keep overthinking which makes me think nothing really helps anymore."
    sv "This is why we are moving to this new house."

    "Mom whispers over to Dad"

    m "I don't think they are ready for this move."
    d "Yes, they are. We couldn't stay in that old house."
    d "It contained too many memories and Shane went mentally insane sometimes."
    m "I guess you're right. Fresh starts are good for us."

    "Mom guiltily smiles."

    scene bg driveway day with fade
    show shane normal at left
    show andre normal at right
    show mom normal
    show dad normal

    d "Alright, everyone! We're here!"

    s "I don't want to be here. Why did we have to move?"

    m "It was the best for all of us. Fresh start anyways."

    "Dad opens the trunk to get all of the luggage out."

    d "Okay, everybody grab their luggage and move it to the door to unpack more."

    "Shane, Andre, Mom, and Dad get their luggage out from the trunk and roll it to the door."

    "Dad stares at the house as he closes the trunk."

    m "Nice home, isn't it?"

    "Dad closes the trunk."

    "Shane walks back on the driveway right after."

    sv "This house has some weird vibe to it."
    sv "Something is definitely wrong. It feels so creepy."
    sv "I might turn this into a case now."

    "Shane looks around as he sees the street is empty besides that house."

    scene bg house groundfloor with fade
    show shane normal at left
    show andre normal at right
    show mom normal
    show dad normal

    "Shane, Andre, Mom, and Dad look around the house as they stand near the door once they walk in."

    a "Woah! This is so cool!"

    show shane disgusted
    sv "Hmm... interesting house..."

    m "Wow! This is a comfy place."

    s "Don't any of you feel this eerie feeling of the house?"

    m "No?"

    a "No, I don't think so. Why?"

    s "It just... feels weird."

    d "Try to get it off your shoulders, Shane. Get comfortable. Maybe after that, you will feel better."

    s "Maybe you're right. I'm gonna go pick a room upstairs and lie down."

    "Shane goes upstairs to rest."

    scene bg shane room day with fade
    show shane tired

    s "Ughhh. I'm bored."

    show andre normal at right
    a "Hey, Shane! Want to play a board game with us?"

    s "Maybe later. I still don't feel my best."

    a "Alright, fine with me."

    "Andre proceeds to leave Shane's room when Shane sees this faint, white, almost transparent figure right next to Andre as he exits."

    show shane shocked
    s "Wait! Andre!"

    show andre confused
    a "What's up?"

    "The feeling suddenly disappears when he is aware of the almost transparent figure."

    s "Nevermind. I'll be down later."

    hide andre
    a "Okay."

    "Andre exits Shane's room and Shane puts his palm to his forehead with a confused expression."

    sv "What was that? It was like something was lurking here."

    scene bg house groundfloor
    show shane tired

    "Shane is quiet while walking down the stairs and has his hand on his head due to his slight headache."

    show andre normal at right
    a "Shane! Come join us!"

    show mom normal
    m "Are you feeling better?"

    s "Yeah, just a little."

    show dad normal
    d "That's great. Come, now. We are playing this board game called clue."

    s "Clue?"

    a "Yeah! The objective of the game is to find out who the murderer is. We thought it would be a fun game since you are kind of an investigator yourself."

    s "Well, glad you guys thought of me when playing this game. Ahaha... I'm just going to go back upstairs since I have a headache and I don't feel well."

    a "Okay, get better soon!"

    scene bg shane room night
    show shane thinking

    sv "That feeling earlier... was it real?"
    sv "You know what? I'm just gonna ignore it. I've been paranoid about this house for a while."

    s "Cmon! Pick up!"

    y "Hello?"

    s "Hi, Yoko. Hear me out-"

    y "Shane, I told you this already. We broke up so long ago and you can't just keep calling me like this. I'm going to hang up now."

    s "Yoko, wait! Let me facetime you for just 5 minutes. Please."

    y "Shane, I know you are mentally ill. I can't deal with you right now. I have my own things to deal with."

    s "Yoko... please..."

    y "Fine. You have 2 minutes."

    s "Thank you."

    "Shane opens Facetime and dials Yoko."

    s "Alright, hear me out."

    y "Shane, stop pranking me."

    s "What?"

    y "Stop it right now. Turn it off."

    s "Turn what off? Are you good?"

    y "Turn off the simulation. Now!"

    s "What are you talking about? There is no simulation."

    y "Then what was that behind you?"

    "Shane turns around and nothing is there."

    s "What? Bro I swear, right now is not the time to prank me. I only have two minutes with you."

    y "I am not going delusional, Shane. I'm not pranking you either. Something was behind you."

    s "You're joking. Was it like a ghost?"

    y "Maybe."

    s "There was this feeling something was following Andre earlier. Maybe that was the figure you saw on my screen."

    y "What the hell, Shane? Stop playing with me. I'm done."

    s "Bro, you are actually lying to me right now. Stop."

    "Yoko hangs up."

    s "There is no way she just hung up on me."

    show andre normal at right
    a "Shane, dinner is almost ready. Come down."

    s "Okay, I'll be right down."

    hide andre

    scene bg dining table
    show andre normal at right
    a "Hey, Shane!"

    show shane normal at left
    s "Hi, Andre."

    show dad normal
    d "Do you feel better?"

    s "Yeah, I guess. There have been many incidents where I have felt unsafe like there is a ghost living in this home."

    show mom concerned
    m "That's nonsense. This house is perfectly safe."

    s "Not from what I've experienced."

    a "What experiences have you had?"

    d "Wait a minute. Shane might be going delusional again."

    s "What?"

    m "Shane, do you need your medicine again?"

    s "What? You are calling me the delusional one?"

    a "Are you okay?"

    show shane angry
    s "Woah, woah, woah. What is wrong with you guys? You sound like I'm the bad guy here. I am not going crazy."

    d "I think you should give him his medicine."

    s "What? No, no, no. I am fine. You guys are not being serious right now."

    m "Calm down. We are just trying to help you."

    s "You can't help me. Why can't you guys think of me as a normal human being anymore? I'm done."

    hide shane

    scene bg upstairs hallway night
    "Shane dashes upstairs."

    a "Did we hurt Shane's feelings?"

    d "I think he just needs time alone."

    scene bg shane room night
    show shane crying

    s "Why can't they think of me the same as when I was a kid?"

    "Shane starts to cry."

    hide shane

    show andre normal at right
    "Andre comes into Shane's room and sees Shane already asleep."

    "Andre walks over and sees tears almost dried."

    a "I hope you feel better soon. Goodnight."

    hide andre

    scene bg andre room night
    show andre thinking

    av "Shane thinks he can do so many things to impress himself but ends up hurting himself even more."
    av "Even though he spent years in a mental hospital, he still acts weird."
    av "He keeps thinking about the things from the past that he is traumatized about and tries to find the main reason why they happened so he becomes the detective he is to get his answers."
    av "Especially... the death of his girlfriend, Yoko."

    hide andre

    scene bg shane room day
    show shane tired

    s "Damn, did I really sleep while crying last night?"

    scene bg upstairs hallway day
    show shane normal

    s "It's only 8:03am?"

    s "So, am I the only one awake?"

    scene bg andre room day
    show shane normal at left
    show andre asleep at right

    s "Andre, are you awake?"

    "No response."

    "Shane slowly walks out."

    show shane shocked

    sv "What the hell? What is this feeling that is stopping me from exiting this room?"

    "Shane looks back to see a figure vaguely, quickly disappearing."

    s "What the hell?!"

    show andre startled
    a "Shane? What's going on?"

    s "I don't want to be here anymore."

    show andre concerned
    a "Calm down, Shane. You are just paranoid. Let's go downstairs together."

    s "No. I don't believe you. You guys think I'm delusional and don't know what I'm talking about."
    s "I'm going to search this house and find out why I keep feeling this ghost lurking around."

    a "I never said you were delusional. Shane, I'm here for you."
    a "I'm not going to stop you from searching the house but I think you should calm down a bit."

    s "Just leave me alone for now."

    hide shane

    scene bg shane room day
    show shane distressed

    "Shane slams his door and slides down with his back facing it."

    s "I am not going crazy."

    scene bg black
    "Begin Flashback:"

    scene bg park fountain day
    show shane happy at left
    show yoko happy at right

    "Shane holds Yoko's hand as he drags her with a smile on both their faces."

    s "Hahaha, come!"

    y "You are so silly, Shane."

    s "Okay, here is the spot I wanted to show you."

    "Shane decorates the fountain and Yoko's face lights up."

    y "Shane, this is beautiful!"

    "Yoko's face lights up as Shane smiles."

    s "I'm glad you like it. I also bought your favorite foods."

    y "Shane, you shouldn't have!"

    s "I love you so much, Yoko. Of course I would do all of this for you!"

    y "I love you!"

    "Shane and Yoko kiss with happiness."

    scene bg black
    "End Flashback:"

    show shane crying

    s "I miss her so much. That one night... that one night changed everything."

    scene bg black
    "Begin Flashback:"

    scene bg street night
    show shane crying at left
    show yoko dying at right

    "Shane is on his knees while looking at Yoko laying on his lap with blood all over her."

    s "You're going to be okay, Yoko. Please, don't leave me. I'm sorry."

    y "Live on... for me."

    "Shane is currently sobbing."

    s "No! Yoko! Don't give up! Live on with me! You can still survive! Somebody get an ambulance!"

    "Yoko stops moving in Shane's arms."

    s "Nooo! Yoko!! Wake up!! Please!"

    "Yoko makes no response as she lays dead at the scene."

    "Shane screams out Yoko's name in the street they are on."

    scene bg black
    "End Flashback:"

    scene bg shane room day
    show shane crying

    s "It was all because of that one night. That person who stabbed Yoko and ran off."
    s "I was too late to save her and nobody was around that night, or so I thought."
    s "I went mentally insane after that."

    "Shane buries his face in his arms to cry harder."

    sv "My whole family agreed to send me to a mental hospital where I thought about Yoko everyday."

    s "Is this why I keep thinking she is still alive?"
    s "Because I blame myself? I feel guilty for not saving her?"
    s "I miss her so much."
    s "I loved her a ton and since she is gone, I couldn't take the impact and got mentally ill."
    s "What is wrong with me?"

    "Shane turns and lays on the floor."

    s "This is why we moved. It was because of me."

    sv "I still didn't search the house."
    sv "Wait... the ghost."
    sv "Is that Yoko?"
    sv "Is Yoko following me wherever I go?"
    sv "She still loves me?"

    "Shane decides to search the house."

    scene bg shane room closet
    show shane normal

    s "Hello? Anybody in here?"

    "No response happens."

    scene bg mom dad room day
    show shane normal

    s "Are you here?"

    "The room is still silent so Shane explores more."

    scene bg andre room day
    show shane normal at left
    show andre normal at right

    s "Yoko? You here?"

    a "Everything okay?"

    s "Yeah, just searching."

    "Andre still looks concerned when watching Shane roam around his room."

    a "Mmm... okay."

    scene bg livingroom day
    show shane sad

    s "I can't find out why this house has this eerie feeling. I'm just gonna go downstairs."

    show andre normal at right
    a "Okay."

    s "Maybe I really am just paranoid."

    "Shane shakes his head as if he were to clear his mind."

    "Shane starts to look depressed until Andre comes down a few minutes later."

    a "Shane? What's up?"

    s "I can't stop thinking about what has been happening."

    a "Hey, hey, hey. It's okay. I know who you're thinking about and it's okay."

    s "I miss her."

    a "I know you do."

    "Andre hugs Shane with a semi-sad face."

    a "Do you want to trigger a memory that happened about 4 years ago?"
    a "It might take your mind off of her."

    s "I mean, I guess you can try."

    a "Okay so basically, when I was 10 and you were 16, we went to Disney World."
    a "I don't know how I still remember this but do you remember that one day where we went to this one park called um... Funland's Frenzy."

    s "Vaguely, I remember."

    a "Do you remember that one ride that we passed and you got so scared?"

    "Andre and Shane start laughing so hard."

    s "Yeah, I do remember that!"

    a "Hahaha! Dude, you looked so stupid!"

    s "Yeah, yeah, sure. You wish you were as smart as me!"

    "Shane rubs Andre's head with laughter."

    a "Hey! I am smart!"

    s "Yeah, yeah, you wish!"

    "Shane and Andre talk for a few hours and share the memories they have had in the past."

    s "(voice fading) Oh, and do you remember this one time where..."

    scene bg mom dad room day
    show dad angry at right
    show mom angry at left

    d "Do you know what you could've done?"

    m "You can not blame this on me! This is my fault as much as it is yours."

    d "I was not the one who killed Yoko."

    m "Are you sure? You literally sound like you did."

    d "Why are you blaming me for Yoko's death?"

    m "Yoko's death made our son into a psychopath."
    m "He cried for days and kept pretending she was still alive."

    d "And that's my fault?"

    m "You were there at the scene when you were coming home."

    d "So you think I would kill our son's girlfriend?"

    m "You never really liked her."

    d "I just wanted her to treat him better."

    m "So you admit you killed her?"

    show shane shocked at center

    s "Dad... you killed Yoko?"

    "Mom and Dad turn to see that Shane ran up to their room to ask them a question and eavesdropped by accident."

    "Mom and Dad have a shocked face and can't even talk."

    d "Shane... I- I would never..."

    s "I don't want to hear it anymore."

    scene bg house groundfloor
    "Shane runs down the hallway and down the stairs to exit the house."

    s "How could you do this to me?"

    scene bg mom dad room afternoon
    show dad angry at right
    show mom neutral at left

    d "Look what you've done! Now my son thinks I am a killer, especially the killer of his own girlfriend when I'm not."

    m "I don't have anything to say to you."

    "Mom walks out the room."

    d "Serena... wait!"