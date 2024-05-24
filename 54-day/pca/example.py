from 03_train import main as train_main
from 02_model import load_pca, transform_data
import pandas as pd

train_main()
pca = load_pca()
df = pd.DataFrame([[0.5, 0.3, 0.9]], columns=["feature1","feature2","feature3"])
print("Example PCA:", transform_data(pca, df)[0])
