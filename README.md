# Final-project
“Pirate Treasure Catcher” is a fast-paced arcade-style game designed as the final project for the semester. The goal is to apply all major concepts learned in class, including sprites, collisions, timers, sound effects, scenes, lists of objects, and game logic, while building a complete, fully playable game.
The player controls a pirate at the bottom of the screen and must catch falling treasure while avoiding dangerous hazards. Coins, special gems, and special gold coin award points; bombs and skulls reduce the score. Random “burst drops” of hazards add challenge and unpredictability. A countdown timer motivates the player to collect as much treasure as possible before time runs out.



This project demonstrates:

•	Managing multiple sprite types

•	Physics-style falling logic 

•	Collision detection for both rewards and penalties

•	Timer-based gameplay 

•	Sound integration for good and bad events

•	An intro scene with instructions and buttons

•	A main game loop with updated labels for score and time

•	Randomized hazard bursts for difficulty spikes

The final objective is to deliver a complete and fully playable game that functions smoothly and show’s solid programming structure.

How to Play

•	You control the pirate at the bottom of the screen.

•	Use the LEFT and RIGHT arrow keys to move.

•	Your goal is to catch falling treasure before time runs out.

•	Different objects award different amounts of points:

o	Coin → +10

o	Ametrine → +20

o	Aquamarine → +25

o	Sapphire → +30

o	Gold Coin (large) → +40

Avoid These Hazards

•	Bombs → -15 points

•	Skulls → -10 points

•	Burst Hazards: Occasionally, random “bursts” of extra bombs or skulls will fall 

•	Burst Bombs → -20 points

•	Brust Skulls → -15 points


Ending the Game

•	The game lasts 15 seconds.

•	When time reaches 0, your score is shown, and you return to the title screen.

•	You can play again to try and beat your previous score.

Sounds

•	Treasure makes a “coin” sound when caught.

•	Hazards play a “bad” sound when hit.



1. Python Programming Language
   
•	Core language used to implement all game logic

•	Variables, loops, functions, and classes

•	Object-oriented programming for sprite types (Coin, Goldcoin, Gem, Bomb, Pirate)

2. Pygame Library
 
•	Underlying engine used by SimpleGE

•	Handles graphics, collision detection, keyboard input, and sound playback

•	Used indirectly through SimpleGE wrappers

