# вводное занятие - не очем (думать вообще не нужно)
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

# Set up code checking
import os
if not os.path.exists("../input/fifa.csv"):
    os.symlink("../input/data-for-datavis/fifa.csv", "../input/fifa.csv")
# from learntools.core import binder
# binder.bind(globals())
# from learntools.data_viz_to_coder.ex1 import *


print("Setup Complete")

# Path of the file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(16, 6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)