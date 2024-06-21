# DL Day 9 — Custom Image Loader Notes

### Why directories?
Real datasets are stored in folders like:
dataset/
    class1/
    class2/
    ...

### image_dataset_from_directory:
Automatically:
- Reads image files
- Labels them by folder name
- Builds batches
- Splits train/validation

### tf.data Pipeline:
- Shuffle → randomization
- Batch → group samples
- Prefetch → improve performance

### Preprocessing:
- Rescaling converts pixel values (0–255) → (0–1)
