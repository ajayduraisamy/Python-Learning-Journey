import tensorflow as tf
from utils.sampling import sample_next_token

def generate_text(model, start_tokens, max_new_tokens=20, temperature=1.0, top_k=None, top_p=None):
    tokens = tf.identity(start_tokens)

    for _ in range(max_new_tokens):
        logits = model(tokens)
        last_logits = logits[:, -1, :]

        next_token = sample_next_token(
            last_logits,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
        )

        tokens = tf.concat([tokens, next_token], axis=1)

    return tokens
