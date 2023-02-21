#!/usr/bin/env python

# First day version (21.02.2023): all files are created manually,
# funny dictionary implementation for matching the data.
# Try working with class "value_on_figure".

import pandas as pd
import matplotlib.pyplot as plt
from mpl_point_clicker import clicker


def label_point(x, y, val, ax):
    a = pd.concat({'x': x + 10, 'y': y + 10, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))


class value_on_figure():
    __name = None
    aliases = []
    x = None
    y = None
    expression = None
    exist = None

    def __init__(self, name="Gene", aliases=[], x=0.0, y=0.0, expression=None,
                 exist=0):  # better not to repeat the attribute names for parameters
        self.name = name
        self.aliases = aliases
        self.x = x
        self.y = y
        self.expression = expression
        self.exist = exist

    def __str__(self):  # A method to output object as a string.
        # print(nds) explicitly is working as print(nds.__str__()
        # it is better to always write it ourselves, otherwise the output would be standard for al objects.
        return f" {self.name}: Aliases = {self.aliases}, coordinates = {self.x}, {self.y}"


# ---------------------------------------------------------------
# Find locations on the image for annotation
def close_on_click(event):
    plt.close()


def find_coords():
    image = plt.imread("C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/Picture1.png")
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    klicker = clicker(ax, ['genes'], markers=['o'])
    # close the window automatically after the first click
    fig.canvas.mpl_connect('button_press_event', close_on_click)
    plt.show()

    # Get x and y values for approximate label placement
    for coords in klicker.get_positions().values():
        for x, y in coords:
            # print(f"{x:.2f},{y:.2f}")
            return x, y


def find_gene_IDs_in_instances(file, insts):
    with open(file) as fin:
        rows = (line.strip('\n').split('\t') for line in fin)
        input_values = {row[0]: float(row[1]) for row in rows}

    print(input_values)

    for k, v in input_values.items():
        for instance in insts:
            if k.upper() in instance.aliases:
                print(v)
                instance.expression = v
                instance.exist = 1


def plot_coords(data_inp):
    nan_data = data_inp[data_inp['Expression'].isnull()]
    data = data_inp[data_inp['Expression'].notnull()]

    img = plt.imread("C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/Picture1bw.png")
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


if __name__ == "__main__":
    try:
        df = pd.read_csv('data.csv')
        plot_coords(df)
    except:
        instances = [
            value_on_figure("GABAB3", ["GABAB3b", "GABAB3a", "GABAB3"]),
            value_on_figure("RGS12", ["RGS12"]),
            value_on_figure("Fake", ["nope"]),
            value_on_figure("GABAB1", ["GABAB1", "GABAB1a"]),
            value_on_figure("GAD-67", ["GAD67"])
        ]

        for instance in instances:
            print(instance.name)
            """ Block this if do not want to chose"""
            gene_coord = find_coords()
            print(gene_coord[0], gene_coord[1])
            instance.x = gene_coord[0]
            instance.y = gene_coord[1]
            """"""

        file = "C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder/fake_values.txt"
        find_gene_IDs_in_instances(file, instances)
        for instance in instances:
            print(instance.name)

        genes = []
        aliases = []
        xs = []
        ys = []
        expressions = []
        for instance in instances:
            genes.append(instance.name)
            aliases.append(instance.aliases)
            xs.append(instance.x)
            ys.append(instance.y)
            expressions.append(instance.expression)

        # create a dictionary
        dict_for_pd = {
            'Genes': genes,
            'Aliases': aliases,
            'x': xs,
            'y': ys,
            'Expression': expressions,
            'Exist': [1] * len(xs)
        }

        df = pd.DataFrame(dict_for_pd)
        print(df)
        df.to_csv('data.csv')
        plot_coords(df)
