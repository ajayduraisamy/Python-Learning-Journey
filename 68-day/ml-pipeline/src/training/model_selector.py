# model_selector.py
# Select best model using ROC-AUC

from utils.logger import log

def choose_best_model(results):
    best_model = None
    best_auc = 0

    for name, data in results.items():
        auc = data["metrics"]["auc"]
        log(f"Model {name} AUC = {auc}")

        if auc > best_auc:
            best_auc = auc
            best_model = name

    log(f"Best model = {best_model} with AUC = {best_auc}")
    return best_model
