# Pokemon-Team-Builder
This is a team builder for the video game franchise Pokemon
## Issues
Duplicate Moves Allowed
Issue: Initially, users could add the same move multiple times to a Pokémon.
Cause: There was no validation to check if a move had already been selected.
Solution: Implemented a check that prevents adding duplicate moves.

Can't Manage Teams After Creation
Issue: After creating a team, users couldn't manage their teams properly.
Cause: The manage team functionality was not properly linked in the main menu.
Solution: Fixed menu navigation and added a separate "Manage Team" menu.

Missing Error Handling for Invalid Pokémon Names
Issue: If a user entered an incorrect or misspelled Pokémon name, the program would crash.
Cause: The program tried to fetch data for an invalid Pokémon name without checking if it existed.
Solution: Implemented a check that notifies the user if the Pokémon is not found instead of crashing.

Moves Not Displaying When Choosing Moves
Issue: When selecting moves for a Pokémon, the list of available moves was not displaying properly.
Cause: The move list was not being retrieved correctly from the API before prompting the user.
Solution: Ensured the move list is fetched from the API and displayed correctly before allowing selection.

No Confirmation When Deleting a Team
Issue: Users could accidentally delete a team with no way to confirm or undo the action.
Cause: The delete function immediately removed the team without asking the user for confirmation.
Solution: Added a confirmation step before deleting a team to prevent accidental deletions.

User Could Not View Team Details
Issue: The option to view team details was missing from the main menu.
Cause: The program did not include a menu option for viewing team details.
Solution: Added a "View Team" option in the main menu to display all Pokémon, their abilities, and moves.

Team Limit Not Enforced
Issue: Users could add more than 6 Pokémon to a team, exceeding the expected limit.
Cause: There was no validation check to enforce a maximum team size.
Solution: Implemented a validation check to prevent users from adding more than 6 Pokémon to a team.

No Indicator If There Are No Saved Teams
Issue: If no teams were created, selecting "View Teams" did nothing.
Cause: The program did not check if the team list was empty before displaying team details.
Solution: Added a message that displays "No teams have been created yet" if no teams exist.

Users Could Remove Pokémon While Creating a Team
Issue: Users were able to remove Pokémon while initially creating a team, which was not intended.
Cause: The remove Pokémon functionality was mistakenly available during team creation.
Solution: Adjusted functionality so Pokémon can only be removed in the "Manage Team" menu.

No Way to Modify Pokémon’s Moves After Selecting Them
Issue: Once moves were selected for a Pokémon, there was no way to change them.
Cause: The system only allowed move selection during initial Pokémon addition, with no modification option.
Solution: Added separate options for adding and removing moves within the "Manage Team" menu.

Pokémon Abilities Were Not Selectable
Issue: The program would automatically assign a Pokémon's first ability without allowing the user to choose from all available abilities.
Cause: The system selected the first ability from the API response without providing a choice.
Solution: Implemented a selection system that lets the user choose from all abilities the Pokémon can have.

No Type Effectiveness Information
Issue: Users had no way to see type effectiveness, making it harder to build a strong team.
Cause: The program did not retrieve or display type effectiveness data from the API.
Solution: Integrated a type effectiveness display that shows what a Pokémon is strong and weak against.

Connection Errors When Fetching Pokémon Data
Issue: Sometimes, the program would fail to connect to the PokeAPI, causing it to crash.
Cause: The program did not handle API connection failures gracefully.
Solution: Added error handling to retry the request or inform the user if the API is unavailable.

Add and Remove Moves Feature Did Not Work Properly
Issue: The option to add and remove moves was in a single menu item, causing conflicts.
Cause: The program tried to handle both adding and removing moves in one function, making it difficult for users to modify moves properly.
Solution: Split "Manage Moves" into two separate options: one for adding moves and one for removing moves.


