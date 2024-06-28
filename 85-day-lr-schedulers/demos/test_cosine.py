import matplotlib.pyplot as plt
import tensorflow as tf
from schedulers.cosine import CosineAnnealing

steps = tf.range(0, 2000)
schedule = CosineAnnealing(max_lr=0.001, min_lr=1e-5, T=1000)
lrs = [schedule(step).numpy() for step in steps]

plt.plot(steps, lrs)
plt.title("Cosine Annealing LR")
plt.xlabel("Step")
plt.ylabel("LR")
plt.show()
