# E-Commerce Store Performance Analysis

## 🎯 Project Objective

The main objective of this project is to model the complete e-commerce customer journey, from product viewing to cart addition and final purchase conversion.

By evaluating behavioral bottlenecks and revenue distribution patterns, the project delivers actionable, data-driven business recommendations to optimize website UI/UX and improve store inventory management.

---

## 📁 Repository Structure & Modular Architecture

This repository follows a production-level modular architecture to ensure code maintainability, scalability, and reusability.

```text
my_internship_project/
│
├── data/
│   └── events.csv
│
├── notebooks/
│   ├── 1_data_cleaning.py
│   ├── 2_kpi_and_eda.py
│   └── 3_funnel_analysis.py
│
├── outputs/
│   ├── cleaned_ecommerce_data.csv
│   ├── funnel_chart.png
│   └── analytical_summary_csvs/
│
├── src/
│   └── dashboard_app.py
│
├── run_all.py
│
└── README.md
```

### Directory Description

| Folder/File | Description |
|------------|-------------|
| data/ | Raw e-commerce dataset (~885k records) |
| notebooks/ | Data cleaning, KPI analysis, and funnel analysis scripts |
| outputs/ | Generated datasets, charts, and KPI reports |
| src/ | Interactive Streamlit dashboard |
| run_all.py | Pipeline automation script |
| README.md | Project documentation |

---

## ⚡ Data Pipeline Automation

Instead of running individual scripts manually, a centralized automation pipeline executes all stages sequentially.

If any stage fails, the pipeline stops execution to prevent downstream errors and maintain data integrity.

Run the complete workflow using:

```bash
python run_all.py
```

This process will:

1. Clean and preprocess raw data
2. Calculate KPIs and perform exploratory analysis
3. Generate funnel analytics
4. Export reports and visualizations
5. Launch the Streamlit dashboard

---

## ⚙️ Methodology & Pipeline Breakdown

### 🧼 1. Data Cleaning & Integrity Preservation

**File:** `1_data_cleaning.py`

Key processing steps:

- Processed 885,129 raw records into 884,464 clean records
- Removed duplicate transactions
- Removed invalid records with zero or negative prices
- Preserved valuable data by replacing missing:
  - `brand` → `"Unknown"`
  - `category_code` → `"Unknown"`
- Improved overall dataset consistency and reporting quality

---

### 📈 2. KPI Computation & Exploratory Data Analysis

**File:** `2_kpi_and_eda.py`

Generated core business metrics:

| KPI | Value |
|------|--------|
| Total Revenue | $5,125,113.92 |
| Total Orders | 37,343 |
| Average Order Value (AOV) | $137.24 |

AOV Formula:

```text
AOV = Total Revenue ÷ Total Orders
```

Additional analyses include:

- Revenue trends
- Brand performance
- Hourly transaction patterns
- User activity distribution

---

### 🛒 3. User Conversion Funnel Analysis

**File:** `3_funnel_analysis.py`

Tracks customer progression through the purchasing journey.

| Funnel Stage | Count | Conversion Rate |
|-------------|--------|----------------|
| Product Views | 793,089 | 100.00% |
| Cart Additions | 54,032 | 6.81% |
| Purchase Completions | 37,343 | 4.71% |

### Funnel Insights

- Significant drop-off occurs between product views and cart additions.
- Users who reach the cart stage demonstrate substantially higher purchase intent.
- Funnel analytics highlight opportunities for conversion optimization.

---

## 🖥️ Interactive Dashboard Features
<img width="1209" height="636" alt="Screenshot (327)" src="https://github.com/user-attachments/assets/1b3d41af-3d44-4fbe-883d-d3b68714daa9" />

## 💡 Key Business Recommendations

### 1. Product Page UI/UX Optimization (Critical)

Analysis identified a major conversion bottleneck:

- Over 90% of users view products but do not add items to their cart.

Recommended actions:

- Improve product page layouts
- Enhance call-to-action visibility
- Simplify purchasing workflows
- Increase trust indicators and product information clarity

---

### 2. Inventory Data Governance Improvement (High Priority)

A significant portion of revenue originates from products with missing brand information.

Findings:

- "Unknown" brands contributed approximately $600,000 in revenue.

Recommended actions:

- Make brand information mandatory during product onboarding
- Implement stricter validation rules
- Improve catalog governance procedures

---

### 3. Customer Retention & Loyalty Programs

Repeat customers contribute significantly to long-term revenue generation.

Recommended actions:

- Launch loyalty reward programs
- Implement personalized promotions
- Create customer retention campaigns
- Introduce customer lifetime value (LTV) monitoring

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- CSV Processing
- Data Analytics & Visualization

---

## 🚀 Project Outcome

This project successfully transformed raw e-commerce interaction data into actionable business intelligence by:

- Cleaning and validating large-scale transaction data
- Measuring customer conversion behavior
- Identifying revenue-driving brands and trends
- Detecting funnel bottlenecks
- Delivering business-focused recommendations through an interactive analytics dashboard

The solution demonstrates practical applications of data analytics, business intelligence, and customer behavior modeling in an e-commerce environment.
