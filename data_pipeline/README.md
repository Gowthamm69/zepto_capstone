# Data Pipeline

## Objective

Scrape book information from BooksToScrape, clean the data, convert currency, store it in SQLite, and query the database using SQL and Pandas.

---

## Libraries Used

- requests
- BeautifulSoup4
- pandas
- sqlite3

---

## Dataset

Website:
https://books.toscrape.com

Books scraped:
100

Categories:
29

---

## Cleaning

- Removed GBP (£) symbol
- Converted price to float (price_gbp)
- Converted rating text (One–Five) to integer (1–5)
- Converted availability to boolean (in_stock)
- Missing numeric values handled using median imputation
- Converted GBP to INR using the fixed rate

1 GBP = 105.50 INR

---

## Database

Two normalized tables were created.

### categories

- category_id (Primary Key)
- category_name

### books

- book_id (Primary Key)
- title
- price_gbp
- price_inr
- rating
- in_stock
- category_id (Foreign Key)

---

## SQL Queries

The following SQL operations were implemented:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- BETWEEN
- JOIN

---

## Pandas

The JOIN result was demonstrated using

- pd.read_sql()
- pd.merge()

---

## Run

```bash
python pipeline.py
```