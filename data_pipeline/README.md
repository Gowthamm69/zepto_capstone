# Data Pipeline

## Objective

Develop an end-to-end data pipeline that scrapes book information from BooksToScrape, cleans and transforms the data, stores it in a normalized SQLite database, and performs SQL analysis using SQLite and Pandas.

---

## Project Structure

```
data_pipeline/
│
├── scraper.py
├── cleaner.py
├── database.py
├── queries.py
├── pipeline.py
├── README.md
├── data/
├── database/
├── outputs/
└── sql/
```

---

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run

Execute the complete pipeline using:

```bash
python pipeline.py
```

This performs the following steps automatically:

1. Scrapes book information.
2. Cleans and transforms the data.
3. Creates and populates the SQLite database.
4. Executes SQL queries.
5. Saves query outputs.

---

## Libraries Used

- requests
- BeautifulSoup4
- pandas
- sqlite3

---

## Dataset

**Source:** https://books.toscrape.com

- Books scraped: **100**
- Categories: **29**

---

## Data Cleaning

The following transformations were applied:

- Removed the GBP (£) currency symbol.
- Converted prices to numeric (`price_gbp`).
- Converted textual ratings (One–Five) into integers (1–5).
- Converted stock availability into boolean values (`in_stock`).
- Missing numeric values were handled using **median imputation**.
- Added `price_inr` using a fixed conversion rate.

**Exchange Rate**

```
1 GBP = 105.50 INR
```

---

## Database Design

A normalized SQLite database with two related tables was created.

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

This design minimizes data duplication and establishes a one-to-many relationship between categories and books.

---

## SQL Queries Implemented

The following SQL operations were demonstrated:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- BETWEEN
- JOIN

Query outputs are stored in the `outputs/` folder.

---

## Pandas Operations

The project demonstrates:

- `pd.read_sql()`
- `pd.merge()`

to retrieve and combine relational data.

---

## Design Decisions

- Used **SQLite** because it is lightweight and requires no external database server.
- Used **BeautifulSoup** for HTML parsing due to its simplicity.
- Used **Pandas** for efficient data cleaning and CSV handling.
- Used a **normalized database schema** to reduce redundancy.
- Automated the complete workflow using `pipeline.py`.

---