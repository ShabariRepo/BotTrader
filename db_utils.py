import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
DB_URL = os.getenv("NEON_DB_URL")

def log_trade(symbol, strategy, action, qty, entry_price, note=""):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS positions (
            id SERIAL PRIMARY KEY,
            symbol TEXT,
            strategy TEXT,
            action TEXT,
            entry_price NUMERIC,
            entry_time TIMESTAMP,
            exit_price NUMERIC,
            exit_time TIMESTAMP,
            status TEXT,
            quantity INTEGER,
            pnl_usd NUMERIC,
            notes TEXT
        )
    """)
    cur.execute("""
        INSERT INTO positions
        (symbol, strategy, action, entry_price, entry_time, status, quantity, pnl_usd, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (symbol, strategy, action, entry_price, datetime.utcnow(), "open", qty, None, note))
    conn.commit()
    cur.close()
    conn.close()
