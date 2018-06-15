import pandas as pd
import numpy as np
import zipfile
import csv

teste_list = ['VS1', 'TS1', 'TS2', 'TS3', 'TS4','SE', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 
              'PS6', 'FS1', 'FS2', 'EPS1', 'CP', 'CE', 'profile']

teste_list = [s + '.txt' for s in teste_list]

new_df = {}
new_file = open('new_dataframe.csv', 'w')
master_df = pd.DataFrame()

for key in teste_list:
    with zipfile.ZipFile('data.zip') as myzip:
        with myzip.open(key) as myfile:
            df = pd.read_table(myfile, header=None) 
            master_df = pd.concat([master_df, df], axis=1)

# with open('new_dataframe.csv', 'w') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, new_df.keys())
#     w.writeheader()
#     w.writerow(new_df)

new_file.close()
