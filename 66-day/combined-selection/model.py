from sklearn.feature_selection import f_classif, chi2
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from dataset import load_data
import pandas as pd

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

print("\n=== ANOVA ===")
F_vals, p_vals = f_classif(X, y)
print(pd.Series(F_vals, index=X.columns))

print("\n=== Chi-Square (scaled) ===")
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
chi_vals, p_vals2 = chi2(X_scaled, y)
print(pd.Series(chi_vals, index=X.columns))

print("\n=== RFE ===")
rfe = RFE(LogisticRegression(max_iter=500), n_features_to_select=2)
rfe.fit(X, y)
print(pd.Series(rfe.support_, index=X.columns))

print("\n=== RandomForest Importance ===")
rf = RandomForestClassifier(n_estimators=200)
rf.fit(X, y)
print(pd.Series(rf.feature_importances_, index=X.columns))
