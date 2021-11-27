import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
import os
if not os.path.exists("../input/cancer_b.csv"):
    os.symlink("../input/data-for-datavis/cancer_b.csv", "../input/cancer_b.csv")
    os.symlink("../input/data-for-datavis/cancer_m.csv", "../input/cancer_m.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex5 import *
print("Setup Complete")

# Paths of the files to read
cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"


cancer_b_data = pd.read_csv(cancer_b_filepath, index_col="Id")
cancer_m_data = pd.read_csv(cancer_m_filepath, index_col="Id")

# Print the first five rows of the (benign) data
cancer_b_data.head()


# Print the first five rows of the (malignant) data
cancer_m_data.head()

# In the first five rows of the data for benign tumors, what is the
# largest value for 'Perimeter (mean)'?
max_perim = 87.46
# What is the value for 'Radius (mean)' for the tumor with Id 842517?
mean_radius = 20.57

# Histograms for benign and maligant tumors
sns.distplot(a=cancer_b_data['Area (mean)'], label="Benign", kde=False)
sns.distplot(a=cancer_m_data['Area (mean)'], label="Malignant", kde=False)
plt.legend()


# KDE plots for benign and malignant tumors
sns.kdeplot(data=cancer_b_data['Radius (worst)'], shade=True, label="Benign")
sns.kdeplot(data=cancer_m_data['Radius (worst)'], shade=True, label="Malignant")







