import pandas as pd
import numpy as np
cars_df=pd.read_csv('cars93.csv')
#checks if any NaN or missing value present
print(cars_df.isna().any())
#total missing value in all columns if any
print(cars_df.isna().sum())
#finding the rows where NaN exist
print(cars_df[cars_df['horsepower'].isnull()])
#it organize data in groupwise manner
gkk=cars_df.groupby(['origin','model_year'])
print(gkk.first())
# fillna() method can be used to fill NA or NaN values in the DataFrame.
#There are various methods for imputing the numerical and categorical columns. Numerical columns can be imputed with mean, median etc.
#Categorical columns can be imputed with mode and so on.
cars_df['horsepower']=cars_df.groupby(['cylinders','model_year'])['horsepower'].apply(lambda x: x.fillna(x.mean()))
print(cars_df.isna().any())
