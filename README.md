# Souro's Diner

A text-based restaurant ordering game built in Python for my ICS3U culminating project, built to
demonstrate input/output, variables, arithmetic, if/else logic, loops, and functions.

## Description

Souro's Diner is a console game that simulates ordering food at a restaurant. Players
choose from five menu categories:

- Breakfast
- Lunch
- Dinner
- Desserts
- Drinks

Based on the budget they get and how many people the user chooses to input, they'll select items and quantities, and receive an itemized receipt with subtotal, tax, and
total at checkout. The game validates all user input so it can't be crashed by invalid
entries, and loops until the player chooses to exit. This project was built to
demonstrate input/output, variables, arithmetic, if/else logic, loops, and functions.

## Getting Started

### Dependencies

* Any Python 3.x Version
* Windows 10/11 (for the packaged `.exe`; the `.py` file itself runs on any OS with Python installed)
* [PyInstaller](https://pyinstaller.org/) (only needed if rebuilding the `.exe` yourself)

### Installing

* Clone or download this repository:
```
git clone https://github.com/<your-username>/<your-repo-name>.git
```
* No additional setup is required to run the `.py` file — it uses only Python's standard library.

### Executing program

**Option 1: Run the Python file directly**
* Open the project folder in VS Code or your terminal
* Run:
```
python restaurantgame.py
```

**Option 2: Run the packaged executable**
* Navigate to the `dist` folder (if included/built)
* Double-click `restaurantgame.exe`

**Playing the game**
* Choose an option from the main menu (Order Food / Exit)
* Pick a category (breakfast, lunch, dinner, desserts, or drinks)
* Enter the number of the item you want, then the quantity
* Repeat until you're done ordering, then exit to see your final receipt

## Help

* If you see `pyinstaller: The term 'pyinstaller' is not recognized...` while building the `.exe`, run it through Python's module flag instead:
```
python -m PyInstaller --onefile restaurantgame.py
```
* If the game crashes on a number input, make sure you're entering whole numbers only (no letters or decimals) — the game will normally re-prompt you instead of crashing.

## Authors

@sour-OS Sourodeep Bhowmik 

## Version History
* 0.1.1
Second release — added budget system to the game
* 0.1
Initial release — full menu system, input validation, receipt generation

## License

This project was created for educational purposes as part of an ICS3U course assignment.

## Acknowledgments

* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
