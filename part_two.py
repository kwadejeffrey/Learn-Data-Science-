import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from pandas_datareader import data as pdr

from IPython import get_ipython

import re

def manipulate_html_data():
    data_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)", match="Country/Territory")
    
    data_list = data_list[0].head(50)
    # data_list = data_list[0]
    
    # Let's drop top level columns
    data_list.columns = data_list.columns.droplevel(0)
    
    # removing duplicate columns
    # : means starting from the beginning
    # ~ means if the column hasn't been used prior
    # data_list.columns.duplicated(): This part generates a boolean mask indicating whether each column in data_list is a duplicate. It returns a Series of True/False values, where True indicates that the column is a duplicate.
    # ~data_list.columns.duplicated(): The tilde (~) is a bitwise NOT operator in Python. It inverts the True and False values in the boolean mask, so now True indicates that the column is not a duplicate, and False indicates that it is a duplicate.
    # data_list.loc[:, ~data_list.columns.duplicated()]: This uses boolean indexing to select columns from the DataFrame. The loc accessor is used to select rows and columns by label. The colon (:) before the comma indicates that we want to select all rows. After the comma, ~data_list.columns.duplicated() is used as a boolean mask to select only the columns that are not duplicated.
    data_list = data_list.loc[:,~data_list.columns.duplicated()]
    
    # remove rows with NaN
    # data_list = data_list.dropna()
    # data_list = data_list[data_list['Estimate'].notna()]
    
    # remove brackets
    # Define a function to clean and rename columns
    def clean_and_rename(value):
        # return str(value).replace('[', '').replace(']', '')
        return re.sub(r'\[.*\]', '', str(value))

    # Apply the function to the 'Capital2' column
    data_list['Year'] = data_list['Year'].apply(clean_and_rename)
    data_list['Country/Territory'] = data_list['Country/Territory'].apply(clean_and_rename)
    
    # rename columns
    data_list = data_list.rename(columns={'Country/Territory':'Country', 'UN region':'Region', 'Estimate':'GDP'})
    
    # find the mean of each column
    # data_list = data_list.groupby('Region').mean()
    # find the median of each column
    # data_list = data_list.groupby('Region').median()
    
    # Convert 'GDP' column to numeric (handling '—' as NaN)
    data_list['GDP'] = pd.to_numeric(data_list['GDP'], errors='coerce')

    # Group by 'Region' and calculate mean and median for 'GDP'
    data_list = data_list.groupby('Region')['GDP'].agg(['mean', 'median'])
    
    # # Ensure that 'Year' and 'GDP' columns are numeric
    # data_list['Year'] = pd.to_numeric(data_list['Year'], errors='coerce')
    # data_list['GDP'] = pd.to_numeric(data_list['GDP'], errors='coerce')

    # # Filter out non-numeric values from the 'Country' column
    # numeric_countries = data_list['Country'].apply(pd.to_numeric, errors='coerce').notna()

    # # Group by the filtered numeric 'Country' and calculate the median
    # data_list = data_list[numeric_countries].groupby('Country').median().reset_index()
    
    # print(data[2].head(10))
    # print(data_list[0].head(30))
    print(data_list)
    
manipulate_html_data()