import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('visualize_data.csv')
#c = pd.to_numeric(df['c'])
c = df['c'].to_numpy()
r = pd.to_numeric(df['R'])
g = pd.to_numeric(df['G']) 
b = pd.to_numeric(df['B'])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(r, g, b,c = c)
plt.show()
