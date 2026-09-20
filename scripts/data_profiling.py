"""
FinTrust Week 1 - Data Analytics Project
Data Profiling Script

Purpose: The purpose is to produce the examine and understand the customers and transaction data.
"""

import pandas as pd

# ---------------------------------------------------------------------
# 1. LOAD THE DATA
# Import the 'Fintrust_Customer_Data.csv' and 'FinTrust_Transaction_Data.csv' from google drive
# ---------------------------------------------------------------------
from google.colab import drive
drive.mount('/content/drive')



customer_path = "/content/drive/MyDrive/ANALYSTLAB MATERIALS/WEEK 1/FinTrust_Customer_Data - FinTrust_Customer_Data.csv"
transaction_path = "/content/drive/MyDrive/ANALYSTLAB MATERIALS/WEEK 1/FinTrust_Transaction_Data - FinTrust_Transaction_Data.csv"

cust = pd.read_csv(customer_path)
txn = pd.read_csv(transaction_path)

print("=" * 60)
print("1. SHAPE — row and column counts")
print("=" * 60)
print(f"Customer data:    {cust.shape[0]} rows, {cust.shape[1]} columns")
print(f"Transaction data: {txn.shape[0]} rows, {txn.shape[1]} columns")

# ---------------------------------------------------------------------
# 2. DATA TYPES —
# ---------------------------------------------------------------------
print("\n" + "=" * 60)
print("2. DATA TYPES")
print("=" * 60)
print("\nCustomer data:\n", cust.dtypes)
print("\nTransaction data:\n", txn.dtypes)

# ---------------------------------------------------------------------
# 3. MISSING VALUES: Finding the missing values in each dataset column-by-column (null-counts)
# ---------------------------------------------------------------------
print("\n" + "=" * 60)
print("3. MISSING VALUES")
print("=" * 60)
print("\nCustomer data:\n", cust.isnull().sum())
print("\nTransaction data:\n", txn.isnull().sum())

# ---------------------------------------------------------------------
# 4. DUPLICATES — Investigating duplicates
# ---------------------------------------------------------------------
print("\n" + "=" * 60)
print("4. DUPLICATES")
print("=" * 60)
print(f"Duplicate Customer_ID values:    {cust['Customer_ID'].duplicated().sum()}")
print(f"Fully duplicate customer rows:   {cust.duplicated().sum()}")
print(f"Duplicate Transaction_ID values: {txn['Transaction_ID'].duplicated().sum()}")
print(f"Fully duplicate transaction rows:{txn.duplicated().sum()}")

# ---------------------------------------------------------------------
# 5. REFERENTIAL INTEGRITY — does every transaction map to a real customer?
# ---------------------------------------------------------------------
orphans = (~txn["Customer_ID"].isin(cust["Customer_ID"])).sum()
print("\n" + "=" * 60)
print("5. JOIN INTEGRITY (Customer_ID)")
print("=" * 60)
print(f"Transaction rows with no matching customer: {orphans}")

# ---------------------------------------------------------------------
# 6. CATEGORICAL BREAKDOWNS — value counts for every text/category column
# ---------------------------------------------------------------------
print("\n" + "=" * 60)
print("6. CATEGORICAL VALUE COUNTS")
print("=" * 60)
for col in cust.select_dtypes(include="object").columns:
    if col not in ("Customer_ID", "Customer_Name"):
        print(f"\nCustomer.{col}:\n{cust[col].value_counts()}")

for col in txn.select_dtypes(include="object").columns:
    if col not in ("Transaction_ID", "Customer_ID", "Transaction_DateTime"):
        print(f"\nTransaction.{col}:\n{txn[col].value_counts()}")

# ---------------------------------------------------------------------
# 7. NUMERIC SUMMARY STATISTICS — mean, median, min, max, spread
# ---------------------------------------------------------------------
print("\n" + "=" * 60)
print("7. NUMERIC SUMMARY STATISTICS")
print("=" * 60)
print("\nCustomer numeric fields:\n", cust.describe())
print("\nAmount_NGN:\n", txn["Amount_NGN"].describe())

# ---------------------------------------------------------------------
# 8. DATE RANGE — confirms the period the transaction data covers
# ---------------------------------------------------------------------
txn["Transaction_DateTime"] = pd.to_datetime(txn["Transaction_DateTime"])
print("\n" + "=" * 60)
print("8. DATE RANGE")
print("=" * 60)
print(f"Earliest transaction: {txn['Transaction_DateTime'].min()}")
print(f"Latest transaction:   {txn['Transaction_DateTime'].max()}")

# ---------------------------------------------------------------------
# 9. CROSS-TABS — the risk patterns behind Part A and Part C
# ---------------------------------------------------------------------
print("\n" + "=" * 60)
print("9. RISK REVIEW RATE BY CHANNEL AND BY INTERNATIONAL FLAG")
print("=" * 60)
print("\nBy channel (%):\n", pd.crosstab(
    txn["Channel"], txn["Risk_Review_Flag"], normalize="index") * 100)
print("\nBy international flag (%):\n", pd.crosstab(
    txn["International_Transaction"], txn["Risk_Review_Flag"], normalize="index") * 100)

# ---------------------------------------------------------------------
# 10. AVERAGE TRANSACTIONS PER CUSTOMER — engagement/frequency KPI input
# ---------------------------------------------------------------------
avg_txn_per_cust = txn.groupby("Customer_ID").size().mean()
print("\n" + "=" * 60)
print("10. AVERAGE TRANSACTIONS PER CUSTOMER")
print("=" * 60)
print(f"Average: {avg_txn_per_cust:.2f}")
