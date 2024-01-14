import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from pandas_datareader import data as pdr

from IPython import get_ipython

import re

PATH = "C:/Users/USER/Documents/Projects/Learn Data Analysis/Start/"
# PATH = r'C:\Users\USER\Documents\Projects\Learn Data Analysis\Start\'

# This will generate a numpy array from 0 to 9
create_range = np.arange(0, 10);
# print(create_range)

create_even_number_range = np.arange(0, 10, 2);
# print(create_even_number_range)

create_matrix = np.ones((5, 5));
# print(create_matrix)

# generate random metrices between 0,50 with 5 rows and 5 columns

create_random_matrix = np.random.randint(0, 50, (5, 5));
# print(create_random_matrix)

# Let's reshape a matrix
init1 = np.random.randint(0, 50, (5, 4));

reshape1 = init1.reshape(1, 20)
# print(reshape1)

reshape2 = init1.reshape(4,5,1)
# print(reshape2)

# Filter array
filter1 = init1[init1 > 20]
# print(filter1)

# Random seed helps to generate the same random numbers
np.random.seed(10)
Stats = np.random.randint(0,50,20)
# print(Stats)

# print("Mean: ", np.mean(Stats))
# print("Median: ", np.median(Stats))
# print("Min: ", np.min(Stats))
# print("Max: ", np.max(Stats))

# get data frame from csv file

def get_df_csv(path):
    try:
        df = pd.read_csv(path + "data.csv", index_col='dates', parse_dates=True)
        return df
    except Exception as e:
        print(e)
        return None
    
    
# get_df_csv()

# read excel file

# PATH_Two = "C:/Users/USER/Downloads/RX Docs/Role Details - Technical Team.xlsx"
# PATH_Two = "C:\Users\USER\Downloads\RX Docs\Role Details - Technical Team.xlsx"
PATH_Two = r"C:\Users\USER\Downloads\RX Docs"

def get_data_from_excel(path):
    try:
        df = pd.read_excel(path + "\\Role Details - Technical Team.xlsx")
        print(df)
        return df
    except Exception as e:
        print(e)
        return None
    
# get_data_from_excel(PATH_Two)

def read_html():
    try:
        df_list = pd.read_html("https://en.wikipedia.org/wiki/Regions_of_Ghana", match="Former Region")
        # print(df)
        df = df_list[0]
        
        # remove space
        df.columns = [x.replace(' ','_') for x in df.columns]
        
        # rename columns
        df = df.rename(columns={'Former_Region':'Old Region Name', 'Capital.1':'Capital2', 'New_Region':'New Region Name'})
        
        # remove space
        df.columns = [x.replace(' ','_') for x in df.columns]
        
        # Rename columns to make them unique
        # df.columns = [f'{col}_{i}' for i, col in enumerate(df.columns)]
        
        # remove brackets
        # df.Capital2 = df.Capital2.str.replace(r"\[.*\]",'')
        # df['Capital2'] = df['Capital2'].astype(str).str.replace(r"\[.*\]", '')
        
        # Define a function to clean and rename columns
        # def clean_and_rename(value):
        #     return str(value).replace('[', '').replace(']', '')

        # # Apply the function to the 'Capital2' column
        # df['Capital2'] = df['Capital2'].apply(clean_and_rename)
        
        def remove_brackets(value):
            return re.sub(r'\[.*\]', '', str(value))

        # Apply the function to the 'Capital2' column
        df['Capital2'] = df['Capital2'].apply(remove_brackets)
        
        # make column an index column
        # df.set_index('Old_Region_Name', inplace=True)
        
        # get data from multiple columns
        # df[['Capital2', 'New_Region_Name']]
        
        # Resetting the index to use default integer-based index
        # df.reset_index(drop=True, inplace=True)
        
        # add column
        df['index'] = np.arange(1, 17)
        
        df.set_index('index', inplace=True)
        
        # grab data from row
        df = df.loc[15]
        # df.iloc[15]
        
        # delete column 
        # df.drop('index', axis=1, inplace=True)
        
        # delete row 
        # df.drop(15, axis=0, inplace=True)
        
        
        # Identify columns with the name 'Capital' and rename them
        # for i, col in enumerate(df.columns):
        #     if 'Capital' in col:
        #         df[col] = df[col].astype(str).str.replace(r"\[.*\]", '')
        #         df.rename(columns={col: f'{col}_{i}'}, inplace=True)
        
        

        # Displaying the first few rows of the DataFrame
        # print(df.head())
        
        
        print(df)
        # print(df[0].head())
        return df
    except Exception as e:
        print(e)
        return None
    
read_html()

# colbot.cpp