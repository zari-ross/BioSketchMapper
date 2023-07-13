import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt
from mpl_point_clicker import clicker
import pickle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


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


class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Application")
        self.geometry("800x600")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,):  # Only create StartPage here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class YourControllerClass(tk.Tk):  # or whatever your controller class is
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.sketch_file = None
        self.sketch_file_for_mapping = None
        self.instances = None


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        notebook = ttk.Notebook(self)

        self.frames = {}
        for F in (OpenSketchForMapping, OpenSketch, OpenAnnotation, OpenValues, PageOne, PageTwo, PageThree):  # Include your new pages here
            page_name = F.__name__
            frame = F(parent=notebook, controller=self.controller)  # Parent is now the notebook
            self.frames[page_name] = frame

            # Add the frame to the notebook
            notebook.add(frame, text=page_name)

        notebook.pack(expand=1, fill='both')


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



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.figure = plt.Figure()
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()

        self.find_coords_button = tk.Button(self, text="Find coordinates", command=self.find_coordinates)
        self.find_coords_button.pack()

        self.ax.clear()

        # self.ax.imshow(map_sketch_file, cmap='gray')  # You'll need to get the image from somewhere
        self.canvas.draw()

    
    def find_coordinates(self):
        # sketch_file = self.controller.sketch_file
        map_sketch_file = self.controller.sketch_file_for_mapping
        instances = self.controller.instances

        # Set the coordinates by clicking on the sketch
        for instance in instances:
            print(instance.name)
            gene_coord = find_coords(map_sketch_file)
            instance.x = gene_coord[0]
            instance.y = gene_coord[1]

        df = create_dataframe_from_collection(instances)
        # plot_coords(df)

        # Save the collection to a file using pickle
        with open("coords_collection_output.pkl", "wb") as f:
            pickle.dump(instances, f)


class PageTwo(tk.Frame):
    # Corresponds to "Map values"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.map_values_button = tk.Button(self, text="Map values", command=self.map_values)
        self.map_values_button.pack()

    def map_values(self):
        # Functionality for mapping values goes here
        pass


class PageThree(tk.Frame):
    # Corresponds to "Modify coordinates"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.modify_coords_button = tk.Button(self, text="Modify coordinates", command=self.select_object_window)
        self.modify_coords_button.pack()

    def select_object_window(self):
        # Functionality for modifying coordinates goes here
        pass


class OpenSketchForMapping(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sketch_file = None  # Initialize sketch_file variable
        self.image_label = tk.Label(self)  # Label to display the image
        self.image_label.pack()
        self.open_file_button = tk.Button(self, text="Open Sketch File For Mapping", command=self.open_file)
        self.open_file_button.pack()

    def open_file(self):
        self.sketch_file = filedialog.askopenfilename()
        if self.sketch_file:
            # Load the image with Pillow
            image = Image.open(self.sketch_file)
            
            # Resize the image if it's too large for your GUI, you can modify the code below
            max_size = (800, 600)
            image.thumbnail(max_size)
            
            # Convert the image to a format Tkinter can use
            tk_image = ImageTk.PhotoImage(image)
            
            # Update the label with the new image
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image  # Keep a reference to the image to prevent it from being garbage collected

            # Move the button to the bottom
            self.open_file_button.pack_forget()
            self.open_file_button.pack(side='bottom')

            # Change the text of the button
            self.open_file_button.config(text="Change Sketch File For Mapping")

            self.controller.sketch_file_for_mapping = self.sketch_file  # Store the file name in the controller


class OpenSketch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sketch_file = None  # Initialize sketch_file variable
        self.image_label = tk.Label(self)  # Label to display the image
        self.image_label.pack()
        self.open_file_button = tk.Button(self, text="Open Sketch File", command=self.open_file)
        self.open_file_button.pack()

    def open_file(self):
        self.sketch_file = filedialog.askopenfilename()
        if self.sketch_file:
            # Load the image with Pillow
            image = Image.open(self.sketch_file)
            
            # Resize the image if it's too large for your GUI, you can modify the code below
            max_size = (800, 600)
            image.thumbnail(max_size)
            
            # Convert the image to a format Tkinter can use
            tk_image = ImageTk.PhotoImage(image)
            
            # Update the label with the new image
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image  # Keep a reference to the image to prevent it from being garbage collected

            # Move the button to the bottom
            self.open_file_button.pack_forget()
            self.open_file_button.pack(side='bottom')

            # Change the text of the button
            self.open_file_button.config(text="Change Sketch File")

            self.controller.sketch_file = self.sketch_file  # Store the file name in the controller


class OpenAnnotation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data_file = None  # Initialize data_file variable
        self.dataframe = None  # Initialize dataframe variable
        self.table_frame = tk.Frame(self)  # Frame to contain the table
        self.table_frame.pack()
        self.open_file_button = tk.Button(self, text="Open Annotation Data File", command=self.open_file)
        self.open_file_button.pack(side='top')

    def create_instances(self, input_annotation_file):
        instances = []
        with open(input_annotation_file, "r") as f:
            for line in f:
                row = line.strip('\n').split('\t')
                instances.append(value_on_figure(row[0], row[1].split(';')))
        return instances

    def open_file(self):
        self.data_file = filedialog.askopenfilename()
        if self.data_file:
            # Call the create_instances function and get the list of instances
            instances = self.create_instances(self.data_file)

            # Create a dataframe from the list of instances
            self.dataframe = pd.DataFrame([instance.__dict__ for instance in instances])

            # Clear the table frame
            for widget in self.table_frame.winfo_children():
                widget.destroy()

            # Create table
            self.table = Table(self.table_frame, dataframe=self.dataframe, showtoolbar=True, showstatusbar=True)

            # Display the table
            self.table.show()

            # Move the button to the bottom
            self.open_file_button.pack_forget()
            self.open_file_button.pack(side='bottom')

            # Change the text of the button
            self.open_file_button.config(text="Change Annotation Data File")

            self.controller.instances = instances  # Store the instances in the controller


class OpenValues(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data_file = None  # Initialize data_file variable
        self.dataframe = None  # Initialize dataframe variable
        self.table_frame = tk.Frame(self)  # Frame to contain the table
        self.table_frame.pack()
        self.open_file_button = tk.Button(self, text="Open Data File with Values", command=self.open_file)
        self.open_file_button.pack(side='top')

    def open_file(self):
        self.data_file = filedialog.askopenfilename()
        if self.data_file:
            # Load the data with pandas
            self.dataframe = pd.read_csv(self.data_file)

            # Create table
            self.table = pt = Table(self.table_frame, dataframe=self.dataframe, showtoolbar=True, showstatusbar=True)

            # Clear the table frame
            for widget in self.table_frame.winfo_children():
                widget.destroy()

            # Display the table
            pt.show()


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

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()