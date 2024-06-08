import numpy as np
import matplotlib.pyplot as plt
from dataset import load_data

df = load_data()

# Before cleaning plots
plt.figure()
df.value.hist()
plt.title("Histogram Before Z-score Cleaning")
plt.savefig("hist_before.png")

plt.figure()
df.boxplot(column="value")
plt.title("Boxplot Before Z-score Cleaning")
plt.savefig("box_before.png")

# Z-score
df["z"] = (df["value"] - df["value"].mean()) / df["value"].std()
df_clean = df[df["z"].abs() < 3]

# After cleaning plots
plt.figure()
df_clean.value.hist()
plt.title("Histogram After Z-score Cleaning")
plt.savefig("hist_after.png")

plt.figure()
df_clean.boxplot(column="value")
plt.title("Boxplot After Z-score Cleaning")
plt.savefig("box_after.png")

print("Before:", len(df))
print("After:", len(df_clean))
