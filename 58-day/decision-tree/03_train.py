# 03_train.py
# Train decision tree + generate visualizations

from 01_dataset_utils import get_train_test, save_output
from 02_model import train_tree, export_tree_graphviz, plot_feature_importance

def main():
    X_train, X_test, y_train, y_test = get_train_test()

    print("Training decision tree...")
    model = train_tree(X_train, y_train)

    print("Generating Graphviz tree image...")
    export_tree_graphviz(model, X_train.columns)

    print("Saving feature importance plot...")
    fig = plot_feature_importance(model, X_train.columns)
    save_output("outputs/feature_importance.png", fig)

if __name__ == "__main__":
    main()
