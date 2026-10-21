
import sqlite3

def create_table():
    dbConn = sqlite3.connect("urls.db")
    dbConn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            code TEXT PRIMARY KEY,
            url TEXT NOT NULL
        )
    """)
    dbConn.commit()
    dbConn.close()


def store_url(code, url):
    dbConn = sqlite3.connect("urls.db")
    dbConn.execute(
        "INSERT INTO urls (code, url) VALUES (?, ?)",
        (code, url)
    )
    dbConn.commit()
    dbConn.close()


def get_url(code):
    dbConn = sqlite3.connect("urls.db")
    result = dbConn.execute(
        "SELECT url FROM urls WHERE code = ?",
        (code,)
    ).fetchone()
    dbConn.close()

    return result[0] if result else None
