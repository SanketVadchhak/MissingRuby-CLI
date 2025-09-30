# Case of the Missing Ruby 🕵️‍♀️💎

## Overview

Case of the Missing Ruby is a command-line interactive mystery game written in Python. Assume the role of a detective assigned to recover the Crimson Star, a priceless ruby stolen from a museum vault. Investigate suspects, collect clues, and use deductive reasoning to solve the case and catch the culprit(s).

---

## Table of Contents

- [Game Premise](#game-premise)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Sample Gameplay](#sample-gameplay)
- [Extensibility](#extensibility)
- [Contributing](#contributing)
- [License](#license)

---

## Game Premise

The Crimson Star ruby has been stolen.  
Three suspects had access to the vault:
- Ms. Thorne, the curator  
- Mr. Finch, the security guard  
- Dr. Vance, the expert

Players must gather clues throughout the museum, analyze evidence, and ultimately identify who orchestrated the theft—whether one person or a team effort.

---

## Features

- Interactive CLI-based mystery gameplay  
- Three distinct locations to investigate  
- Multiple clues revealing motives and methods  
- Dynamic conclusion based on player deduction  
- Replayable for practice and entertainment

---

## Requirements

- Python 3.x (any stable version)
- No third-party libraries necessary

---

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/MissingRuby-CLI.git
    cd MissingRuby-CLI
    ```
2. Run the game:
    ```
    python case_of_missing_ruby.py
    ```

---

## How to Play

1. Begin by entering your detective name.
2. Investigate three key locations:
   - Curator's Office
   - Security Booth
   - Ruby's Display Case
3. Gather clues and formulate your theory.
4. At any time, type `solve` to make your accusation:
   - Choose one suspect or all three.
   - Success reveals the full conspiracy; incorrect guesses end the game.
5. Type `quit` to exit and end the investigation.

---

## Code Structure

The main game logic is handled in a perpetual loop:
while True:
# Prompt for investigation, solving, or quitting
# Check for discovered clues at each location
# Validate user input
# On 'solve', prompt for final accusation, check outcome
# On 'quit', exit
Unique clues, victory conditions, and prompts are displayed based on player actions, with tailored feedback at each stage.

---

## Sample Gameplay

Enter your detective name:
Detective Alex, a priceless ruby, The Crimson Star, has been stolen.

Your suspects are:

Ms. Thorne, the curator

Mr. Finch, the security guard

Dr. Vance, the expert

Where would you like to investigate?

The Curator’s Office

The Security Booth

The Ruby’s Display Case

(Type 'solve' when ready, 'quit' to exit)

You find a clue in the Security Booth: a coded keycard.



---

## Extensibility

Further improvements may include:
- New suspects and clues for expanded cases
- Branching storylines or randomized puzzles
- Visual feedback for CLI or graphical interface
- Timed investigation modes for competitive play

---

## Contributing

Contributions are encouraged!
Please submit issues for enhancements or bugs. Pull requests should include concise commit messages and follow repository code conventions.

---

## License

This game is released under the MIT License.

---

_Last Updated: October 2025_
