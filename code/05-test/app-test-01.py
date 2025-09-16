from palmerpenguins import load_penguins
from shiny.express import input, render, ui

penguins = load_penguins()

ui.input_select("species", "Enter a species", list(penguins.species.unique()))


@render.data_frame
def display_dat():
    idx = penguins.species.isin([input.species()])
    return penguins[idx]
