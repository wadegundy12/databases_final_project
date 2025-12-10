## Project Summary
We designed a game hub with classic two-player games like connect four and tic-tac-toe. The program has both players sign in, and keeps track of wins and losses for each game. This allows players to check leaderboards for individual games and a global leaderboard that shows total wins/losses over every game.

## Demo Video
//TODO:: insert video here

## What we learned (key learnings)
# Pygame
We learned what pygame is, and how to implement it for our project. Both of us have always had an interest in small local game design, and pygame turned out to be very helpful in keeping the project simple, and allowing us to focus less on overhead and more on the games themselves.

# Database Design
When designing our database, we considered multiple design options. Our first design had table players, storing usernames, passwords, and playerIDs. There was also a table games, with gameName and gameID. Finally, there would be a record table for storing who won and lost each game, with gameID, winnerID, and loserID. Since this design forced us to query the entire database every time we checked the leaderboard, we decided to just increment the total win/loss variable and game-specific win/loss for the player. Finally, since the project was designed for local play only, we decided to combine all variables into one table for simplicity.