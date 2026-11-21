# DOTA-Random-Build

This is my first project in Python — a simple CLI build and hero randomizer for **Dota 2** (updated for Patch 7.42). It generates chaotic, fun challenges for Turbo or All Pick matches with friends.

## Features

- **Random Position:** Picks a role from `1 pos` (Carry) to `5 pos` (Hard Support).
- **Full Hero Pool:** Randomly selects from all 127 Dota 2 heroes.
- **Dedicated Boots Slot:** Always assigns a random pair of boots for Slot 1.
- **5-Item Build Order:** Picks 5 unique items from Support, Magic, Defense, Damage, and Patch 7.42 pools without duplicates.
- **Talent Tree & Skill Priority:** Randomizes left/right talents for levels 10, 15, 20, and 25, plus which basic ability to max out first.
- **Zero External Dependencies:** Built using only Python's built-in `random` module.

## Requirements

- Python 3.8 or higher (no `pip install` needed).

## How to Run

1. Clone the repository or download `DOTA_Random_Build.py`:
   ```bash
   git clone [https://github.com/your-username/DOTA-Random-Build.git](https://github.com/your-username/DOTA-Random-Build.git)
   cd DOTA-Random-Build
