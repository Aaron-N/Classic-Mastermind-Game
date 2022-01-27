# Classic-Mastermind-Game
A Python implementation of the classic Mastermind game. Solve the hidden secret code with 8 guesses or less.

The secret code consists of 4 color items, which may be from the set black, red, yellow, green, blue or 
white. Colors may be repeated in the secret code. 
For each round, the player makes a guess and is then provided a hint score to reveal how close the guess 
is to the secret code. Hints are as follow: ‘B’ – an item is the right color and in the right position, ‘W’ – an 
item is the right color but in the wrong position, ‘-‘ (a dash) – an item is the wrong color. The hints are 
provided in random order to make things more difficult. Some example scores: ‘- - - -‘, ‘B - W - ‘, ‘BW-W’, 
‘WWBB’
If the player determines the secret code within 8 guesses, they win the game.
If all 8 guesses are made without determining the secret code, the player loses, and the game is over.

To run the Mastermind game, use the command line:
 
python3 mastermind.py
 
The game then starts and is played in the terminal.
