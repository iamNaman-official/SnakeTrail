# 🐍 SnakeTrail
**Your Personal Python Learning Adventure: From "Hello World" to Full Mini-Projects**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview
SnakeTrail documents my exciting journey mastering Python, starting from writing my very first line of code (`print("Hello python world!")` in `01_print.py`) and progressing step-by-step to building complete, interactive console-based mini-projects. 

This repository showcases:
- **Fundamentals first**: Sequential lessons on core Python concepts.
- **Hands-on practice**: Fun beginner projects applying those skills in real scenarios.
- **Real-world patterns**: Input validation, modularity, logging, cross-platform compatibility, and game logic.

Whether you're a beginner tracing my learning path or seeking simple Python project ideas, SnakeTrail demonstrates how basic syntax evolves into functional apps like games (Hangman, Blackjack) and tools (Calculator with history).

## Features
- **Progressive Learning**: 12 basics files + 15+ mini-projects building complexity.
- **Interactive Console Apps**: User input handling, validation (alphabetic/single char), lives/scoring systems.
- **Modular Design**: Separate modules for assets (ASCII art, words), logging to files (history.txt, blackjack_log.txt).
- **Robust Utilities**: Cross-platform screen clearing, error handling (division by zero, invalid bets), persistent calculations.
- **Game Mechanics**: Randomization (words/decks), state tracking (wallets, guesses), win/lose conditions.
- **Modern Python**: `match-case` statements, `if __name__ == "__main__"`, datetime logging.

**Unique Architecture Highlights**: Simple, standalone scripts with shared patterns (clear_screen(), art imports). No external deps—pure standard library. Projects are self-contained, easy to run individually.

## Tech Stack
| Category       | Technologies |
|----------------|--------------|
| Language      | Python 3.10+ |
| Standard Libs | `os`, `random`, `datetime` |
| Styling       | ASCII Art (art.py modules) |
| Logging       | File-based (txt) |

## Getting Started

### Prerequisites
- Python 3.10+ ([Download](https://www.python.org/downloads/))
- Git (for cloning)

**Verify**:
```bash
python --version  # Should be 3.10+
git --version
```

### Quick Setup & First Run (Follow My Journey!)
1. **Clone**:
   ```bash
   git clone https://github.com/iamNaman-official/SnakeTrail.git
   cd SnakeTrail
   ```

2. **Start with Basics** (your first line of code!):
   ```bash
   python "Python Basics/Beginners/01_print.py"
   ```
   Output: `Hello python world!` 🚀

3. **Dive into Projects** (e.g., Hangman):
   ```bash
   python "Mini Projects/Beginners Projects/Hangman_game/game.py"
   ```
   *Note: Use quotes for paths with spaces.*

4. **Explore More**:
   ```bash
   python "Mini Projects/Beginners Projects/blackjack/blackjack.py"
   python "Mini Projects/Beginners Projects/calculator/calculator.py"
   ```

**Windows Users**: Use `py` instead of `python` if needed. No installs—runs instantly!

### Environment Variables
None.

### Development Tips
- Edit any `.py` and rerun.
- View logs: `cat history.txt` or `cat blackjack_log.txt`.
- Cross-platform: Works on Linux/Mac/Windows.

## Project Structure
```
SnakeTrail/
├── README.md                 # This file
├── Mini Projects/
│   └── Beginners Projects/   # 15+ interactive apps
│       ├── Hangman_game/     # Word guessing game (game.py + words.py + arts.py)
│       ├── blackjack/        # Casino Blackjack w/ betting & logging
│       ├── calculator/       # Persistent calculator w/ history
│       ├── #Beginner.md      # Mini-projects overview
│       └── ... (Auction, Caesar, etc.)
└── Python Basics/
    └── Beginners/            # 12 fundamentals lessons
        ├── 01_print.py       # Starting point: Hello World!
        ├── 02_input.py
        ├── ... 12_generators.py
```

- **Basics**: Linear progression mirroring my journey.
- **Projects**: Themed folders for organization.

## Usage Examples
### 1. Hangman (`game.py`)
```python
# Handles guesses, lives (6 stages), validation
guess = input("Guess a letter: ").lower()
# ... reveals word progressively
```
Play: Guess letters to reveal random word before losing lives.

### 2. Blackjack (`blackjack.py`)
```python
# Full game loop w/ wallets, deck, Ace adjustment
choice = input("Type 'y' to hit, 'n' to stand: ")
# Logs to blackjack_log.txt
```
Bet, hit/stand/double down vs. dealer.

### 3. Calculator (`calculator.py`)
```python
# Chain ops (+ - * /), logs to history.txt
result = calculator(a, b, opr)  # match-case
```
Continue with result or view history.

Explore others: BMI calc, auctions, ciphers!

## Contributing
1. Fork the repo.
2. Create branch: `git checkout -b feature/amazing-feature`
3. Commit: `git commit -m "Add amazing feature"`
4. Push: `git push origin feature/amazing-feature`
5. Open PR!

Suggestions for more projects welcome—let's extend the trail!

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

🐍 *Happy coding on the SnakeTrail! From one line to full projects—keep slithering forward.*
