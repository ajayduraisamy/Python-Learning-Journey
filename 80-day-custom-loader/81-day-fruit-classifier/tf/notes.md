# Fruit Classifier (Day 10)

### Why MobileNetV2?
- Lightweight
- Fast training
- Good accuracy for small datasets

### Pipeline:
1. Load images from folders
2. Apply batching, shuffling, prefetching
3. Freeze MobileNetV2 base
4. Train classification head
5. Save best model
