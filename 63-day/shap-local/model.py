from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import shap
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

print("SHAP Local Explanation for first sample:")
shap.force_plot(explainer.expected_value[1], shap_values[1][0], X_test.iloc[0], show=False)
