import os
import glob
import pandas as pd


folder = "C:/folder's_path/data_set"

os.chdir(folder)

# Creating a files list

extension = '.csv'

all_filenames = [i for i in glob.glob(f"*{extension}")]

# Combining files

combined_csv = pd.concat([pd.read_csv(file, delimiter=",", encoding='ANSI') for file in all_filenames])


# Export to csv

combined_csv.to_csv('combine_csv.csv', index=False, encoding='ANSI' )  
  

  