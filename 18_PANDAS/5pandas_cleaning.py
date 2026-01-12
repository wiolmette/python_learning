import pandas as pd

df = pd.read_csv('data2.csv')

print(df)

# ---

# pip install lxml html5lib beautifulsoup4 - najpierw instalacja lxml, czyli parsera HTML
# parser HTML to program (biblioteka), który czyta kod HTML i zamienia go w strukturę, 
# z którą Python może sensownie pracować

url = "https://www.w3schools.com/python/pandas/pandas_cleaning.asp"
tables = pd.read_html(url)
df2 = tables[0]
print(df2)
