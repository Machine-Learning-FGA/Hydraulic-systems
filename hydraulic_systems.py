import pandas as pd
import numpy as np
import zipfile
import csv
import os

teste_list = ['TS1', 'TS2', 'TS3', 'TS4','SE', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5',
              'PS6', 'FS1', 'FS2', 'EPS1', 'CP', 'CE']

teste_list = [s + '_normalized.csv' for s in teste_list]

new_df = {}
master_df = pd.DataFrame()


# This code is for the not normalized data
# for key in teste_list:
#     with zipfile.ZipFile('data.zip') as myzip:
#         with myzip.open(key) as myfile:
#             df = pd.read_table(myfile, header=None)
#             master_df = pd.concat([master_df, df], axis=1)

for key in teste_list:
        df = pd.read_table(key, header=None)
        master_df = pd.concat([master_df, df], axis=1)

print(master_df)