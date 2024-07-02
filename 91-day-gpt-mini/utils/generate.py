import tensorflow as tf

def generate_text(model, start_tokens, max_new_tokens=20):
    tokens = tf.identity(start_tokens)

    for _ in range(max_new_tokens):
        logits = model(tokens)
        next_token_logits = logits[:, -1, :]  # last token's prediction
        next_token = tf.argmax(next_token_logits, axis=-1, output_type=tf.int32)
        next_token = tf.reshape(next_token, (1, 1))
        tokens = tf.concat([tokens, next_token], axis=1)

    return tokens
