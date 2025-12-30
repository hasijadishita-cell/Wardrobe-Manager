import sqlite3

Database="wardrobe.db"

def get_connection():
    return sqlite3.connect(Database)

def initialize_db():
    con = get_connection()
    cursor=con.cursor()

    query="""CREATE TABLE IF NOT EXISTS items( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    color TEXT NOT NULL,
    season TEXT NOT NULL,
    occasion TEXT NOT NULL,
    image_path TEXT,
    UNIQUE (name, category))"""
    cursor.execute(query)
    con.commit()
    con.close()

