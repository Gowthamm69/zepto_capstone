import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ==========================
# Create paths
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(DATA_DIR, "raw_books.csv")

BASE_URL = "https://books.toscrape.com/"

books = []

# ==========================
# Scrape first 5 pages
# ==========================

for page in range(1, 6):

    print(f"Scraping Page {page}")

    page_url = f"{BASE_URL}catalogue/page-{page}.html"

    response = requests.get(page_url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        print(f"Failed to load {page_url}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    for product in products:

        title = product.h3.a["title"]

        price = product.find("p", class_="price_color").text.strip()

        rating = product.find("p")["class"][1]

        availability = product.find(
            "p",
            class_="instock availability"
        ).text.strip()

        detail_link = product.h3.a["href"]

        detail_url = urljoin(page_url, detail_link)

        detail_response = requests.get(detail_url)
        detail_response.encoding = "utf-8"

        if detail_response.status_code != 200:
            continue

        detail_soup = BeautifulSoup(
            detail_response.text,
            "html.parser"
        )

        breadcrumb = detail_soup.find("ul", class_="breadcrumb")

        items = breadcrumb.find_all("li")

        category = items[2].get_text(strip=True)

        books.append(
            {
                "title": title,
                "price": price,
                "star_rating": rating,
                "availability": availability,
                "category": category,
            }
        )

# ==========================
# Save CSV
# ==========================

df = pd.DataFrame(books)

df.to_csv(OUTPUT_FILE, index=False)

print("\n====================================")
print("Scraping Completed Successfully")
print("====================================")
print(f"Total Books Scraped : {len(df)}")
print(f"CSV Saved To : {OUTPUT_FILE}")
print()

print(df.head())