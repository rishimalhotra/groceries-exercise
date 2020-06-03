import os
import pandas
#csv_filepath = "data/products.csv"
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
df = pandas.read_csv(csv_filepath)
print(type(df)) #> <class 'pandas.core.frame.DataFrame'>
print(df.head()) #> prints first few rows
products = df.to_dict("records")
# todo: assemble a list of dictionaries
# APPROACH A
#products = []
#
#for row in _____________: # how to loop through each row in a dataframe
#    products.append({}) # how to convert each row to a dictionary
# APPROACH B
