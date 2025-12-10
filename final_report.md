## Project Summary
We designed a game hub with classic two-player games like connect four and tic-tac-toe. The program has both players sign in, and keeps track of wins and losses for each game. This allows players to check leaderboards for individual games and a global leaderboard that shows total wins/losses over every game.

## Demo Video
# Login/gameplay

https://github.com/user-attachments/assets/ba27f3cc-5f9a-4cde-9da6-ca3cd2e8bc83

# Leaderboards

https://github.com/user-attachments/assets/0b995535-9c85-4a33-8b41-40f17e3f32a0


## What we learned (key learnings)
# Pygame
We learned what pygame is, and how to implement it for our project. Both of us have always had an interest in small local game design, and pygame turned out to be very helpful in keeping the project simple, and allowing us to focus less on overhead and more on the games themselves.

# Database Design
When designing our database, we considered multiple design options. Our first design had table players, storing usernames, passwords, and playerIDs. There was also a table games, with gameName and gameID. Finally, there would be a record table for storing who won and lost each game, with gameID, winnerID, and loserID. Since this design forced us to query the entire database every time we checked the leaderboard, we decided to just increment the total win/loss variable and game-specific win/loss for the player. Finally, since the project was designed for local play only, we decided to combine all variables into one table for simplicity.

# Sound/Music
We originally tried to include some music for the login screen, as well as sound affects for when a player wins. After a little research, we found a way to incorporate this through pygame's built-in functionality. After some debugging, we had a few sounds implemented. Unfortunately, due to concerns about where we could source our sound affects legally/ethically, we chose to remove the functionality but still found the process educational and enjoyable.

## AI
We did not incorporate AI into our final design project. Upon asking the class whether we should make an agent to play connect 4 or to focus more on making different games, the class encouraged variety of games.

When programming, we used AI for research, syntax questions, and some debugging.

## Why This Project?
Both of us are very competetive. We really enjoyed the idea of having short, simple games that should carry little to no weight and immortalizing the true champ. With neither of us having any game design experience, the project seemed the perfect place to introduce ourselves while focusing time on what matters most (the database of winners).

## Authentication
We used bcrypt as a simple way to prevent meddling with other players accounts.