# STEP 1: DATA INGESTION & CLEANING (Task 1, 2, 3, 4)
import pandas as pd
import numpy as np
import os

print("--- Starting Data Cleaning Pipeline ---")

if not os.path.exists('../outputs'):
    os.makedirs('../outputs')

# 1. Load Dataset
try:
    df = pd.read_csv("data/events.csv")
    print(f"Dataset Loaded Successfully. Raw Rows: {df.shape[0]}")
except FileNotFoundError:
    print("Error: '/data/events.csv'සොයාගත නොහැකි විය. කරුණාකර file එක නිවැරදි තැන තබන්න.")
    exit()

# 2. Handle Missing Values 
df['brand'] = df['brand'].fillna('Unknown')
df['category_code'] = df['category_code'].fillna('Unknown')


df = df.dropna(subset=['price', 'user_id', 'event_type'])

# 3. Price Validation (- and 0)
df = df[df['price'] > 0]

# 4. Convert Datetime & Feature Engineering
df['event_time'] = pd.to_datetime(df['event_time'])
df['date'] = df['event_time'].dt.date
df['month'] = df['event_time'].dt.to_period('M').astype(str)
df['day'] = df['event_time'].dt.day_name()
df['hour'] = df['event_time'].dt.hour

# 5. Remove Exact Duplicates
df = df.drop_duplicates()

# Reset Index
df = df.reset_index(drop=True)

# Export file
df.to_csv("../outputs/cleaned_ecommerce_data.csv", index=False)
print(f"Data Cleaning Done! Cleaned Rows Remaining: {df.shape[0]}")