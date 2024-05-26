# 02_model.py
# Train logistic regression + generate decision boundary plot

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def plot_decision_boundary(model, X, y):
    fig = plt.figure()

    # Scatter points
    plt.scatter(X.iloc[:,0], X.iloc[:,1], c=y, cmap="coolwarm")

    # Meshgrid
    x_min, x_max = X.iloc[:,0].min()-1, X.iloc[:,0].max()+1
    y_min, y_max = X.iloc[:,1].min()-1, X.iloc[:,1].max()+1

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 200),
        np.linspace(y_min, y_max, 200)
    )

    grid = np.c_[xx.ravel(), yy.ravel()]
    preds = model.predict(grid).reshape(xx.shape)

    plt.contourf(xx, yy, preds, alpha=0.3, cmap="coolwarm")
    plt.title("Decision Boundary (Logistic Regression)")

    return fig
