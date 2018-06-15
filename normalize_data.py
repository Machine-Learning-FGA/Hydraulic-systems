import pandas as pd
import numpy as np
import zipfile
import csv

list_100 = ['PS1', 'PS2', 'PS3', 'PS4', 'PS5',
            'PS6', 'EPS1']
list_10 = ['FS1', 'FS2']

list_100 = [s + '.txt' for s in list_100]
list_10 = [s + '.txt' for s in list_10]


master_df = pd.DataFrame()
for key in list_100:
    new_file = open(key.replace('.txt', '') + '_normalized.csv', "w")
    writer = csv.writer(new_file, delimiter='\t')
    with zipfile.ZipFile('data.zip') as myzip:
        with myzip.open(key) as myfile:
            df = pd.read_table(myfile, header=None)

            for i in range(2205):
                row = df.loc[i, :].values.tolist()
                definite_row = []
                sum = 0

                for x, y in enumerate(row):
                    if x == 0:
                        sum += y
                    elif x == len(row)-1:
                        sum += y
                        definite_row.append(sum/100)
                    elif x % 100 != 0:
                        sum += y
                    else:
                        definite_row.append(sum/100)
                        sum = 0
                        sum += y

                writer.writerow(definite_row)
                del definite_row[:]

for key in list_10:
    new_file = open(key.replace('.txt', '') + '_normalized.csv', "w")
    writer = csv.writer(new_file, delimiter='\t')
    with zipfile.ZipFile('data.zip') as myzip:
        with myzip.open(key) as myfile:
            df = pd.read_table(myfile, header=None)

            for i in range(2205):
                row = df.loc[i, :].values.tolist()
                definite_row = []
                sum = 0

                for x, y in enumerate(row):
                    if x == 0:
                        sum += y
                    elif x == len(row)-1:
                        sum += y
                        definite_row.append(sum/10)
                    elif x % 10 != 0:
                        sum += y
                    else:
                        definite_row.append(sum/10)
                        sum = 0
                        sum += y

                writer.writerow(definite_row)
                del definite_row[:]
