import tensorflow as tf

class WarmupSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, peak_lr=0.001, warmup_steps=1000):
        super().__init__()
        self.peak_lr = peak_lr
        self.warmup_steps = warmup_steps

    def __call__(self, step):
        return self.peak_lr * tf.minimum(1.0, step / self.warmup_steps)
