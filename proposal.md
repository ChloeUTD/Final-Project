# Title

## Repository
<https://github.com/ChloeUTD/Final-Project.git>

## Description
Infinite auto runner where you must avoid obstacles by either jumping, sliding, or attacking. 
Combines art and code to make a playable and visually appealing game

## Features
- Random Obstacle Generation
	- Add obstacles to a list, every given interval a random object will be selected 
    and generate. Interval is shortened the longer you play
- Animated characters
	- Create a function that splits sprite sheets and returns animation that changes
    based upon framerate given to function
- Auto "Running"
	- Have obstacles slide towards the player while running animation is playing. Player
    only moves vertically, but the animation gives the illusion of moving

## Challenges
- Creating a function that can dynamically split spritesheets into different frames
- Managing lists of objects that need to be deleted, especially once the level gets faster
- Working with hitboxes so the timing of player input does not feel to easy or hard

## Outcomes
Ideal Outcome:
- The basic features are implemented, and I get extra time to add animations for 
when the player destroys the obstacles. 

Minimal Viable Outcome:
- The game responds to user input so that it is able to function

## Milestones

- Week 1
  1. Implement obstacle class + handling
  2. Implement User input

- Week 2
  1. Implement animation function
  2. Implement distance counter

- Week N (Final)
  1. Implement obstacle destruction animation
  2. Implement menu screen