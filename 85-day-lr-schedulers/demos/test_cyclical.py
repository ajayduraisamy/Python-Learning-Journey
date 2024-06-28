import matplotlib.pyplot as plt
import tensorflow as tf
from schedulers.cyclical import CyclicalLR

steps = tf.range(0, 3000)
schedule = CyclicalLR(min_lr=1e-5, max_lr=1e-3, step_size=500)
lrs = [schedule(step).numpy() for step in steps]

plt.plot(steps, lrs)
plt.title("Cyclical Learning Rate")
plt.xlabel("Step")
plt.ylabel("LR")
plt.show()
