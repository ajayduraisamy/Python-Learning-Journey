import tensorflow as tf
from model.gpt_rope import GPTRoPE
from loaders.dataset_bpe import GPTBPEdataset

def main():
    ds = GPTBPEdataset("data/tiny.txt")
    dataset = ds.tf_dataset()

    model = GPTRoPE(
        vocab_size=len(ds.vocab),
        d_model=64,
        num_heads=4,
        d_ff=128,
        num_layers=2
    )

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    opt = tf.keras.optimizers.AdamW(1e-3)

    for epoch in range(5):
        print(f"Epoch {epoch+1}")
        for x, y in dataset:
            with tf.GradientTape() as tape:
                logits = model(x)
                loss = loss_fn(y, logits)

            grads = tape.gradient(loss, model.trainable_variables)
            opt.apply_gradients(zip(grads, model.trainable_variables))

        print("Loss:", loss.numpy())

    model.save_weights("gpt_bpe.h5")
    print("Model saved")

if __name__ == "__main__":
    main()
