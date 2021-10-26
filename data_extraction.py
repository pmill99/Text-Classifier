
import numpy as np
import pandas as pd
import os
#Filepath to each folder containing txt files
sports_folder = r'C:\Users\peyto\OneDrive - fredonia.edu\ML\PROJECT 2\data\sports'
business_folder = r'C:\Users\peyto\OneDrive - fredonia.edu\ML\PROJECT 2\data\business'
poli_folder = r'C:\Users\peyto\OneDrive - fredonia.edu\ML\PROJECT 2\data\politics'

#Instantiating an empty dataframe with proper fields
data = pd.DataFrame(columns=['Text','Category'])

#Appending text from each sports article to dataframe
for file in os.listdir(sports_folder):
    with open(f'{sports_folder}\{file}') as f:
        txt = f.read()
    #Category is sports    
    new_entry = {'Text':txt,'Category':'Sports'}
    data = data.append(new_entry,ignore_index=True)

#Business Data
for file in os.listdir(business_folder):
    with open(f'{business_folder}\{file}') as f:
        txt = f.read()
    new_entry = {'Text':txt,'Category':'Business'}
    data = data.append(new_entry,ignore_index=True)

#Politics Data
for file in os.listdir(poli_folder):
    with open(f'{poli_folder}\{file}') as f:
        txt = f.read()
    new_entry = {'Text':txt,'Category':'Politics'}
    data = data.append(new_entry,ignore_index=True)

data.to_csv('data.csv',index=False)



