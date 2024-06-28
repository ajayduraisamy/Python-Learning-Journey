import matplotlib.pyplot as plt
import tensorflow as tf
from schedulers.warmup import WarmupSchedule

steps = tf.range(0, 2000)
schedule = WarmupSchedule(peak_lr=0.001, warmup_steps=1000)
lrs = [schedule(step).numpy() for step in steps]

plt.plot(steps, lrs)
plt.title("Warmup Learning Rate")
plt.xlabel("Step")
plt.ylabel("LR")
plt.show()
