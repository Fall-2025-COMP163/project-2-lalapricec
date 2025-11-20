<div align="center">

# ⚔️ Character Abilities Showcase  
### *COMP 163 — Project 2*  
**Author: Lauren Price**

A polished, object-oriented fantasy battle simulation demonstrating  
**inheritance, method overriding, and unique character abilities**.

---

</div>

## Overview
This project uses Python classes to model different character types with their own attributes and abilities.  
It highlights core OOP concepts covered in COMP 163 up through **Inheritance**.

The program runs a small combat simulation where each character displays its own behavior, stats, and special moves.

---

## Inheritance Structure
Character
├── Warrior
│ └── Knight
├── Mage
│ └── Archmage
└── Rogue

Each subclass extends shared behavior from `Character` and customizes it through method overriding and special abilities.

---

## Character Abilities
| Class | Ability | Description |
|-------|---------|-------------|
| **Warrior** | Power Strike | Double-damage melee attack |
| **Knight** | Shield Bash | Armor-reduced damage + partial stun |
| **Mage** | Fireball | Magic damage that consumes mana |
| **Archmage** | Elemental Storm | High-damage multi-element spell |
| **Rogue** | Backstab / Hide | Triple-damage stealth attack + stealth reset |

---

## Running the Program
Clone your repository and run:

```bash
python3 project2_starter.py
This will display:
Character descriptions
Attack interactions
Special abilities
Final health outcome
  Running Tests
To run all automated tests:
python3 -m unittest
Make sure not to modify the test files provided.
## AI Assistance
AI assistance was used for:
Organization
Documentation style
All logic and final testing were reviewed and fully understood by me.
