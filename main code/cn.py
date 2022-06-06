import numpy as np
import pandas as pd



df = pd.read_csv('complete_data.csv')
df_cn = df['c']
df_cn.to_csv("cn.csv",index=False)