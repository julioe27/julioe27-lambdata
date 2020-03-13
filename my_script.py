import pandas
import numpy

from my_mod import df_nulls

print("HAPPY TUESDAY NIGHT")

df = pandas.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
print(df.head())

x = 5
print(df_nulls(df))

