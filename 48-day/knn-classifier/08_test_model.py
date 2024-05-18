# 08_test_model.py
# Test model training

from 01_dataset import get_train_test
from 02_model import train_model

def test_model():
    X_train, X_test, y_train, y_test = get_train_test()
    model = train_model(X_train, y_train)
    assert hasattr(model, "predict")
