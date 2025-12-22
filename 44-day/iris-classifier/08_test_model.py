# 08_test_model.py
# Basic test to ensure training produces a model and that predict works

from 01_data import get_train_test
from 02_model import train_model, evaluate_model

def test_train_and_eval():
    X_train, X_test, y_train, y_test = get_train_test()
    model = train_model(X_train, y_train, n_estimators=10)
    acc, report = evaluate_model(model, X_test, y_test)
    assert acc > 0.5  # rough sanity check
