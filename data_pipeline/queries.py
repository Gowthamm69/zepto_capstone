import os
import sqlite3
import pandas as pd

# ==========================================
# Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_FILE = os.path.join(BASE_DIR, "database", "books.db")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_FILE)

# ==========================================
# Query 1
# SELECT + WHERE
# ==========================================

query1 = """
SELECT title, rating
FROM books
WHERE rating = 5;
"""

df1 = pd.read_sql(query1, conn)

print("\n========== QUERY 1 ==========")
print(df1.head())

df1.to_csv(os.path.join(OUTPUT_DIR, "query1.csv"), index=False)

# ==========================================
# Query 2
# ORDER BY + LIMIT
# ==========================================

query2 = """
SELECT title, price_gbp
FROM books
ORDER BY price_gbp DESC
LIMIT 10;
"""

df2 = pd.read_sql(query2, conn)

print("\n========== QUERY 2 ==========")
print(df2)

df2.to_csv(os.path.join(OUTPUT_DIR, "query2.csv"), index=False)

# ==========================================
# Query 3
# DISTINCT
# ==========================================

query3 = """
SELECT DISTINCT rating
FROM books
ORDER BY rating;
"""

df3 = pd.read_sql(query3, conn)

print("\n========== QUERY 3 ==========")
print(df3)

df3.to_csv(os.path.join(OUTPUT_DIR, "query3.csv"), index=False)

# ==========================================
# Query 4
# BETWEEN
# ==========================================

query4 = """
SELECT title, price_gbp
FROM books
WHERE price_gbp BETWEEN 20 AND 30;
"""

df4 = pd.read_sql(query4, conn)

print("\n========== QUERY 4 ==========")
print(df4.head())

df4.to_csv(os.path.join(OUTPUT_DIR, "query4.csv"), index=False)

# ==========================================
# Query 5
# JOIN
# ==========================================

query5 = """
SELECT
b.title,
b.rating,
c.category_name
FROM books b
JOIN categories c
ON b.category_id = c.category_id
ORDER BY b.rating DESC;
"""

df5 = pd.read_sql(query5, conn)

print("\n========== QUERY 5 ==========")
print(df5.head())

df5.to_csv(os.path.join(OUTPUT_DIR, "query5.csv"), index=False)

# ==========================================
# pd.read_sql Demonstration
# ==========================================

print("\n========== pd.read_sql OUTPUT ==========")

books_sql = pd.read_sql("SELECT * FROM books", conn)

categories_sql = pd.read_sql("SELECT * FROM categories", conn)

print(books_sql.head())

print(categories_sql.head())

# ==========================================
# pd.merge Demonstration
# ==========================================

merged = pd.merge(
    books_sql,
    categories_sql,
    on="category_id",
    how="inner"
)

print("\n========== pd.merge OUTPUT ==========")

print(
    merged[
        [
            "title",
            "category_name",
            "rating"
        ]
    ].head()
)

merged.to_csv(
    os.path.join(OUTPUT_DIR, "merge_output.csv"),
    index=False
)

conn.close()

print("\n====================================")
print("All Queries Executed Successfully")
print("====================================")