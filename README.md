# Case of the Missing Ruby 🕵️‍♀️💎

## Overview

Case of the Missing Ruby is a command-line interactive mystery game written in Python. Assume the role of a detective assigned to recover the Crimson Star, a priceless ruby stolen from a museum vault. Investigate suspects, collect clues, and use deductive reasoning to solve the case and catch the culprit(s).

## 🕵️ Game Premise

The Crimson Star ruby has been stolen from the museum vault.
Your suspects, each with access, include:
- Ms. Thorne, the curator
- Mr. Finch, the security guard
- Dr. Vance, the expert
Utilize your investigative skills by exploring multiple locations, uncovering clues, and ultimately identifying the mastermind behind the theft.

## ✨ Features

- Interactive CLI-based mystery gameplay  
- Three distinct locations to investigate  
- Multiple clues revealing motives and methods  
- Dynamic conclusion based on player deduction  
- Replayable for practice and entertainment

## ⚙️ Requirements

- Python 3.x (any stable version)
- No third-party libraries necessary

## 🚀 Getting Started

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/MissingRuby-CLI.git
    cd MissingRuby-CLI
    ```
2. Run the game:
    ```
    python case_of_missing_ruby.py
    ```
    
### Usage

Simply follow the in-game prompts to navigate the investigation, collect clues, and solve the mystery.

## 🎮 How to Play

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

## 🗂 Code Structure

The game logic revolves around a continuous loop that:
- Prompts the player for investigation or to solve the case
- Validates inputs and tracks discovered clues
- Checks player accusations against the true culprit(s)
- Provides descriptive feedback and game progression

Example:
```
while True:
    choice = input("Your choice: ").lower()
    if choice == "quit":
        break
    elif choice == "solve":
        # logic for accusation and result
    else:
        # investigation logic
```


## 📝 Sample Gameplay

```text
Enter your detective name: John

Welcome, Detective John. A priceless ruby, 'The Crimson Star,' has been stolen.
Your suspects are the three people who had access to the vault last night:
- Ms. Thorne, the curator
- Mr. Finch, the security guard
- Dr. Vance, the expert

Choose a location to investigate:
1. The Curator's Office
2. The Security Booth
3. The Ruby's Display Case
Type 'solve' if you think you have enough information.
Type 'quit' to exit the game.
Your choice: 2

Inside the security booth, you find a small, coded keycard hidden under the desk.
```

## Extensibility

Further improvements may include:
- New suspects and clues for expanded cases
- Branching storylines or randomized puzzles
- Visual feedback for CLI or graphical interface
- Timed investigation modes for competitive play


## 🤝 Contributing

Enjoyed solving the mystery? Help make Case of the Missing Ruby even better! Here’s how you can contribute:
- **Report bugs**: Found something that doesn’t work or breaks the game? Let us know by opening an issue.
- **Suggest features**: Have a brilliant idea to add new suspects, clues, or gameplay elements? Share it!
- **Submit pull requests**: Improve the code, fix bugs, or enhance documentation. Fork the repo, make your changes, and open a pull request.
- **Improve docs**: Help polish instructions or add examples for easier gameplay.

### Getting Started

1. Fork the repository.
2. Clone your fork locally:
```bash
git clone https://github.com/yourusername/MissingRuby-CLI.git
```
3. Create a branch for your changes:
```bash
git checkout -b feature/your-feature-name
```
4. Implement your improvements.
5. Push your changes and open a pull request.
Every contribution counts and is greatly appreciated. Thank you for helping crack the case!

## License

This project is open-source and free to use for educational or entertainment purposes.

---

_Last Updated: October 2025_
