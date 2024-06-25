# Depthwise Separable Convolution (MobileNet)

### Standard Conv:
- Applies N filters across all channels
- Costly: K*K*C_in*C_out

### Depthwise Convolution:
- One filter per channel (C_in filters)
- Much cheaper: K*K*C_in

### Pointwise Convolution (1x1):
- Combines depthwise outputs
- Cost: C_in*C_out

### Total cost = K*K*C_in + C_in*C_out
Much cheaper than normal convolution!

Used in:
- MobileNet
- EfficientNet
- Lightweight CNN models
