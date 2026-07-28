DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (

    category_id INTEGER PRIMARY KEY AUTOINCREMENT,

    category_name TEXT UNIQUE

);

CREATE TABLE books (

    book_id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    price_gbp REAL,

    price_inr REAL,

    rating INTEGER,

    in_stock INTEGER,

    category_id INTEGER,

    FOREIGN KEY(category_id)
    REFERENCES categories(category_id)

);