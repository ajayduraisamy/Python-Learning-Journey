# evaluate.py
# Functions to compute model metrics

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix
)
from utils.logger import log

def evaluate_model(model, X_val, y_val):
    preds = model.predict(X_val)
    probs = model.predict_proba(X_val)[:,1]

    acc = accuracy_score(y_val, preds)
    prec = precision_score(y_val, preds)
    rec = recall_score(y_val, preds)
    f1 = f1_score(y_val, preds)
    auc = roc_auc_score(y_val, probs)
    cm = confusion_matrix(y_val, preds)

    log("Accuracy: " + str(acc))
    log("Precision: " + str(prec))
    log("Recall: " + str(rec))
    log("F1 Score: " + str(f1))
    log("ROC-AUC: " + str(auc))
    log("Confusion Matrix: " + str(cm))

    return {
        "acc": acc,
        "prec": prec,
        "rec": rec,
        "f1": f1,
        "auc": auc,
        "cm": cm
    }
