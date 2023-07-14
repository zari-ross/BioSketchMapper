# BioSketchMapper: Gene Expression Visualization Tool

This tool allows users to interactively analyze and visualize gene expression data on a chosen image, which can be a biological pathway, diagram, etc. It can read gene expression data from an input file, allows users to place gene data points on the image, and generates an output showing gene expression levels on the chosen image.
## Features
    *Interactive GUI*: The application provides an intuitive graphical interface, simplifying the task of gene mapping and data analysis.
    *Custom sketches*: Users can upload their own sketches or diagrams to which gene data points can be mapped.
    *Gene expression mapping*: The tool can plot specific genes or all genes from the dataset onto the provided sketch.
    *Flexible data points placement*: Allows for data points to be interactively placed on the image for customized visualization.
    *Output formats*: The final visualization can be saved as an SVG file, and gene expression data, along with coordinates, can be exported as a CSV file.

## Usage

    Run the Python script.
    The GUI will open. Follow the instructions in the GUI for the analysis.

## Input

The tool requires four input files:

    Two image files (.jpg, .png, etc.) of the pathway or diagram.
    Two tab-separated files containing gene names and expression data.

## Output

This tool generates several output files:

    A final visualization of the gene expression data on the chosen image, saved as an SVG file.
    A .pkl file storing the value_on_figure objects created during the analysis.


## Installation

First, ensure that Python 3.7 is installed on your system. 

Clone this repository using git:
git clone https://github.com/username/BioSketchMapper.git

Then, install the required Python packages using pip:
pip install -r requirements.txt

python BioSketchMapper_GUI.py

## Contributions

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

