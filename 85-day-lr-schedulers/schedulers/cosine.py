import tensorflow as tf
import math

class CosineAnnealing(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, max_lr=0.001, min_lr=1e-5, T=1000):
        self.max_lr = max_lr
        self.min_lr = min_lr
        self.T = T

    def __call__(self, step):
        cosine = 0.5 * (1 + tf.cos(math.pi * step / self.T))
        return self.min_lr + (self.max_lr - self.min_lr) * cosine
