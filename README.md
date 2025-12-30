# Wardrobe Manager

## Overview
Wardrobe Manager is a desktop-based Python application that helps users manage their clothing items efficiently.
Users can add, update, delete and view clothing items, along with storing images and details such as category, color, season, and occasion.

Thios project demonstrates GUI development, database integration, and CRUD operations using Python.


## Features
- Add items
- Update items
- Prevents duplicate items by name
- Delete items
- View all items in a list
- Image preview for selected items
- GUI-based interface
- Persistent storage using SQLite

## Tech Stack
- Python 3
- Tkinter - GUI framework
- SQLite3 - Database
- Pillow (PIL) - Image handling
- VS code - Developmemnt environment

## Project Structure

Wardrobe Manager/
|
|___main.py         # Application entry point
|___gui.py          # Tkinter GUI logic
|___models.py       # Database operations (CRUD)
|___database.py     #Database connection and setup
|___screenshorts/   #Screenshorts of the app working
|___README.md

## Key Learning Outcomes

- Built a complete GUI-based application from scratch
- Implemented CRUD operations using SQLite
- Managed application state between GUI and database
- Handled image storage and preview
- Debugged real world issues like:
   . Duplicate records
   . Database update errors
- Improved code organization using modular files

## How to run project
Ensure you have the following installed:
. Python 3.9 or later
. pip (Python package manager)

- Check:
python --version
pip --version

- Install Required Libraries

This project uses pillow for image handling.

pip install pillow

- Run the application 

The Tkinter GUI opens directly from gui.py.
python gui.py

On macOS/Linux:
python3 gui.py

- How the program works
. gui.py contains all Tkinter GUI logic
. models.py handles database operations (CRUD)
. database.py sets up the SQLite database
. Data is stored locally using SQlite

## Author

Dishita Hasija
Bachelor of Engineering (Software Engineering)- RMIT University
Melbourne, Australia

## Status
- Completed core functionality
- Actively improving and refactoring
