import pandas as pd
import numpy as np


#def calculate_demographic_data(print_data=True):
# Read data from file
df = pd.read_csv('adult.data.csv')

#df.groupby(by='race').size()

 # What is the average age of men?
average_age_men = None

print('printable \n')
groupof_men = df.loc[(df['sex'] == 'Male')]
print(groupof_men['age'].mean().mean())

# people with bachelor degree
bachelor = df.loc[(df['education'] == 'Bachelors')]
print(bachelor)


