from cnn.data import load_mnist
from cnn.model_tf import build_cnn

(X_train, y_train), (X_test, y_test) = load_mnist()
model = build_cnn()

model.fit(X_train, y_train, epochs=3, validation_split=0.1)

print("Evaluating on test set:")
loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc}")

model.save("mnist_cnn.h5")
print("Model saved as mnist_cnn.h5")
