import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay

def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model

def plot_roc(model, X, y):
    fig, ax = plt.subplots()
    RocCurveDisplay.from_estimator(model, X, y, ax=ax)
    ax.set_title("ROC Curve")
    return fig
