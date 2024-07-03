import tensorflow as tf
from model.gpt_mini import GPTMini
from loaders.dataset import GPTDataset
from utils.generate import generate_text

def main():
    ds = GPTDataset("data/tiny.txt", seq_len=10)
    dataset = ds.get_tf_dataset(batch_size=4)

    vocab_size = len(ds.vocab)

    model = GPTMini(
        vocab_size=vocab_size,
        d_model=64,
        num_heads=4,
        d_ff=128,
        num_layers=2,
        max_len=20
    )

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

    for epoch in range(5):
        print(f"Epoch {epoch+1}")

        for x, y in dataset:
            with tf.GradientTape() as tape:
                logits = model(x)
                loss = loss_fn(y, logits)

            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

        print("Loss:", loss.numpy())

    model.save_weights("gpt-mini.h5")
    print("Model saved.")

    # Demo generation
    start_word = ds.word2id["hello"]
    output = generate_text(model, tf.constant([[start_word]]), max_new_tokens=10)
    print("Generated token IDs:", output.numpy())

if __name__ == "__main__":
    main()
