from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from dataset import load_data
import pandas as pd

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

model = LogisticRegression(max_iter=500)
selector = RFE(model, n_features_to_select=3)
selector.fit(X, y)

print("Selected Features:")
print(pd.Series(selector.support_, index=X.columns))

print("\nFeature Ranking:")
print(pd.Series(selector.ranking_, index=X.columns))
