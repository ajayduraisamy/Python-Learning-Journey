import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import yeojohnson
from dataset import load_data

df = load_data()

# Before
plt.figure()
df.value.hist()
plt.title("Before Cleaning")
plt.savefig("before.png")

# Step 1 — IQR remove
Q1, Q3 = df.value.quantile([0.25, 0.75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
df_clean = df[(df.value >= lower) & (df.value <= upper)]

# Step 2 — Yeo-Johnson
df_clean["yj"], _ = yeojohnson(df_clean["value"])

# After
plt.figure()
df_clean.yj.hist()
plt.title("After Cleaning + Yeo-Johnson")
plt.savefig("after.png")

print("Original size:", len(df))
print("After cleaning:", len(df_clean))
print("Skew before:", df["value"].skew())
print("Skew after:", df_clean["yj"].skew())
