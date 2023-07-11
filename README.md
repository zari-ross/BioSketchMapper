# BioSketchMapper: Gene Expression Visualization Tool

This tool allows users to interactively analyze and visualize gene expression data on a chosen image, which can be a biological pathway, diagram, etc. It can read gene expression data from an input file, allows users to place gene data points on the image, and generates an output showing gene expression levels on the chosen image.
## Features

    Interactive GUI for data analysis
    Plots gene expression data on a given image (pathway)
    Visualizes specific genes or all genes in the dataset
    Highlights specific genes upon user request
    Allows for data points to be placed on the image interactively
    Outputs final visualization as an SVG file
    Exports gene expression data and coordinates as a CSV file

## Usage

    Run the Python script.
    When prompted, input a name for your sketch/pathway/condition.
    Provide a name for your experiment.
    The GUI will open. Follow the instructions in the GUI for the analysis.

## Input

This tool requires two input files:

    An image file (.jpg, .png, etc.) of the pathway or diagram.
    A tab-separated file containing gene names and expression data.

## Output

This tool generates several output files:

    A final visualization of the gene expression data on the chosen image, saved as an SVG file.
    A CSV file with the gene expression data and coordinates.
    A .pkl file storing the value_on_figure objects created during the analysis.

## Requirements

This script requires Python 3.x and the following Python packages:

    pandas
    matplotlib
    tkinter
    numpy

## Installation

First, ensure that Python 3.x is installed on your system. Then, install the required Python packages using pip:

pip install pandas matplotlib tkinter numpy

Then, download this repository to your local machine and run the script:

python BioSketchMapper_GUI.py

## Contributions

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

