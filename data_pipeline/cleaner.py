import os
import pandas as pd

# =====================================
# Create Paths
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_FILE = os.path.join(DATA_DIR, "raw_books.csv")

CLEAN_FILE = os.path.join(DATA_DIR, "cleaned_books.csv")

# =====================================
# Read Raw Data
# =====================================

df = pd.read_csv(RAW_FILE)

print("Raw Dataset Shape :", df.shape)

# =====================================
# Convert Price to Float
# =====================================

df["price_gbp"] = (
    df["price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.extract(r"(\d+\.\d+)")[0]
)

df["price_gbp"] = pd.to_numeric(
    df["price_gbp"],
    errors="coerce"
)

median_price = df["price_gbp"].median()

df["price_gbp"] = df["price_gbp"].fillna(median_price)

# =====================================
# Convert Rating
# =====================================

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["star_rating"].map(rating_map)

median_rating = int(df["rating"].median())

df["rating"] = df["rating"].fillna(median_rating)

df["rating"] = df["rating"].astype(int)

# =====================================
# Convert Availability
# =====================================

df["in_stock"] = df["availability"].str.contains(
    "In stock",
    case=False,
    na=False
)

# =====================================
# Currency Conversion
# =====================================

GBP_TO_INR = 105.50

df["price_inr"] = (
    df["price_gbp"] * GBP_TO_INR
).round(2)

# =====================================
# Remove Old Columns
# =====================================

df.drop(
    columns=[
        "price",
        "star_rating",
        "availability"
    ],
    inplace=True
)

# =====================================
# Save Cleaned Data
# =====================================

df.to_csv(CLEAN_FILE, index=False)

print("\nCleaning Completed Successfully")

print("Clean Dataset Shape :", df.shape)

print("\nColumns")

print(df.columns)

print("\nFirst Five Rows")

print(df.head())