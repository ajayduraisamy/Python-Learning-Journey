import pandas as pd
import matplotlib.pyplot as plt
from dataset import load_data

df = load_data()

# Visualization before cleaning
plt.figure()
df["value"].hist()
plt.title("Histogram Before IQR Cleaning")
plt.savefig("hist_before.png")

plt.figure()
df.boxplot(column="value")
plt.title("Boxplot Before IQR Cleaning")
plt.savefig("box_before.png")

Q1 = df["value"].quantile(0.25)
Q3 = df["value"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df["value"] >= lower) & (df["value"] <= upper)]

# After cleaning
plt.figure()
df_clean["value"].hist()
plt.title("Histogram After IQR Cleaning")
plt.savefig("hist_after.png")

plt.figure()
df_clean.boxplot(column="value")
plt.title("Boxplot After IQR Cleaning")
plt.savefig("box_after.png")

print("Before:", len(df))
print("After:", len(df_clean))
