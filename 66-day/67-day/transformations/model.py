import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import boxcox, yeojohnson
from dataset import load_data

df = load_data()

plt.figure()
df.value.hist()
plt.title("Histogram Before Transformations")
plt.savefig("hist_before.png")

# Log Transform (add 1 to avoid log(0))
df["log"] = np.log1p(df["value"])

# Box-Cox (positive only)
df["boxcox"], _ = boxcox(df["value"])

# Yeo-Johnson (allows negative)
df["yj"], _ = yeojohnson(df["value"])

plt.figure()
df["log"].hist()
plt.title("After Log Transform")
plt.savefig("hist_log.png")

plt.figure()
df["boxcox"].hist()
plt.title("After Box-Cox Transform")
plt.savefig("hist_boxcox.png")

plt.figure()
df["yj"].hist()
plt.title("After Yeo-Johnson Transform")
plt.savefig("hist_yj.png")

print("Skewness Before:", df["value"].skew())
print("Skewness Log:", df["log"].skew())
print("Skewness BoxCox:", df["boxcox"].skew())
print("Skewness Yeo-Johnson:", df["yj"].skew())
