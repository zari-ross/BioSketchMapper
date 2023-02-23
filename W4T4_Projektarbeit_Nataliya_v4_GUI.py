#!/usr/bin/env python

# Third day version (23.02.2023):
# 1) Experiment that gives values for large number of entities that could be
# represented with a color-code (proteomics or transcriptomics experiment)
# 2) Idea of a pathway that needs to be
# represented - sketch or copy of a textbook figure
# 3) Preliminary list of entities for the figure, e.g.,
# genes or categories of genes
# 4) Automatic pathway to look for all the genes for this category (searching through a
# proteomics database using keywords)
# 5) Going back to manually affirming all the entities and all the genes or aliases that pass to them
# 6) Creating classes for all the final entities. Class attributes are: name,
# list of aliases, coordinates on the figure: x and y, expression at first None  - changes if found on the dataset
# 7) Going through all the entities to find preliminary coordinates on the plot (should it be approximated automatically
# to some kind of grid of 10, for example?)
# 8) Saving the coordinates and working with that file from there only
# 9)Matching the entities with the value that needs to be color-coded
# 10) Final plot - export in svg-format to be able to work in vector graphics

import subprocess

try:
    import pandas as pd
except ImportError:
    subprocess.check_call(['pip', 'install', 'pandas'])
    import pandas as pd

try:
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call(['pip', 'install', 'matplotlib'])
    import matplotlib.pyplot as plt

try:
    from mpl_point_clicker import clicker
except ImportError:
    subprocess.check_call(['pip', 'install', 'mpl_point_clicker'])
    from mpl_point_clicker import clicker

try:
    import pickle
except ImportError:
    subprocess.check_call(['pip', 'install', 'pickle'])
    import pickle

import os
import tkinter as tk


import tkinter.simpledialog as sd
from tkinter import filedialog, messagebox


def get_input(prompt):
    root = tk.Tk()
    root.withdraw()
    user_input = sd.askstring("Input", prompt)
    return user_input


def open_input_files():
    # create a root window
    root = tk.Tk()
    root.withdraw()  # hide the root window

    # Choose all the input files
    list_of_input_files = ["input_annotation_file", "file_with_values", "map_sketch_file", "sketch_file"]
    for i in list_of_input_files:
        print("Please select:", i)
        # open a file dialog box
        file_path = filedialog.askopenfilename()

        # check if the user selected a file
        if file_path:
            var_name = i
            value = file_path
            globals()[var_name] = value
        else:
            print('No file selected')


"""
# Define the folder path and file name variables
folder_path = "C:/Users/NITru/OneDrive/Documents/PhD_work/GitHub/Various_scripts/Untitled Folder"
# Create file paths
condition = "synapse"
experiment_name = "values_to_plot"
input_annotation_file = os.path.join(folder_path, condition + ".txt")
file_with_values = os.path.join(folder_path, experiment_name + ".txt")
map_sketch_file = os.path.join(folder_path, condition + ".png")
sketch_file = os.path.join(folder_path, condition + "_bw.png")
final_figure_output_file = os.path.join(folder_path, condition + "_" + experiment_name + ".svg")
final_df_output_file = os.path.join(folder_path, condition + "_" + experiment_name + ".csv")
collection_output_file = os.path.join(folder_path, condition + ".pkl")
"""


class AnalysisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Analysis GUI")

        # Create widgets
        self.task_label = tk.Label(master, text="Please choose a menu point:")
        self.task_label.pack()

        self.find_coords_button = tk.Button(master, text="Find coordinates", command=self.find_coordinates)
        self.find_coords_button.pack()

        self.map_values_button = tk.Button(master, text="Map values", command=self.map_values)
        self.map_values_button.pack()

        self.modify_coords_button = tk.Button(master, text="Modify coordinates", command=self.select_object_window)
        self.modify_coords_button.pack()

        #self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button = tk.Button(master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

    def select_object_window(self):
        window = SelectObjectWindow(self.master)
        self.master.wait_window(window.top)
        selected_object = window.selected_object
        if selected_object is not None:
            self.modify_coordinates(selected_object)

    def find_coordinates(self):
        # messagebox.showinfo("Analysis GUI", "Finding the coordinates...")

        # Create instances from file
        instances = create_instances()

        # Set the coordinates by clicking on the sketch
        for instance in instances:
            print(instance.name)
            gene_coord = find_coords(map_sketch_file)
            instance.x = gene_coord[0]
            instance.y = gene_coord[1]

        df = create_dataframe_from_collection(instances)
        plot_coords(df)

        # Save the collection to a file using pickle
        with open(empty_coords_collection_output_file, "wb") as f:
            pickle.dump(instances, f)

        # messagebox.showinfo("Analysis GUI", "Finding the coordinates is finished.")

    def map_values(self):
        try:
            loaded_collection = load_obj_collection(collection_output_file)
        except:
            loaded_collection = load_obj_collection(empty_coords_collection_output_file)

        find_gene_IDs_in_instances(file_with_values, loaded_collection)

        with open(collection_output_file, "wb") as f:
            pickle.dump(loaded_collection, f)

        df = create_dataframe_from_collection(loaded_collection)
        df.to_csv(final_df_output_file)
        plot_coords(df)

    def modify_coordinates(self, selected_object):
        loaded_collection = load_obj_collection(collection_output_file)

        find_gene_IDs_in_instances(file_with_values, loaded_collection)
        df = create_dataframe_from_collection(loaded_collection)
        df.to_csv(final_df_output_file)
        plot_coords(df, selected_object.name)

        root = tk.Tk()
        root.title("Modify Coordinates")

        x_move_label = tk.Label(root, text="Choose how far the point should be moved in x:")
        x_move_entry = tk.Entry(root)
        x_move_label.pack(side=tk.TOP)
        x_move_entry.pack()
        x_move_entry.focus_set()

        y_move_label = tk.Label(root, text="Choose how far the point should be moved in y:")
        y_move_label.pack(side=tk.TOP)
        y_move_entry = tk.Entry(root)
        y_move_entry.pack()

        def get_input():
            x_move = int(x_move_entry.get())
            y_move = int(y_move_entry.get())

            for obj in loaded_collection:
                if obj.name == selected_object.name:
                    obj.modify_coords(x_move, y_move)

            with open(collection_output_file, "wb") as f:
                pickle.dump(loaded_collection, f)

            find_gene_IDs_in_instances(file_with_values, loaded_collection)
            df = create_dataframe_from_collection(loaded_collection)
            df.to_csv(final_df_output_file)
            plot_coords(df)

            root.destroy()

        submit_button = tk.Button(root, text="Submit", command=get_input)
        submit_button.pack()

        root.mainloop()

        # messagebox.showinfo("Analysis GUI", "Modifying the coordinates is finished.")


def load_obj_collection(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)


class SelectObjectWindow:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("Select Object")

        # self.label = tk.Label(self.top, text="Enter object name:")
        # self.label.pack()
        #
        self.entry = tk.Entry(self.top)
        # self.entry.pack()
        self.entry.focus_set()

        self.listbox = tk.Listbox(self.top)
        self.listbox.pack()

        self.button = tk.Button(self.top, text="OK", command=self.select_object)
        self.button.pack()

        self.selected_object = None

        self.listbox_update()

    def listbox_update(self):
        self.listbox.delete(0, tk.END)
        user_input = self.entry.get().lower()
        matching_objs = [obj for obj in load_obj_collection(collection_output_file) if user_input in obj.name.lower()]
        for obj in matching_objs:
            self.listbox.insert(tk.END, obj.name)

    def select_object(self):
        selection = self.listbox.curselection()
        if len(selection) == 1:
            self.selected_object = load_obj_collection(collection_output_file)[selection[0]]
            self.top.destroy()


def input_menu_number(s):
    num = 0
    inp_ok = False
    while not inp_ok:
        inp = input(s)
        # if (inp.isnumeric()) or ((inp[0] == "-") and inp[1:].isnumeric()):
        if 0 <= int(inp) <= 3:
            num = int(inp)
            inp_ok = True
        else:
            print("Please input a number from 0 to 3.")
            inp_ok = False
    return num


def input_int(s: str) -> int:
    num = 0
    inp_ok = False
    while not inp_ok:
        inp = input(s)
        if (inp.isnumeric()) or ((inp[0] == "-") and inp[1:].isnumeric()):
            num = int(inp)
            inp_ok = True
        else:
            print("Please input a number.")
            inp_ok = False
    return num


