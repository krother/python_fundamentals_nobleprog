
import pandas as pd

data = pd.read_csv('babynames.csv', names=['name', 'gender', 'number'])  # returns a DataFrame  ~table

# top 10 names
top10 = data.iloc[:10, :3]   # select first 10 rows and first 3 columns
print(top10)

# count girls / boys names
print(data.groupby('gender')['name'].count())   # number of non-empty rows

# count number of girls / boys
print(data.groupby('gender')['number'].sum())

# count first characters
print(data['name'].str[0].value_counts())

# Hint: for plotting, check out the Jupyter notebook
# or
from matplotlib import pyplot as plt

data['name'].str[0].value_counts().head(10).plot.bar()
plt.savefig('frequent_first_characters.png')
