# Pokemon-Team-Builder
This is a team builder for the video game franchise Pokemon
## Issues
1. Duplicating Moves
   Description: When adding moves to a Pokémon, the application allows the same move to be added multiple times.
   Expected Behavior: A move should only be added once to a Pokémon’s move set (max 4 unique moves).
   Possible Causes:
   The function responsible for adding moves does not check if the move is already in the Pokémon's move set.
   The move list is not being validated before updating.
   Fixing it:
   To fix this problem I added a check before the move was added to make sure that there was no duplicates.

2. Creating Team
   Description: When creating trying to create a team the program only lets the user name the team instead of being able to go ahead and add pokemon.
   Expected Behavior: After I add the name of the team the program should allow the user to begin adding pokemon 
   Possible Causes:
   For got to add a statement that allows that tells the program to let users add pokemon after team name
   Fixing it:
   I added an else statement that allows the user to be able to add pokemon after the name their team.

3. List for Moves
   Descirption: When adding moves for your pokemon the user is supposed to have a list of some of the moves it can lear
   Expected Behavior: A list should appear at the top showing users what moves a pokemon can learn
   Possible Causes:
   Fixing it:
   
