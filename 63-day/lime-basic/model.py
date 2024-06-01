from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from lime.lime_tabular import LimeTabularExplainer
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1).values
y = df["label"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

explainer = LimeTabularExplainer(
    X_train,
    feature_names=["f1","f2","f3","f4"],
    class_names=["Class0", "Class1"],
    verbose=True
)

exp = explainer.explain_instance(X_test[0], model.predict_proba)
print("LIME Explanation:")
print(exp.as_list())
