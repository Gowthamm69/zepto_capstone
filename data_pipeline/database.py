import os
import sqlite3
import pandas as pd

# =====================================
# Paths
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

DATABASE_DIR = os.path.join(BASE_DIR, "database")

SQL_DIR = os.path.join(BASE_DIR, "sql")

os.makedirs(DATABASE_DIR, exist_ok=True)

CSV_FILE = os.path.join(DATA_DIR, "cleaned_books.csv")

DB_FILE = os.path.join(DATABASE_DIR, "books.db")

SCHEMA_FILE = os.path.join(SQL_DIR, "schema.sql")

# =====================================
# Load CSV
# =====================================

df = pd.read_csv(CSV_FILE)

# =====================================
# Create Database
# =====================================

conn = sqlite3.connect(DB_FILE)

cursor = conn.cursor()

# =====================================
# Execute Schema
# =====================================

with open(SCHEMA_FILE, "r") as file:
    cursor.executescript(file.read())

# =====================================
# Insert Categories
# =====================================

categories = sorted(df["category"].unique())

category_map = {}

for category in categories:

    cursor.execute(
        "INSERT INTO categories(category_name) VALUES (?)",
        (category,)
    )

    category_map[category] = cursor.lastrowid

# =====================================
# Insert Books
# =====================================

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO books
        (
            title,
            price_gbp,
            price_inr,
            rating,
            in_stock,
            category_id
        )
        VALUES
        (
            ?,?,?,?,?,?
        )
        """,

        (
            row["title"],
            row["price_gbp"],
            row["price_inr"],
            int(row["rating"]),
            int(row["in_stock"]),
            category_map[row["category"]]
        )

    )

conn.commit()

print("\nDatabase Created Successfully")

print(f"Database Location : {DB_FILE}")

cursor.execute("SELECT COUNT(*) FROM books")

print("Books :", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM categories")

print("Categories :", cursor.fetchone()[0])

conn.close()