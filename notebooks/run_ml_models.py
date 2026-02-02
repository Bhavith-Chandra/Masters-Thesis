
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Config
DATA_DIR = '/Users/srimanarayana/Thesis Master/Data'
SURVEY_DIR = os.path.join(DATA_DIR, 'INS-W_1/SurveyData')

def run_analysis():
    print("--- 1. Loading Data ---")
    feat_path = os.path.join(DATA_DIR, 'latent_constructs.csv')
    if not os.path.exists(feat_path):
        print("ERROR: latent_constructs.csv not found. Did the previous notebook run successfully?")
        return

    df_features = pd.read_csv(feat_path)
    # Handle unlabeled index column if present (often index 0)
    if 'pid' not in df_features.columns:
        # Check if first column is pid or date
        pass 
    
    # Ensure date is datetime
    if 'date' in df_features.columns:
        df_features['date'] = pd.to_datetime(df_features['date'])

    # Load Targets
    df_target = pd.read_csv(os.path.join(SURVEY_DIR, 'dep_endterm.csv'))
    df_target = df_target[['pid', 'BDI2', 'dep']].dropna(subset=['pid'])

    # Aggregate
    print("--- 2. Aggregating Features per User ---")
    # Drop non-numeric for aggregation, keeping pid for grouping
    numeric_cols = df_features.select_dtypes(include=np.number).columns.tolist()
    # If 'pid' is not in numeric, we need it for groupby
    if 'pid' not in df_features.columns:
        print("Error: 'pid' column missing in latent_constructs.csv")
        return

    df_agg = df_features.groupby('pid')[numeric_cols].agg(['mean', 'std'])
    df_agg.columns = ['_'.join(col).strip() for col in df_agg.columns.values]
    df_agg.reset_index(inplace=True)

    # Merge
    df_final = pd.merge(df_target, df_agg, on='pid', how='inner')
    df_final.set_index('pid', inplace=True)
    print(f"Final Dataset: {df_final.shape} (Users, Features+Targets)")

    # Prepare Data
    X = df_final.drop(columns=['BDI2', 'dep'])
    # Impute/Scale features
    imputer = SimpleImputer(strategy='mean')
    X_clean = imputer.fit_transform(X)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_clean)

    # Targets
    y_score = df_final['BDI2'].fillna(df_final['BDI2'].median())
    y_class = df_final['dep'].map({True: 1, False: 0}).fillna(0)

    # Models
    print("\n--- 3. Training Models (5-Fold CV) ---")
    
    # 1. Linear Regression
    lr = LinearRegression()
    # Using 'neg_mean_squared_error' because 'mse' isn't valid, and 'r2'
    scores_lr = cross_validate(lr, X_scaled, y_score, cv=5, scoring=['r2', 'neg_root_mean_squared_error'])
    r2 = np.mean(scores_lr['test_r2'])
    rmse = -np.mean(scores_lr['test_neg_root_mean_squared_error'])
    print(f"[Linear Regression] Predicting BDI2 Score")
    print(f"   -> R2: {r2:.3f}")
    print(f"   -> RMSE: {rmse:.3f}")

    # 2. SVM
    svm = SVC(kernel='linear')
    scores_svm = cross_validate(svm, X_scaled, y_class, cv=5, scoring=['accuracy', 'f1'])
    print(f"[SVM] Predicting Depression Status (Binary)")
    print(f"   -> Accuracy: {np.mean(scores_svm['test_accuracy']):.3f}")
    print(f"   -> F1 Score: {np.mean(scores_svm['test_f1']):.3f}")

    # 3. Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    scores_rf = cross_validate(rf, X_scaled, y_class, cv=5, scoring=['accuracy', 'f1'])
    print(f"[Random Forest] Predicting Depression Status (Binary)")
    print(f"   -> Accuracy: {np.mean(scores_rf['test_accuracy']):.3f}")
    print(f"   -> F1 Score: {np.mean(scores_rf['test_f1']):.3f}")

    # 4. KNN
    knn = KNeighborsClassifier(n_neighbors=5)
    scores_knn = cross_validate(knn, X_scaled, y_class, cv=5, scoring=['accuracy', 'f1'])
    print(f"[KNN] Predicting Depression Status (Binary)")
    print(f"   -> Accuracy: {np.mean(scores_knn['test_accuracy']):.3f}")
    print(f"   -> F1 Score: {np.mean(scores_knn['test_f1']):.3f}")

if __name__ == "__main__":
    run_analysis()