def select_object(obj_collection):
    print("Enter object name (or a few characters):")
    while True:
        user_input = input("> ")
        matching_objs = [obj for obj in obj_collection if user_input.lower() in obj.name.lower()]
        if len(matching_objs) == 0:
            print("No objects found. Please try again.")
        elif len(matching_objs) == 1:
            return matching_objs[0]
        else:
            print("Multiple matching objects found:")
            for idx, obj in enumerate(matching_objs):
                print(f"{idx + 1}: {obj.name}")
            print("Enter the number of the object you want to select (or 0 to try again): ")
            selection = None
            while selection is None:
                try:
                    selection_idx = int(input("> "))
                    if selection_idx == 0:
                        break
                    elif 1 <= selection_idx <= len(matching_objs):
                        selection = matching_objs[selection_idx - 1]
                    else:
                        print("Invalid selection. Please enter a number between 1 and", len(matching_objs))
                except ValueError:
                    print("Invalid input. Please enter a number.")
            if selection is not None:
                return selection


def create_instances():
    instances = []
    with open(input_annotation_file, "r") as f:
        for line in f:
            row = line.strip('\n').split('\t')
            instances.append(value_on_figure(row[0], row[1].split(';')))
    return instances


def label_point(x, y, val, color, ax):
    a = pd.concat({'x': x + 10, 'y': y + 10, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']), color=color)


class value_on_figure():
    __name = None
    aliases = []
    x = None
    y = None
    expression = None

    def __init__(self, name="Gene", aliases=[], x=0.0, y=0.0, expression=None):
        # better not to repeat the attribute names for parameters?
        self.name = name
        self.aliases = aliases
        self.x = x
        self.y = y
        self.expression = expression

    def __str__(self):  # A method to output object as a string.
        # print(nds) explicitly is working as print(nds.__str__()
        # it is better to always write it ourselves, otherwise the output would be standard for al objects.
        return f" {self.name}: Aliases = {self.aliases}, coordinates = {self.x}, {self.y}"

    def modify_coords(self, x_move=0, y_move=0):
        self.x = self.x + x_move
        self.y = self.y + y_move


def close_on_click(event):
    plt.close()


def find_coords(figure_file):
    image = plt.imread(figure_file)
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
            x = round(x / 10) * 10
            y = round(y / 10) * 10
            return x, y


def find_gene_IDs_in_instances(file, insts):
    with open(file) as fin:
        rows = (line.strip('\n').split('\t') for line in fin)
        input_values = {row[0]: float(row[1]) for row in rows}

    for k, v in input_values.items():
        for instance in insts:
            if k.upper() in [x.upper() for x in instance.aliases]:
                instance.expression = v


def plot_coords(data_inp, highlight_gene=None):
    nan_data = data_inp[data_inp['Expression'].isnull()]
    data = data_inp[data_inp['Expression'].notnull()]

    img = plt.imread(sketch_file)
    fig, ax = plt.subplots()
    ax.imshow(img)  # , extent=[0, 500, 0, 500]

    # Plot data points
    data.plot(kind='scatter', x='x', y='y', s=100,
              c=data['Expression'],
              edgecolors='black', linewidths=1,
              colormap="RdYlGn", colorbar=True,
              title='Genes', ax=ax)

    # Plot NaN data points
    nan_data.plot(kind='scatter', x='x', y='y', s=100,
                  fc=(0.3, 0.3, 0.3, 0.7),
                  edgecolors='black', linewidths=1, ax=ax)

    # Add labels to data points
    label_point(data.x, data.y, data.Genes, color="black", ax=ax)
    label_point(nan_data.x, nan_data.y, nan_data.Genes, color="black", ax=ax)

    # Highlight the specified gene in red
    if highlight_gene:
        gene_data = data_inp[data_inp['Genes'] == highlight_gene]
        gene_data.plot(kind='scatter', x='x', y='y', s=100,
                       fc='red', ec='black', linewidths=1, ax=ax)
        label_point(gene_data.x, gene_data.y, gene_data.Genes, color='red', ax=ax)

    plt.savefig(final_figure_output_file)
    plt.show()


def create_dataframe_from_collection(collection):
    genes = []
    aliases = []
    xs = []
    ys = []
    expressions = []
    for instance in collection:
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
        'Expression': expressions
    }

    # create a data frame
    dataframe = pd.DataFrame(dict_for_pd)
    return dataframe


if __name__ == "__main__":
    condition = get_input("Please give a name for your sketch/pathway/condition:")
    experiment_name = get_input("Please give a name for your experiment:")

    final_figure_output_file = condition + "_" + experiment_name + ".svg"
    final_df_output_file = condition + "_" + experiment_name + ".csv"
    empty_coords_collection_output_file = condition + ".pkl"
    collection_output_file = condition + "_" + experiment_name + ".pkl"

    open_input_files()

    root = tk.Tk()
    analysis_gui = AnalysisGUI(root)
    root.mainloop()
