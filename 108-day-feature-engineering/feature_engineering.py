import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.DataFrame({
    "age": [20, 30, 40],
    "salary": [20000, 40000, 60000],
    "city": ["A", "B", "A"]
})

scaler = StandardScaler()
df[["age", "salary"]] = scaler.fit_transform(df[["age", "salary"]])

encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(df[["city"]])

print(df)
print(encoded)
