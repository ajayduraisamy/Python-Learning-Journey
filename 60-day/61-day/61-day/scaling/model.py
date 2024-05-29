from sklearn.preprocessing import StandardScaler, MinMaxScaler
from dataset import load_data

df = load_data()

std = StandardScaler()
minmax = MinMaxScaler()

print("Standard Scaled:")
print(std.fit_transform(df)[:3])

print("\nMinMax Scaled:")
print(minmax.fit_transform(df)[:3])
