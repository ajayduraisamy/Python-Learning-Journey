import tensorflow as tf
from xor.data import load_xor
from xor.model_tf import build_model, compile_model

X, y = load_xor()

model = build_model()
model = compile_model(model)

model.fit(X, y, epochs=500, verbose=0)

print("Final predictions:")
print(model.predict(X).round())

model.save("xor_tf_model.h5")
print("Model saved as xor_tf_model.h5")
