import kagglehub
import json
import pandas as pd
import os

filelink_ = kagglehub.dataset_download("zhengyiling/rollingsales")
filepath_ = os.path.join(filelink_, "rollingsales_queens.csv")

df = pd.read_csv(filepath_)

important_cols = ["NEIGHBORHOOD", "ADDRESS", "APARTMENT NUMBER", "EASEMENT", "LAND SQUARE FEET", "SALE PRICE", "SALE DATE"]

# Ask Pandas for a full column report
df_info = df.info()

# Ask Pandas to count the missing values prescisely
df_missing = df.isnull().sum()

print(df.shape)