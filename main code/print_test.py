import pandas as pd
df = pd.read_csv('dict/NBS-ISCC-rgb.csv')
df = df.drop(columns = ["Centroids", "http://tx4.us/nbs-iscc.htm"])
df = df.rename(columns={'Unnamed: 0' : 'R', 'NBS/ISCC' : 'G', 'Color': 'B', 'System': 'ColorName'})
df = df.drop(df.index[range(0, 9)])
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.reset_index(drop=True)


#colorNames = df['ColorName']
#nbs = colorNames.to_numpy()
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]
NBS =  df
df.columns = ['ColorName', 'R', 'G', 'B']
colorNames = df['ColorName']
labels = colorNames.to_numpy()
labels
import matplotlib.pyplot as plt
r = pd.to_numeric(df['R'])
g = pd.to_numeric(df['G']) 
b = pd.to_numeric(df['B'])
c = 65536*r+ 256*g + b
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(r, g, b, c = c)
plt.show()