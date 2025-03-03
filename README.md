# Pokemon-Team-Builder
This is a team builder for the video game franchise Pokemon
## Issues
1. Duplicate Moves Allowed  
Issue: Initially, users could add the same move multiple times to a Pokémon.  
Solution: Implemented a check that prevents adding duplicate moves.  

2. Can't Manage Teams After Creation 
Issue: After creating a team, users couldn't manage their teams properly.  
Solution: Fixed menu navigation and added a separate "Manage Team" menu.
 
3. Missing Error Handling for Invalid Pokémon Names
Issue: If a user entered an incorrect or misspelled Pokémon name, the program would crash.
Solution: Implemented a check that notifies the user if the Pokémon is not found instead of crashing.

4. Moves Not Displaying When Choosing Moves
Issue: When selecting moves for a Pokémon, the list of available moves was not displaying properly.
Solution: Ensured the move list is fetched from the API and displayed correctly before allowing selection.

5. No Confirmation When Deleting a Team
Issue: Users could accidentally delete a team with no way to confirm or undo the action.
Solution: Added a confirmation step before deleting a team to prevent accidental deletions.

6. User Could Not View Team Details
Issue: The option to view team details was missing from the main menu.
Solution: Added a "View Team" option in the main menu to display all Pokémon, their abilities, and moves.

7. Team Limit Not Enforced
Issue: Users could add more than 6 Pokémon to a team, exceeding the expected limit.
Solution: Implemented a validation check to prevent users from adding more than 6 Pokémon to a team.

8. No Indicator If There Are No Saved Teams
Issue: If no teams were created, selecting "View Teams" did nothing.
Solution: Added a message that displays "No teams have been created yet" if no teams exist.

9. Users Could Remove Pokémon While Creating a Team
Issue: Users were able to remove Pokémon while initially creating a team, which was not intended.
Solution: Adjusted functionality so Pokémon can only be removed in the "Manage Team" menu.

10. No Way to Modify Pokémon’s Moves After Selecting Them
Issue: Once moves were selected for a Pokémon, there was no way to change them.
Solution: Added the option to add or remove moves within the "Manage Team" menu.

11. Pokémon Abilities Were Not Selectable
Issue: The program would automatically assign a Pokémon's first ability without allowing the user to choose from all available abilities.
Solution: Implemented a selection system that lets the user choose from all abilities the Pokémon can have.

12. No Type Effectiveness Information
Issue: Users had no way to see type effectiveness, making it harder to build a strong team.
Solution: Integrated a type effectiveness display that shows what a Pokémon is strong and weak against.

13. Connection Errors When Fetching Pokémon Data
Issue: Sometimes, the program would fail to connect to the PokeAPI, causing it to crash.
Solution: Added error handling to retry the request or inform the user if the API is unavailable.
