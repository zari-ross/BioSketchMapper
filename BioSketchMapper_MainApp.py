import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
from BioSketchMapper_GUI import *

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
        for F in (StartPage, PageOne, PageTwo, GraphPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        notebook = ttk.Notebook(self)

        self.frames = {}
        for F in (OpenSketch, OpenMapSketch, PageOne, PageTwo, GraphPage):  # Include your new pages here
            page_name = F.__name__
            frame = F(parent=notebook, controller=self.controller)  # Parent is now the notebook
            self.frames[page_name] = frame

            # Add the frame to the notebook
            notebook.add(frame, text=page_name)

        notebook.pack(expand=1, fill='both')

        
class PageOne(tk.Frame):
    # Corresponds to "Find coordinates"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.find_coords_button = tk.Button(self, text="Find coordinates", command=self.find_coordinates)
        self.find_coords_button.pack()

    
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


class GraphPage(tk.Frame):
    # Corresponds to "Modify coordinates"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.modify_coords_button = tk.Button(self, text="Modify coordinates", command=self.select_object_window)
        self.modify_coords_button.pack()

    def select_object_window(self):
        # Functionality for modifying coordinates goes here
        pass


class OpenSketch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.sketch_file = None  # Initialize sketch_file variable
        self.image_label = tk.Label(self)  # Label to display the image
        self.image_label.pack()
        open_file_button = tk.Button(self, text="Open Sketch File", command=self.open_file)
        open_file_button.pack()

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
            

class OpenMapSketch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.map_sketch_file = None  # Initialize map_sketch_file variable
        open_file_button = tk.Button(self, text="Open Map Sketch File", command=self.open_file)
        open_file_button.pack()

    def open_file(self):
        self.map_sketch_file = filedialog.askopenfilename()
        # Now you can use self.map_sketch_file in this class, and it will persist as long as this frame exists


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()