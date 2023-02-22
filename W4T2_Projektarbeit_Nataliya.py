#!/usr/bin/env python

# First day version (21.02.2023): all files are created manually,
# funny dictionary implementation for matching the data.
# Try working with class "value_on_figure".

import pandas as pd
import matplotlib.pyplot as plt
from mpl_point_clicker import clicker


def label_point(x, y, val, ax):
    a = pd.concat({'x': x+10, 'y': y+10, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))


# ---------------------------------------------------------------
# Find locations on the image for annotation

image = plt.imread("C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/Picture1.png")
fig, ax = plt.subplots()
ax.imshow(image, cmap='gray')
klicker = clicker(ax, ['genes'], markers=['o'])
plt.show()

# Get x and y values for approximate label placement
for coords in klicker.get_positions().values():
    for x,y in coords:
        print(f"{x:.2f},{y:.2f}")

# Insert the x, y values into genes_coords.txt

# ---------------------------------------------------------------
# Upload f

file1 = "C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/fake_values.txt"

with open(file1) as fin:
    rows = (line.strip('\n').split('\t') for line in fin)
    input_values = {row[0]: float(row[1]) for row in rows}

print(input_values)

file2 = "C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/genes_names.txt"

with open(file2) as fin:
    rows = (line.strip('\n').split('\t') for line in fin)
    genes_names = {row[0]: row[1].split(',') for row in rows}

print(genes_names)

file3 = "C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/genes_coords.txt"

with open(file3) as fin:
    rows = (line.strip('\n').split('\t') for line in fin)
    genes_coords = {row[0]: row[1].split(',') for row in rows}

print(genes_coords)

dict_fig = dict()
for k, v in input_values.items():
    for genes_fig, gene_IDs in genes_names.items():
        if k.upper() in gene_IDs:
            dict_fig[genes_fig] = v
print(dict_fig)

for k, v in genes_coords.items():
    for genes_fig, gene_IDs in dict_fig.items():
        if k in genes_fig:
            # print(v)
            dict_fig[genes_fig] = [dict_fig[genes_fig], v]
            flat_list = []
            for item in dict_fig[genes_fig][1]:
                flat_list.append(float(item))
            flat_list.append(dict_fig[genes_fig][0])
            flat_list.append(0.7)
            dict_fig[genes_fig] = flat_list
    if k not in dict_fig.keys():
        flat_list = []
        for item in genes_coords[k]:
            flat_list.append(float(item))
        flat_list.append(None)
        flat_list.append(0.0)
        dict_fig[k] = flat_list

print(dict_fig)

data = pd.DataFrame(dict_fig).T
data = data.rename(columns={0: 'x', 1: 'y', 2: 'Expression', 3: 'Exist'})
data = data.rename_axis("Genes").reset_index()
nan_data = data[data['Expression'].isnull()]
print(nan_data.head())
data = data[data['Expression'].notnull()]
print(data.head())


img = plt.imread("C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/Picture1.png")
fig, ax = plt.subplots()
ax.imshow(img)  # , extent=[0, 500, 0, 500]
data.plot(kind='scatter', x='x', y='y', s=100,
          c=data['Expression'], alpha=data['Exist'],
          edgecolors='black', linewidths=1,
          # colorbar=True,
          title='Genes', ax=ax)
nan_data.plot(kind='scatter', x='x', y='y', s=100,
              fc=(0.3, 0.3, 0.3, 0.7),
              edgecolors='black', linewidths=1, ax=ax)

label_point(data.x, data.y, data.Genes, ax)
label_point(nan_data.x, nan_data.y, nan_data.Genes, ax)

plt.show()

