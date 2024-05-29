from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
from dataset import load_data

df = load_data()

# Label encoding
le = LabelEncoder()
df["color_label"] = le.fit_transform(df["color"])

print("Label Encoded:")
print(df)

# OneHot Encoding
ohe = OneHotEncoder(sparse_output=False)
ohe_result = ohe.fit_transform(df[["size"]])

print("\nOneHot Encoded:")
print(pd.DataFrame(ohe_result, columns=ohe.get_feature_names_out()))
