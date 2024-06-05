from sklearn.impute import SimpleImputer, KNNImputer
from dataset import load_data

df = load_data()
print("Original Data:")
print(df)

# Mean imputation
mean_imp = SimpleImputer(strategy="mean")
mean_filled = mean_imp.fit_transform(df)
print("\nMean Imputed:")
print(mean_filled[:10])

# Median imputation
median_imp = SimpleImputer(strategy="median")
median_filled = median_imp.fit_transform(df)
print("\nMedian Imputed:")
print(median_filled[:10])

# KNN imputation
knn = KNNImputer(n_neighbors=3)
knn_filled = knn.fit_transform(df)
print("\nKNN Imputed:")
print(knn_filled[:10])
