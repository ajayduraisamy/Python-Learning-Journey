import numpy as np
import matplotlib.pyplot as plt
from dataset import load_data

df = load_data()

plt.figure()
df.value.hist()
plt.title("Histogram Before Winsorizing")
plt.savefig("hist_before.png")

plt.figure()
df.boxplot(column="value")
plt.title("Boxplot Before Winsorizing")
plt.savefig("box_before.png")

# Winsorizing
lower = df["value"].quantile(0.01)
upper = df["value"].quantile(0.99)
df["clean"] = df["value"].clip(lower, upper)

plt.figure()
df.clean.hist()
plt.title("Histogram After Winsorizing")
plt.savefig("hist_after.png")

plt.figure()
df.boxplot(column="clean")
plt.title("Boxplot After Winsorizing")
plt.savefig("box_after.png")

print("Before range:", df["value"].min(), df["value"].max())
print("After range:", df["clean"].min(), df["clean"].max())
