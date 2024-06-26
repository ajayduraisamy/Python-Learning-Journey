# Learning Rate Schedulers (Warmup, Cosine Annealing, Cyclical)

### Why scheduling?
- Too high LR → divergence
- Too low LR → slow training
- Good schedules → faster, stable convergence

---

## 1️⃣ Warmup LR (Transformers)
Start small → gradually increase → avoid unstable updates.

---

## 2️⃣ Cosine Annealing LR
LR follows cosine curve:
High → low → high → low cycles

Used in:
- EfficientNet
- YOLOv5
- Many modern CNNs

---

## 3️⃣ Cyclical LR (CLR)
LR oscillates between low & high.
Helps escape sharp local minima.
