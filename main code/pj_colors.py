import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


common_colors = ["black", "white", "red", "green", "yellow",
                 "blue", "brown", "orange", "pink", "purple", "gray"]


df = pd.read_csv('complete_data.csv')


for colors in common_colors:

    df_colors = df.loc[df['c'] == colors]

    r = pd.to_numeric(df_colors['R'])
    g = pd.to_numeric(df_colors['G'])
    b = pd.to_numeric(df_colors['B'])

    c = np.column_stack((r, g, b))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(r, g, b, c=c/255.0)
    plt.title(colors)
    plt.show()
