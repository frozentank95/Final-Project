import pandas as pd 

# to read csv file named "samplee" 
df = pd.read_csv('df.csv') 
df = df.head(10)

# to save as html file 
# named as "Table" 
df.to_html("dataset.html") 