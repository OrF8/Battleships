# 🚢 Battleships
This repository contains the implementation of Exercise 4 from the course [**67101 - Introduction to Computer Science**](https://shnaton.huji.ac.il/index.php/NewSyl/67101/2/2024/) at The Hebrew University o Jerusalem ([HUJI](https://en.huji.ac.il/)). \
The project focuses on developing a console-based version of the classic Battleships game using Python. \
> 🎓 Final Grade: **99.5**

# 🎮 Game Overview
Battleships is a two-player strategy game where each player places ships on a grid and takes turns guessing the locations of the opponent's ships to sink them. \
In this implementation, the player competes against the computer in a turn-based format.

🛠️ Features
- Interactive console-based gameplay
- Randomized ship placement for the computer opponent
- Input validation to ensure correct user entries​
- Clear display of game boards after each move
- Modular code structure for maintainability​

📁 Project Structure
````
Battleships/
├── battleship.py   # Main game logic
├── helper.py       # Helper functions for game operations
├── README.md       # Project documentation
└── LICENSE         # MIT License
````

# 🚀 Getting Started
## Perquisites
- Python 3.x
## Installation
1. Clone the repository:
   ````
   git clone https://github.com/OrF8/Battleships.git
   cd Battleships
   ````
2. Run the game:
   ````
   python battleship.py
   ````
   
# 🎯 How to Play
1. Game Start:
   - The game initializes two 10x10 grids: one for the player and one for the computer.​
   - The computer randomly places its ships on its grid.
   - The player is prompted to place their ships by entering coordinates.
2. Gameplay Loop:
   - Players take turns guessing the coordinates of the opponent's ships.​
   - After each guess, the game displays whether it was a hit or miss.
   - The game continues until all of one player's ships are sunk.​
3. Winning the Game:​
   - The first player to sink all of the opponent's ships wins the game.

# 📄 License
This project is licensed under the MIT License – see the [**LICENSE**](https://github.com/OrF8/Battleships/blob/main/LICENSE) file for details.
































