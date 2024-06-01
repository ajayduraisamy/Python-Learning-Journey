from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import shap
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

print("SHAP Global Explanation:")
shap.summary_plot(shap_values[1], X, show=False)
