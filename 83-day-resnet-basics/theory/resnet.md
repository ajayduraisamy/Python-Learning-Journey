# ResNet Basics — Why Residual Learning?

### Deep Networks Problem:
As networks became deeper:
- Training accuracy got WORSE
- Gradients vanished or exploded
- Optimization became impossible

### Solution: Residual Block
Instead of learning F(x), learn:
    y = F(x) + x

This "skip connection" gives:
- Better gradient flow
- Faster convergence
- Ability to train 50, 101, 152 layer nets

### Identity Block:
x → Conv → BN → ReLU → Conv → BN → ADD(x) → ReLU

### Projection Shortcut:
Used when shapes differ:
    x → Conv1x1 → match shape → ADD → ReLU
