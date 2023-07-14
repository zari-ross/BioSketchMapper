import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt
from mpl_point_clicker import clicker
import pickle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Add to the classes to be able zoom in on the plots:
        # self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        # self.toolbar.update()

import matplotlib.image as mpimg
from matplotlib.backend_bases import MouseButton
import customtkinter as ctk
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("green") 

class MainApplication(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title("BioSketchMapper")
        self.geometry("800x650")

        container = ctk.CTkFrame(self)
        container.pack(fill='both', expand=True)  # Updated this line

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ShowValueColor):  # Create StartPage and ShowValueColor here
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
        self.values = None


class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        notebook = ttk.Notebook(self)

        self.frames = {}

        classes = [OpenAnnotation, OpenValues, MapCoordinates, ShowValueColor, ModifyCoordinates]  # Include your new pages here
        sketches = [(OpenSketch, "Open Sketch File For Mapping", "sketch_file_for_mapping", "small_map_sketch_file_Picture1.png", "OpenSketchForMapping"),
                    (OpenSketch, "Open Sketch File", "sketch_file", "small_sketch_file_Picture1bw.png", "OpenSketch")]

        for F, text, var, default_file, tab_name in sketches:
            frame = F(parent=notebook, controller=self.controller, button_text=text, sketch_file_variable=var, default_file=default_file)
            self.frames[tab_name] = frame
            notebook.add(frame, text=tab_name)

        for F in classes:
            page_name = F.__name__
            frame = F(parent=notebook, controller=self.controller)
            self.frames[page_name] = frame
            notebook.add(frame, text=page_name)

        notebook.pack(fill='both', expand=True)


class MapCoordinates(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.figure = plt.Figure()
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=20, pady=20)

        # self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        # self.toolbar.update()

        # Create a frame to reserve space for the button
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack()

        self.find_coords_button = ctk.CTkButton(self.button_frame, text="Map coordinates", command=self.find_coordinates)
        self.find_coords_button.pack()

        # Create a label to display the instance name
        # Pack it after all other widgets
        self.instance_label = ctk.CTkLabel(self, text="")
        self.instance_label.pack(side='bottom')  # Change side to 'bottom'

        self.cid = None

    def find_coordinates(self):
        self.find_coords_button.destroy()  # Destroy the button # pack_forget()  # Hide the button
        self.find_coords_button = ctk.CTkButton(self.button_frame, text="Restart", command=self.find_coordinates)
        self.find_coords_button.pack()


        map_sketch_file = self.controller.sketch_file_for_mapping
        instances = self.controller.instances
        self.current_instance_index = 0  # Initialize current instance index

        # Set the label text to the name of the first instance
        self.instance_label.configure(text=f"Click inside the plot to map: {instances[self.current_instance_index].name}")

        # Load image
        image = mpimg.imread(map_sketch_file)

        # Clear current plot and show image
        self.ax.clear()
        self.ax.imshow(image, cmap='gray')

        # Capture click events
        def onclick(event):
            if event.button is MouseButton.LEFT and event.xdata is not None and event.ydata is not None:
                x = round(event.xdata / 10) * 10
                y = round(event.ydata / 10) * 10

                # Assign coordinates to the current instance
                if self.current_instance_index < len(instances):
                    instance = instances[self.current_instance_index]

                    instance.x = x
                    instance.y = y

                    # Plot point at the instance's coordinates
                    self.ax.plot(x, y, marker='x', color='black')

                    # Move to the next instance
                    self.current_instance_index += 1

                    # Update the label text to the name of the next instance, if there is one
                    if self.current_instance_index < len(instances):
                        next_instance = instances[self.current_instance_index]
                        self.instance_label.configure(text=f"Click inside the plot to map: {next_instance.name}")
                    else:
                        self.instance_label.configure(text="Finished finding coordinates")

                        # Disconnect the click listener
                        self.figure.canvas.mpl_disconnect(self.cid)
                        self.cid = None

                        # Reset current instance index to 0 and make the button reappear
                        self.current_instance_index = 0
                        self.find_coords_button.destroy()
                        self.find_coords_button = ctk.CTkButton(self.button_frame, text="Save Results", command=self.save_results)
                        self.find_coords_button.pack()

                    # Redraw the canvas every time a new point is plotted
                    self.canvas.draw()

        # Disconnect previous click listener if it exists
        if self.cid is not None:
            self.figure.canvas.mpl_disconnect(self.cid)

        # Connect the click listener
        self.cid = self.figure.canvas.mpl_connect('button_press_event', onclick)
        self.canvas.draw()

    def save_results(self):
        instances = self.controller.instances
        df = create_dataframe_from_collection(instances)

        # Save the collection to a file using pickle
        with open("coords_collection_output.pkl", "wb") as f:
            pickle.dump(instances, f)

        # Destroy the Save Results button
        self.find_coords_button.destroy()

        # Recreate the Find coordinates button
        self.find_coords_button = ctk.CTkButton(self.button_frame, text="Remap coordinates", command=self.find_coordinates)
        self.find_coords_button.pack()

        # Clear the label text
        self.instance_label.configure(text="")

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


