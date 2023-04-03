# Backrooms – Doomsday
## Summary
Backrooms – Doomsday is a 2.5D first person maze game made with Pygame. Its movement and display style similar to that of the original Doom and Wolfenstein. The goal of the game is to find the hidden end of the maze as quick as possible. If the timer hits zero, you die!

## How to Play
In order to move use the “WASD” keys (to move forward, left, back, and right respectively) and the arrow keys (left and right) to turn.

## Design
### Main
The “main” file stitches all the game logic together, from the screen state to the enemy movement, it handles all the core game functionality. These are the files “main” pulls from (with brief descriptions).

This file handles two core tasks:
1. Transitions from start, playing, and end screens
2. Detection of key presses and game events

### Screen Manager
One of the files, “game_screen”, handle the drawing and display of the different states of the game (start, playing, and end screens). With its tie into the “main”, the displayed screen will change based on what button is clicked or what key is pressed. For example, on the start screen, clicking the “start” button will change the game into playing mode. The same is true from playing to end screens and end screen to exit.

### Player
The user logic is handled by the “player” file. This involves movement controls, wall collisions, and image updating (for the surrounding map).
  
### Map
In order to have a playable area, the “map” file instantiates a 2D array for the map area. This enables a challenging maze environment.
### Constants
For the 2.5D logic to work many global constants are needed. This allows for the trigonometric drawing of tiles in the environment, based on the sightline of the player.
