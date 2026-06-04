# PIPELINE STEP 3: FUNNEL ANALYSIS & CUSTOMER BEHAVIOR (Task 7, 8, 9, 10)
import pandas as pd
import matplotlib.pyplot as plt

print("--- Starting Funnel & Behavioral Analysis ---")

df = pd.read_csv("../outputs/cleaned_ecommerce_data.csv")

# 1. Conversion Funnel Data
funnel_order = ['view', 'cart', 'purchase']
funnel_events = df['event_type'].value_counts().reindex(funnel_order)

# Funnel Summary DataFrame 
funnel_df = pd.DataFrame({
    'Stage': ['Product Views', 'Cart Additions', 'Purchase Completion'],
    'Event Count': [funnel_events['view'], funnel_events['cart'], funnel_events['purchase']]
})

# Drop-off
funnel_df['Stage Conversion %'] = (funnel_df['Event Count'] / funnel_df['Event Count'].iloc[0]) * 100
print("\n[FUNNEL STAGES BREAKDOWN]")
print(funnel_df)

# Funnel Chart in Save 
plt.figure(figsize=(8, 5))
plt.bar(funnel_df['Stage'], funnel_df['Event Count'], color=['#2980b9', '#e67e22', '#27ae60'])
plt.title('E-Commerce User Conversion Funnel')
plt.ylabel('Number of Actions')
plt.tight_layout()
plt.savefig('../outputs/funnel_chart.png')
plt.close()

# 2. Customer Behavior - Repeat Users vs Single Users
user_activity = df['user_id'].value_counts()
repeat_users = user_activity[user_activity > 1].count()
single_users = user_activity[user_activity == 1].count()

print(f"\n[CUSTOMER BEHAVIOR]")
print(f"- Repeat-Action Users: {repeat_users:,}")
print(f"- Single-Action Users: {single_users:,}")

# 3. Export Dashboard Prototype Data (Task 10)
funnel_df.to_csv("../outputs/funnel_summary.csv", index=False)
print("\nAll Analytical Summary CSVs exported to '/outputs' successfully!")