def label_point(x, y, val, color, ax):
    a = pd.concat({'x': x + 15, 'y': y + 10, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']), color=color)


def plot_coords(data_inp, sketch_file, ax, fig, highlight_gene=None, colorbar_owner=None):
    nan_data = data_inp[data_inp['Expression'].isnull()]
    data = data_inp[data_inp['Expression'].notnull()]

    img = plt.imread(sketch_file)

    ax.clear()  # clear the axes
    im = ax.imshow(img)  # , extent=[0, 500, 0, 500]

    # Plot data points
    cmap = plt.get_cmap("RdYlGn")
    scatter = ax.scatter(data['x'], data['y'], s=100,
              c=data['Expression'],
              edgecolors='black', linewidths=1,
              cmap=cmap)
    
    # Add colorbar for image
    if colorbar_owner is not None:
        cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
        colorbar_owner.colorbar = fig.colorbar(scatter, cax=cax)

    # Plot NaN data points
    ax.scatter(nan_data['x'], nan_data['y'], s=100,
                  fc=(0.3, 0.3, 0.3, 0.7),
                  edgecolors='black', linewidths=1)

    # Add labels to data points
    label_point(data.x, data.y, data.Genes, color="black", ax=ax)
    label_point(nan_data.x, nan_data.y, nan_data.Genes, color="black", ax=ax)

    # Highlight the specified gene in red
    if highlight_gene:
        gene_data = data_inp[data_inp['Genes'] == highlight_gene]
        ax.scatter(gene_data['x'], gene_data['y'], s=100,
                       fc='red', ec='black', linewidths=1)
        label_point(gene_data.x, gene_data.y, gene_data.Genes, color='red', ax=ax)

    fig.canvas.draw()  # update the canvas


class ShowValueColor(ctk.CTkFrame):
    # Corresponds to "Map values"
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.figure = plt.Figure()
        self.ax = self.figure.add_subplot(111)
        self.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=20, pady=20)

        self.map_values_button = ctk.CTkButton(self, text="Map values", command=self.map_values)
        self.map_values_button.pack()

        self.save_button = ctk.CTkButton(self, text="Save Plot", command=self.save_plot)
        self.save_button.pack(pady=2)

        self.colorbar = None

        self.save_count = 1  # This will keep track of how many times you've saved the figure

    def save_plot(self):
        default_filename = f"Figure{self.save_count:03}.svg"
        filename = filedialog.asksaveasfilename(defaultextension=".svg", initialfile=default_filename)
        if filename:  # To ensure the dialog wasn't cancelled
            self.figure.savefig(filename, format='svg')
            self.save_count += 1

    def find_gene_IDs_in_instances(self, input_values, insts):
        for k, v in input_values.items():
            for instance in insts:
                if instance.aliases is not None and isinstance(instance.aliases, list):
                    if k.upper() in {x.upper() for x in instance.aliases}:
                        instance.expression = v

    def map_values(self):
        file_path = "coords_collection_output.pkl"  # os.path.join(script_dir, "coords_collection_output.pkl")
        
        if os.path.exists(file_path):
            # Load the instances from the file
            with open(file_path, "rb") as f:
                instances = pickle.load(f)

            # Map instance values
            self.find_gene_IDs_in_instances(self.controller.values, instances)

            # Convert instances to dataframe
            df = create_dataframe_from_collection(instances)

            # Clear color bar
            if self.colorbar is not None:
                self.colorbar.remove()
                self.colorbar = None
            
            # Plot instances on the sketch file
            plot_coords(df, sketch_file=self.controller.sketch_file, ax=self.ax, fig=self.figure, colorbar_owner=self)

        else:
            # Show a message telling the user to go to the MapCoordinates tab
            tk.messagebox.showinfo("Information", "No coordinates file found. Please go to the MapCoordinates tab and generate it.")


class ModifyCoordinates(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.figure = plt.Figure()
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=20, pady=20)

        # Create placeholders for buttons and instructions
        self.modify_coords_button = ctk.CTkButton(self, text="Modify coordinates", command=self.modify_coordinates)
        self.save_and_exit_button = ctk.CTkButton(self, text="Save and Exit", command=self.save_and_exit)

        # Pack the button and instruction widgets in the desired order
        self.modify_coords_button.pack()
        self.save_and_exit_button.pack_forget()  # Initially, this button is hidden
        
        self.instructions = ctk.CTkLabel(self, text="")
        self.instructions.pack(side='bottom')  # Initially, this label has no text

        self.selected_instance = None
        self.cid = None
        self.instances = None  # New instance variable to store instances

    def modify_coordinates(self):
        file_path = "coords_collection_output.pkl"

        if os.path.exists(file_path):
            self.modify_coords_button.pack_forget()  # Hide the modify button
            self.save_and_exit_button.pack()  # Show the Save and Exit button
            self.instructions.configure(text="Click on the instance you want to change.")  # Update the instructions

            # Load the instances from the file
            with open(file_path, "rb") as f:
                self.instances = pickle.load(f)  # Use the new instance variable

                df = create_dataframe_from_collection(self.instances)  # Convert instances to dataframe

                # Clear current plot and show instances
                self.ax.clear()
                plot_coords(df, sketch_file=self.controller.sketch_file, ax=self.ax, fig=self.figure)

                # Capture click events
                def onclick(event):
                    if event.button is MouseButton.LEFT and event.xdata is not None and event.ydata is not None:
                        x = round(event.xdata / 10) * 10
                        y = round(event.ydata / 10) * 10

                        if self.selected_instance is None:  # If no instance is currently selected, try to select one
                            for instance in self.instances:
                                if abs(instance.x - x) < 10 and abs(instance.y - y) < 10:  # If the click is close to an instance
                                    self.selected_instance = instance  # Select the instance
                                    # Only update the instructions when an instance has been successfully selected
                                    self.instructions.configure(text="Click on the new position.")
                                    break
                        else:  # If an instance is currently selected, move it to the new coordinates
                            self.selected_instance.x = x
                            self.selected_instance.y = y

                            # Unselect the instance
                            self.selected_instance = None

                            # Redraw the plot with updated coordinates
                            self.ax.clear()
                            df = create_dataframe_from_collection(self.instances)
                            plot_coords(df, sketch_file=self.controller.sketch_file, ax=self.ax, fig=self.figure)
                            self.canvas.draw()

                            # Update the instructions after moving the instance
                            self.instructions.configure(text="Click on the instance you want to change.")

                # Disconnect previous click listener if it exists
                if self.cid is not None:
                    self.figure.canvas.mpl_disconnect(self.cid)

                # Connect the click listener
                self.cid = self.figure.canvas.mpl_connect('button_press_event', onclick)
                self.canvas.draw()
        else:
            # Show a message telling the user to go to the MapCoordinates tab
            tk.messagebox.showinfo("Information", "No coordinates file found. Please go to the MapCoordinates tab and generate it.")
        
    def save_and_exit(self):
        file_path = "coords_collection_output.pkl"

        # Save the instances back to the file
        with open(file_path, "wb") as f:
            pickle.dump(self.instances, f)  # Use the new instance variable

        # Hide the Save and Exit button, clear the instructions, and show the Modify button
        self.save_and_exit_button.pack_forget()
        self.modify_coords_button.pack()
        self.instructions.configure(text="")  # Clear the instructions


class OpenSketch(ctk.CTkFrame):
    def __init__(self, parent, controller, button_text, sketch_file_variable, default_file):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.sketch_file_variable = sketch_file_variable  # Store the sketch_file_variable
        self.sketch_file = None  # Initialize sketch_file variable
        self.image_label = ctk.CTkLabel(self, text="")  # Label to display the image
        self.image_label.grid(row=0, column=0, sticky='nsew')  # use grid instead of pack

        self.rowconfigure(0, weight=1)  # Make the image_label row expandable
        self.columnconfigure(0, weight=1)  # Make the column expandable

        self.open_file_button = ctk.CTkButton(self, text=button_text, command=self.open_file)
        self.open_file_button.grid(row=1, column=0)  # use grid instead of pack

        # Check if default file exists and open it
        if os.path.exists(default_file):
            self.sketch_file = default_file
            self.load_image(default_file)
            setattr(self.controller, self.sketch_file_variable, self.sketch_file)  # Use the instance variable here

    def open_file(self):
        self.sketch_file = filedialog.askopenfilename()
        if self.sketch_file:
            self.load_image(self.sketch_file)  # Use load_image method

            # Move the button to the bottom
            self.open_file_button.pack_forget()
            self.open_file_button.grid(row=1, column=0)  # use grid instead of pack

            # Change the text of the button
            self.open_file_button.configure(text="Change Sketch File")
            
            # Save the new sketch_file to controller
            setattr(self.controller, self.sketch_file_variable, self.sketch_file)  # Use the instance variable here

    def load_image(self, file_path):
        # Load the image with Pillow
        self.orig_image = Image.open(file_path)  # Save original image data here

        # Get the size of the original image
        orig_size = self.orig_image.size

        # Convert the image to a format Tkinter can use
        tk_image = ctk.CTkImage(self.orig_image, size=orig_size)

        # Update the label with the new image
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image  # Keep a reference to the image to prevent it from being garbage collected


class OpenAnnotation(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.data_file = None  # Initialize data_file variable
        self.dataframe = None  # Initialize dataframe variable
        self.table_frame = ctk.CTkScrollableFrame(self, width=500, height=500)  # Frame to contain the table
        self.table_frame.pack()
        self.open_file_button = ctk.CTkButton(self, text="Open Annotation Data File", command=self.open_file)
        self.open_file_button.pack(side='bottom')

        # Check if default file exists and open it
        default_file = "input_annotation_file.txt"
        if os.path.exists(default_file):
            self.data_file = default_file
            self.open_file(self.data_file)

    def create_instances(self, input_annotation_file):
        instances = []
        with open(input_annotation_file, "r") as f:
            for line in f:
                row = line.strip('\n').split('\t')
                instances.append(value_on_figure(row[0], row[1].split(';')))
        return instances

    def open_file(self, filename=None):
        if filename is None:
            self.data_file = filedialog.askopenfilename()
        else:
            self.data_file = filename

        if self.data_file:
            # Call the create_instances function and get the list of instances
            instances = self.create_instances(self.data_file)

            # Create a dataframe from the list of instances
            self.dataframe = pd.DataFrame([instance.__dict__ for instance in instances])

            # Clear the table frame
            for widget in self.table_frame.winfo_children():
                widget.destroy()

            # Display the dataframe
            self.display_dataframe(self.dataframe, self.table_frame)

            # Change the text of the button
            self.open_file_button.configure(text="Change Annotation Data File")
            self.open_file_button.pack(side='bottom')

            self.controller.instances = instances  # Store the instances in the controller

    def display_dataframe(self, df, parent):
        for i, column in enumerate(df.columns):
            ctk.CTkLabel(parent, text=column).grid(row=0, column=i)
        for row in range(len(df)):
            for column in range(len(df.columns)):
                ctk.CTkLabel(parent, text=df.iat[row, column]).grid(row=row+1, column=column)


class OpenValues(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.data_file = None  # Initialize data_file variable
        self.dataframe = None  # Initialize dataframe variable
        self.table_frame = ctk.CTkScrollableFrame(self, width=500, height=500)  # Frame to contain the table
        self.table_frame.pack()
        self.open_file_button = ctk.CTkButton(self, text="Open Data File with Values", command=self.open_file)
        self.open_file_button.pack(side='bottom')

        # Check if default file exists and open it
        default_file = "file_with_values.txt"
        if os.path.exists(default_file):
            self.data_file = default_file
            self.open_file(self.data_file)

    def open_file(self, filename=None):
        if filename is None:
            self.data_file = filedialog.askopenfilename()
        else:
            self.data_file = filename

        if self.data_file:
            # Load the data with pandas
            self.dataframe = pd.read_csv(self.data_file, sep='\t')

            # Clear the table frame
            for widget in self.table_frame.winfo_children():
                widget.destroy()

            # Display the dataframe
            self.display_dataframe(self.dataframe, self.table_frame)

            # Change the text of the button
            self.open_file_button.configure(text="Change Data File with Values")
            self.open_file_button.pack(side='bottom')

            self.controller.values = self.create_value_dict()  # Store the values in the controller

    def create_value_dict(self):
        with open(self.data_file) as fin:
            next(fin)  # Skip the header row
            rows = (line.strip('\n').split('\t') for line in fin)
            input_values = {row[0]: float(row[1]) for row in rows}
        return input_values
    
    def display_dataframe(self, df, parent):
        for i, column in enumerate(df.columns):
            ctk.CTkLabel(parent, text=column).grid(row=0, column=i)
        for row in range(len(df)):
            for column in range(len(df.columns)):
                ctk.CTkLabel(parent, text=df.iat[row, column]).grid(row=row+1, column=column)


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
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the current script
    app = MainApplication()
    app.mainloop()