3. SimpleGE (
   
A primary part of the project, used for:

Scenes

•	Separate the Instructions scene and Game scene

•	Scene transitions using .start() and .stop()

Sprites

•	Custom sprite classes for multiple object types:

o	Coin

o	Ametrine

o	Aquamarine

o	Sapphire

o	Goldcoin

o	Bomb

o	Skull

o	Pirate

Labels Elements

•	Label for score

•	Label for time

•	MultiLabel for instructions

•	Button for Play/Quit

Timers

•	Game countdown timer 

Sound System

•	simpleGE.Sound() used for:

o	Coin / treasure sounds

o	Bad hazard sound

4. Game Mechanics & Techniques

Falling Object Management

•	Random X-position generation

•	Randomized falling speeds 

•	Resetting objects using checkBounds()

•	Lists to manage multiple falling items

Collision Detection

•	sprite.collidesWith(self.pirate) to determine:

o	Points earned

o	Penalties

o	Sound effects

o	Object resets

Randomization

•	Random falling speeds

•	Random reset positions

•	Random hazard bursts (2–5 bombs/skulls at once)

•	Random hazard type (“bombs”, “skulls”, or “both”)

5. Score & Time Tracking
   
•	Automatic score updates

•	Time-left display

•	Score never allowed to go below zero

•	Game ends when the timer reaches zero

6. Input Handling
   
•	Keyboard input for pirate movement (LEFT/RIGHT)

•	Future support for on-screen click controls

•	Boundary checking to keep the pirate on screen

7. Sound Integration
    
•	Playback of multiple sounds depending on the event

•	Good sounds for treasure

•	Bad sounds for hazards

•	Prize sound for special gold coin

8. User Interface
    
•	Clear instruction screen

•	Play and Quit buttons

•	Last score displayed on instruction screen

•	Clean score/time HUD during gameplay

9. Graphics & Assets
    
•	Custom PNG images for:

o	Pirate

o	Ship background

o	Each gem and treasure

o	Bombs and skulls

•	Transparent PNGs for better visual layering

•	Simple game theme consistent with a pirate treasure hunt

10. Game Loop Architecture
    
•	Main loop calling scene transitions

•	Separate process() functions for logic updates

•	Clean division between the instruction screen and gameplay

Citations for any external resources you used
OpenGameArt.org
The project uses several graphics and sound effects that were legally obtained from OpenGameArt.org, a public domain / Creative Commons asset library used widely in game development.

Specifically:

•	Sound Effect:

Win Sound Effect

Source: https://opengameart.org/content/win-sound-effect

Used for: bombs and skulls

•	Graphics & Icons:

Various project sprites (pirate, bomb, skull, treasure icons, gems, goldcoin) were inspired by or derived from publicly available art packs on OpenGameArt, ensuring appropriate licensing and free academic use.



What I Learned

Throughout this project, I learned how to combine everything from the semester into one complete, functioning game. I gained experience with:

•	Managing multiple sprite classes at once

•	Using lists of objects (coins, goldcoin, gems, bombs, skulls)

•	Collision detection between many different sprite types

•	Working with timers for gameplay duration and hazard bursts

•	Integrating sound effects for feedback

•	Structuring a multi-scene game (instructions + gameplay)

•	Debugging indentation and logic issues in a larger program

I also learned how important it is to keep my code organized when the project gets bigger. Especially using GitHub with each change.

Where I Got Stuck

I hit several challenges during the process:

•	Score label not updating because the update code was indented inside a for loop

•	Sound file errors when the file was missing or named incorrectly

•	Burst hazards caused crashes when lists were created inside the wrong loop

•	Keeping the pirate on the bottom while still allowing smooth left/right movement

•	The timer was not keeping up it keep stopping the starting back up

•	Normal indent issues

Each challenge required carefully reading the traceback and slowly checking indentation, which ended up being one of the most common sources of bugs.



What I Would Like to Improve

If I had more time, I would improve:

•	Adding on-screen arrow controls for mouse/touch users

•	More polished graphics and animations

•	A health system instead of instantly deducting score

•	A smoother transition between screens

•	Sound mixing (volume control, softer bad sound, louder treasure sound)

I would also like to add a more interesting background, achievements, and maybe moving hazards in future versions.



How I Would Do Things Differently Next Time

Next time, I would:

•	Plan the sprite classes earlier so I don’t have to rewrite them

•	Build a small version of the game first (MVP) before adding features

•	Keep the code cleaner with separate helper functions

•	Add new objects one at a time instead of several at once

•	Test each collision setup individually so debugging is easier

This would make the project smoother and reduce the amount of re-fixing I had to do.

How Far I Strayed From the Original Game Design Document

I stayed fairly close to the original idea, but I did stray in a few areas:

•	Added more gem types than originally planned

•	Added burst hazard system, which wasn’t in the first draft

•	Added a special gold coin for bigger points

•	Made the pirate move only left/right instead of all directions

•	Added different sound effects for treasure types, and then having to remove them caused way too much sound. You could not differentiate the different sounds. 

The core idea (catch treasure, avoid hazards) stayed the same, but I expanded the game as I learned more.



How I Stayed on Track

I stayed on track by:

•	Breaking the project into small pieces

•	Adding one object type at a time (coin → goldcoin → gems → hazards → burst hazards)

•	Testing constantly after each change

•	Using print statements and simple checks to debug

•	Keeping my goal in mind: make a complete, playable, fun game


This step-by-step approach made the entire project manageable.
