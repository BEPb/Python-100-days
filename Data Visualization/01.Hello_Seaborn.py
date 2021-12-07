"""
Python 3.9 вводное занятие - о визуализации данных
Название файла '01.Hello_Seaborn.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-06
"""

import pandas as pd  # data analysis library
import matplotlib.pyplot as plt  # provides an implicit way of plotting
import seaborn as sns  # for visualization

print("Setup Complete")

# Path of the file to read
fifa_filepath = "/home/user/PycharmProjects/Python-100-days/Data Visualization/archive/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

print(fifa_data.head())

# Set the width and height of the figure
plt.figure(figsize=(16, 6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)
plt.show()
print("All Complete")

print('полный список seaborn ', sns.get_dataset_names())

