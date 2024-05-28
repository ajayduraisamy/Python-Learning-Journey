# 02_model.py
# Decision Tree + Graphviz export + feature importance plot

import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, export_graphviz

def train_tree(X_train, y_train):
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    return model

def export_tree_graphviz(model, feature_names, dot_path="outputs/tree.dot", png_path="outputs/tree.png"):
    os.makedirs("outputs", exist_ok=True)

    export_graphviz(
        model,
        out_file=dot_path,
        feature_names=feature_names,
        class_names=["0","1"],
        filled=True,
        rounded=True
    )

    # Convert DOT → PNG using Graphviz
    os.system(f"dot -Tpng {dot_path} -o {png_path}")
    print("Saved tree visualization:", png_path)

def plot_feature_importance(model, feature_names):
    importance = model.feature_importances_
    fig, ax = plt.subplots()
    sns.barplot(x=importance, y=feature_names, ax=ax)
    ax.set_title("Feature Importance")
    return fig
