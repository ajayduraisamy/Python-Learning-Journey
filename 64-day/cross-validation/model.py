from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

print("KFold CV:")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores_kf = cross_val_score(RandomForestClassifier(), X, y, cv=kf)
print(scores_kf, "Mean:", scores_kf.mean())

print("\nStratifiedKFold CV:")
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores_skf = cross_val_score(RandomForestClassifier(), X, y, cv=skf)
print(scores_skf, "Mean:", scores_skf.mean())
