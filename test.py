import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from pandas_datareader import data as pdr

from IPython import get_ipython

weights = np.array([0.3, 0.2, 0.9])



# weights = [0.3, 0.2, 0.9]
# regions = {
#     'kanto': [73, 67, 43],
#     'johto': [91, 88, 64],
#     'hoenn': [87, 134, 58],
#     'sinnoh': [102, 43, 37],
#     'unova': [69, 96, 70]
# }
# kanto = [73, 67, 43]
# johto = [91, 88, 64]
# hoenn = [87, 134, 58]
# sinnoh = [102, 43, 37]
# unova = [69, 96, 70]

# np_shape = np.array([
#     [[11, 12, 13], 
#      [13, 14, 15]], 
#     [[15, 16, 17], 
#      [17, 18, 19]]])

# # numpy data types should always be the same
# # if a single data type is a float, all values would be converted to float
# np_shape.shape
# print(np_shape.shape)
# print(np_shape.dtype)


# def test(region_name, weights, regions_dict):
#     if region_name in regions_dict:
#         result = 0
#         region_values = regions_dict[region_name]
#         for x, w in zip(region_values, weights):
#             result += x * w
        
#         print(result)
#         return result
#     else:
#         print("Region not found")
#         return None


# test('sinnoh', weights, regions)