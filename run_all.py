import subprocess
import os
import sys

print("==================================================")
print("🚀 STARTING COMPLETE DATA ANALYTICS PIPELINE")
print("==================================================")

# 1. Run Data Cleaning
print("\n[STEP 1/3] Running Data Cleaning...")
step1 = subprocess.run([sys.executable, "notebooks/1_data_cleaning.py"])

if step1.returncode != 0:
    print("❌ Error in Data Cleaning. Pipeline stopped.")
    exit()

# 2. Run KPI & EDA
print("\n[STEP 2/3] Running KPI Calculation & EDA...")
step2 = subprocess.run([sys.executable, "notebooks/2_kpi_and_eda.py"])

if step2.returncode != 0:
    print("❌ Error in KPI & EDA. Pipeline stopped.")
    exit()

# 3. Run Funnel Analysis
print("\n[STEP 3/3] Running Funnel & Behavioral Analysis...")
step3 = subprocess.run([sys.executable, "notebooks/3_funnel_analysis.py"])

if step3.returncode != 0:
    print("❌ Error in Funnel Analysis. Pipeline stopped.")
    exit()

print("\n==================================================")
print("✅ ALL ANALYTICAL BACKEND SCRIPTS RUN SUCCESSFULLY!")
print("==================================================")

# 4. Launch Dashboard
print("\n🖥️ Launching Interactive Streamlit Dashboard...\n")
subprocess.run(["streamlit", "run", "src/dashboard_app.py"])