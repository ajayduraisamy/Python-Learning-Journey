from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from lime.lime_tabular import LimeTabularExplainer
import shap
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# SHAP
explainer_shap = shap.TreeExplainer(model)
shap_values = explainer_shap.shap_values(X_test)

print("SHAP summary for comparison:")
shap.summary_plot(shap_values[1], X_test, show=False)

# LIME
lime = LimeTabularExplainer(
    X_train.values,
    feature_names=X_train.columns,
    class_names=["0","1"]
)
exp = lime.explain_instance(X_test.values[0], model.predict_proba)
print("LIME Explanation:", exp.as_list())
