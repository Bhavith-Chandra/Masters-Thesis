
import pandas as pd
import numpy as np
import glob
import os
import sys
import subprocess

# 1. Check Dependencies
try:
    import causal_learn
    print("[OK] causal-learn is installed.")
except ImportError:
    print("[ERROR] causal-learn is NOT installed.")

try:
    import seaborn
    print("[OK] seaborn is installed.")
except ImportError:
    print("[ERROR] seaborn is NOT installed.")

# 2. Check Data Path
DATA_DIR = '../Data'
if not os.path.exists(DATA_DIR):
    # Try absolute path based on known user path
    DATA_DIR = '/Users/srimanarayana/Thesis Master/Data'
    
print(f"Using Data Directory: {DATA_DIR}")
if not os.path.exists(DATA_DIR):
    print(f"[ERROR] Data directory not found at {DATA_DIR}")
else:
    print(f"[OK] Data directory exists. Contents: {os.listdir(DATA_DIR)}")

# 3. Test Data Loading (Small scale)
def test_load():
    print("Testing One File Load...")
    # diverse pattern to catch at least one file
    pattern = os.path.join(DATA_DIR, 'INS-W_*', 'FeatureData', '*.csv')
    files = glob.glob(pattern)
    if not files:
        print("[ERROR] No feature files found matching pattern!")
        return
    
    first_file = files[0]
    print(f"Loading {first_file}...")
    try:
        df = pd.read_csv(first_file, nrows=100) # Read only 100 rows
        print(f"[OK] Loaded successfully. Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()[:5]}...")
    except Exception as e:
        print(f"[ERROR] Failed to read CSV: {e}")

test_load()
