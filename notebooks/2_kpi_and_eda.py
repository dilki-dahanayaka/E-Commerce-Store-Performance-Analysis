#STEP 2: KPI CALCULATION & MERCHANDISING EDA (Task 5, 6)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Starting KPI Calculation & EDA ---")

# Cleaned data load 
df = pd.read_csv("../outputs/cleaned_ecommerce_data.csv")

# 1. Core KPI Calculations 
total_unique_users = df['user_id'].nunique()
total_sessions = df['user_session'].nunique() if 'user_session' in df.columns else df['user_id'].nunique()
total_revenue = df[df['event_type'] == 'purchase']['price'].sum()
total_purchases = df[df['event_type'] == 'purchase'].shape[0]
aov = total_revenue / total_purchases if total_purchases > 0 else 0

# Industry Standard Conversion Rate (Unique Buyers / Total Unique Users)
unique_buyers = df[df['event_type'] == 'purchase']['user_id'].nunique()
conversion_rate = (unique_buyers / total_unique_users) * 100

print(f"\n[CORE KPIs]")
print(f"- Total Unique Users: {total_unique_users:,}")
print(f"- Total Revenue: ${total_revenue:,.2f}")
print(f"- Average Order Value (AOV): ${aov:.2f}")
print(f"- Conversion Rate: {conversion_rate:.2f}%")

# 2. EDA - Event Distribution Graph Save 
plt.figure(figsize=(7, 4))
df['event_type'].value_counts().plot(kind='bar', color=['#34495e', '#e67e22', '#2ecc71'])
plt.title('Platform Event Distribution')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('../outputs/event_distribution.png')
plt.close()

# 3. Merchandising Analysis (Top Performers)
brand_revenue = df[df['event_type'] == 'purchase'].groupby('brand')['price'].sum().sort_values(ascending=False)
print("\n[TOP BRANDS BY REVENUE]")
print(brand_revenue.head(5))

print("\nEDA Outputs and Graphs saved to '/outputs' folder successfully!")