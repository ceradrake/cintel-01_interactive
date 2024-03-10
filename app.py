# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sns
from palmerpenguins import load_penguins

# Set page options for PyShiny App
ui.page_opts(title="Cera's PyShiny App with Plot", fillable=True)

# Create a sidebar with an input slider for the number of bins
with ui.sidebar():
    # String ID = selected_number_of_bins
    # String Label = Number of Bins
    # Integer representing the minimum # of bins = 0
    # Integer representing the maximum # of bins = 150
    # Integer representing the intial value of the slider = 75
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 150, 75)


# Define a plot function for rendering a histogram
@render.plot(alt="A histogram")
def histogram():
    # Set a random seed for reproducibility
    np.random.seed(500)

    # Generate random data for the histogram
    x = 100 + 15 * np.random.randn(150)

    # Plot the histogram using the specified number of bins
    plt.hist(x, input.selected_number_of_bins(), density=True, color='green')

@render.plot(alt="A line plot")
def lineplot(): 
    x = [1, 5, 25, 75, 150]
    y = [1, 5, 25, 75, 150]
    plt.plot(x,y)
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("My Simple Line Plot")
    num_points = 50 
    x_points = np.random.uniform(0, 100, num_points)
    y_points = np.random.uniform(-1, 150, num_points)
    plt.scatter(x_points, y_points, color="red", label="random points")
    
