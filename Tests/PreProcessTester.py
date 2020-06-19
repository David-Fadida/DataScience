import PreProcess

PATH = '../resources/Dataset.xlsx'

# test script -> PreProcess

# load data
try:
    data = PreProcess.read_data(PATH)
    print('\nSuccess -> data loaded from xlsx file')
except FileNotFoundError:
    data = None
    print('\nError -> broken PATH or bad file format')
    print(FileNotFoundError)

# complete numeric values
before = data.isnull().sum().sum()
data = PreProcess.complete_numeric_data(data)
after = data.isnull().sum().sum()
if after == 0:
    print('\nSuccess -> ' + str(before) + ' null values fixed')
else:
    print('\nError -> ' + str(after) + '/' + str(before) + ' are null values')

# normalize numeric values
data = PreProcess.normal_numeric_data(data)
print(data)

