import pandas as pd
import numpy as np
import zipfile
import csv
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import timeit

start = timeit.default_timer()

teste_list = ['VS1', 'TS1', 'TS2', 'TS3', 'TS4','SE', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5',
              'PS6', 'EPS1', 'CP']

teste_list = [s + '_normalized.csv' for s in teste_list]

new_df = {}
master_df = pd.DataFrame()


# This code is for the not normalized data
# for key in teste_list:
#     with zipfile.ZipFile('data.zip') as myzip:
#         with myzip.open(key) as myfile:
#             df = pd.read_table(myfile, header=None)
#             master_df = pd.concat([master_df, df], axis=1)

# This code is for the normalized data
for key in teste_list:
        df = pd.read_table(key, header=None)
        master_df = pd.concat([master_df, df], axis=1)

target_df = pd.read_table('profile.csv', header=None)
target_df = target_df.drop([0,1,2,4], axis=1)

print(master_df)
# print(master_df.dtypes)
# print(target_df.dtypes)

x_train, x_test, y_train, y_test = train_test_split(master_df, target_df, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=4)

knn.fit(x_train, y_train.values.ravel())
print(knn.score(x_test, y_test))
pred = knn.predict(x_test)
y_train_pred = knn.predict(x_train)
cm_train = confusion_matrix(y_train, y_train_pred)
cm_test = confusion_matrix(y_test, pred)
print('confusion matrix teste\n', cm_test,'\n')
print('confusion matrix treino\n',cm_train,'\n')
print(classification_report(y_test, pred),'\n')
stop = timeit.default_timer()

print('Programa executado em ',stop - start,'segundos\n')