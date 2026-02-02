import pandas as pd
import glob
import os

data_dir = '/Users/srimanarayana/Thesis Master/Data/INS-W_1/FeatureData'
files = glob.glob(os.path.join(data_dir, '*.csv'))

with open('columns_report.txt', 'w') as f:
    for file in files:
        f.write(f"\n--- {os.path.basename(file)} ---\n")
        try:
            df = pd.read_csv(file, nrows=1)
            f.write(str(df.columns.tolist()))
        except Exception as e:
            f.write(f"Error: {e}")
