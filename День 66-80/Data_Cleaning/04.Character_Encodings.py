# Character Encodings

# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)

sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

before = sample_entry.decode("big5-tw")
new_entry = before.encode()

police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='Windows-1252')


police_killings.to_csv("my_file.csv")