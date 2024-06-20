# Transfer Learning Notes (DL Day 8)

### What is Transfer Learning?
Using knowledge learned from a large dataset (ImageNet) and applying it to a smaller dataset.

### Why VGG16?
- Simple architecture
- Good feature extractor
- Widely used for teaching TL

### Why freeze base layers?
We reuse pre-learned features:
- edges
- shapes
- textures

We only train the classifier head.

### Benefits:
- Faster training
- Requires less data
- Higher accuracy
