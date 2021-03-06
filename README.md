# cs-wall
This repo is a Python implementation of Project Wall.
Project Wall is a modular robotics game meant for children and students from age 6 - 18. This repository contains the Python code modules to display the GUI content on the Raspberry Pi.

This repository is currently in development. For more information on Minibot see the [cs-minibot repo]{https://github.com/cornell-cup/cs-minibot}

## Classes in CS-wall
### Main function
Runs the GUI in a non-ending while loop

### Parser 
Used to parse the block code into robot command

### moveRobot
Packages the translated RFID's received from Wall through Parser as minibot script in the form of "<<<<SCRIPT, code>>>>" and sends it to minibot. In addition, records the current position of the bot during its movement as class variables.

### MapMaker
Object class for making levels for Wall from JSON files. Contains the keywords for parsing a level JSON into a data structure representing the game state for the GUI.

## Dependencies

### Running Dependencies 
File with list of RFIDs and another file of RFID tag's corresponding blocks should be provided for running the repo. The first file should be provided by the Raspberry Pi's RFID scanner and the second one should be hard coded by the user.  