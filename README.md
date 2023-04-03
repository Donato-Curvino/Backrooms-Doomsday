# Backrooms – Doomsday
## Summary
Backrooms – Doomsday is a 2.5D first person evasion game made with Pygame. Its movement and display style similar to that of the original Doom and Wolfenstein. The goal of the game is to avoid the Skin-Stealer (the monster) for as long as possible. Be quick! The Skin-Stealer is not playing around.

## How to Play
In order to move use the “WASD” keys (to move forward, left, back, and right respectively) and the arrow keys (left and right) to turn.

Avoid the Skin-Stealer at all costs! If you get hit three times in melee range, you will die.

## Design
### Main
The “main” file stitches all the game logic together, from the screen state to the enemy movement, it handles all the core game functionality. These are the files “main” pulls from (with brief descriptions).

This

### Screen Manager
One of the files, “game_screen”, handle the drawing and display of the different states of the game (start, playing, and end screens). With its tie into the “main”, the displayed screen will change based on what button is clicked or what key is pressed. For example, on the start screen, clicking the “start” button will change the game into playing mode. The same is true from playing to end screens and end screen to exit.

### Player
The user logic is handled by the “player” file. This involves movement controls, wall collisions, and image updating (for the surrounding map).
  
### Enemy
This file handles the enemy logic to incite the fun part of the game. The enemy in this game has a path-finding algorithm to locate and track down the player.
