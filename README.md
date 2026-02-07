# Python Simple Auth

Simple authentication system written in **Python**, using **SQLite** for data storage.

The project includes:
- User registration
- User login
- Password hashing with SHA-256
- SQLite database (`users.db`)
- Optional Discord webhook logging

## Features
- Register users with unique usernames
- Secure password storage using hash
- Login validation
- Local database (no server required)
- Console-based interface

## Technologies
- Python 3
- SQLite3
- hashlib
- requests

## How it works
1. The program creates a local SQLite database
2. Users can register with a username and password
3. Passwords are stored as hashes
4. Login compares the hashed password
5. Events can be sent to a Discord webhook

## How to run
```bash
python main.py
