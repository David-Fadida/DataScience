import pandas as panda
from sklearn import preprocessing as pre_process


# read data from xlsx (Excel) file
def read_data(path):
    data = panda.read_excel(path)
    return data


# complete numeric data
def complete_numeric_data(data):
    fix_null(data, 'Log GDP per capita')
    fix_null(data, 'Social support')
    fix_null(data, 'Healthy life expectancy at birth')
    fix_null(data, 'Freedom to make life choices')
    fix_null(data, 'Generosity')
    fix_null(data, 'Perceptions of corruption')
    fix_null(data, 'Positive affect')
    fix_null(data, 'Negative affect')
    fix_null(data, 'Confidence in national government')
    fix_null(data, 'Democratic Quality')
    fix_null(data, 'Delivery Quality')
    return data


# replace null values with column average value
def fix_null(data, column):
    data[column].fillna((data[column]).mean, inplace=True)


# Standardization numeric data
def normal_numeric_data(data):
    return pre_process.normalize(data)
