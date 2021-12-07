"""
Python 3.9 о визуализации данных
Название файла '03.BarCharts_Heatmaps.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-07
"""
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
ign_filepath = r"/home/user/PycharmProjects/Python-100-days/Data Visualization/archive/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

high_score = 7.759930
# On the Playstation Vita platform, which genre has the
# lowest average score? Please provide the name of the column, and put your answer
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'

# Bar chart showing average score for racing games by platform
# Set the width and height of the figure
plt.figure(figsize=(8, 6))
# Bar chart showing average score for racing games by platform
sns.barplot(x=ign_data['Racing'], y=ign_data.index)
# Add label for horizontal axis
plt.xlabel("")
# Add label for vertical axis
plt.title("Average Score for Racing Games, by Platform")
plt.show()



# Heatmap showing average game score by platform and genre
# Set the width and height of the figure
plt.figure(figsize=(10,10))
# Heatmap showing average game score by platform and genre
sns.heatmap(ign_data, annot=True)
# Add label for horizontal axis
plt.xlabel("Genre")
# Add label for vertical axis
plt.title("Average Game Score, by Platform and Genre")
plt.show()