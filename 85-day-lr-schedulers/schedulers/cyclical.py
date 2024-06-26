import tensorflow as tf

class CyclicalLR(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, min_lr=1e-5, max_lr=1e-3, step_size=500):
        self.min_lr = min_lr
        self.max_lr = max_lr
        self.step_size = step_size

    def __call__(self, step):
        cycle = tf.floor(1 + step / (2 * self.step_size))
        x = tf.abs(step / self.step_size - 2 * cycle + 1)
        lr = self.min_lr + (self.max_lr - self.min_lr) * tf.maximum(0.0, (1 - x))
        return lr
