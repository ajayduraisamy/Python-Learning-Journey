import tensorflow as tf

def apply_temperature(logits, temperature):
    if temperature <= 0:
        return logits
    return logits / temperature

def top_k_sampling(logits, k=5):
    values, indices = tf.math.top_k(logits, k=k)
    probs = tf.nn.softmax(values)
    sample = tf.random.categorical(tf.math.log(probs), num_samples=1)
    return tf.gather(indices, sample, batch_dims=1)

def top_p_sampling(logits, p=0.9):
    sorted_logits = tf.sort(logits, direction="DESCENDING")
    sorted_indices = tf.argsort(logits, direction="DESCENDING")

    probs = tf.nn.softmax(sorted_logits)
    cumulative = tf.cumsum(probs, axis=-1)

    mask = cumulative > p
    first_mask = tf.concat([tf.zeros_like(mask[:, :1]), mask[:, :-1]], axis=-1)

    filtered_logits = tf.where(first_mask, tf.float32.min, sorted_logits)
    probs = tf.nn.softmax(filtered_logits)

    sample = tf.random.categorical(tf.math.log(probs), 1)
    return tf.gather(sorted_indices, sample, batch_dims=1)

def sample_next_token(logits, temperature=1.0, top_k=None, top_p=None):
    logits = apply_temperature(logits, temperature)

    if top_k is not None:
        return top_k_sampling(logits, top_k)

    if top_p is not None:
        return top_p_sampling(logits, top_p)

    # default greedy
    return tf.argmax(logits, axis=-1, output_type=tf.int32)
