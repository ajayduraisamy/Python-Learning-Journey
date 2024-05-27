import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model

def plot_confusion_matrix(model, X, y):
    preds = model.predict(X)
    cm = confusion_matrix(y, preds)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    return fig
