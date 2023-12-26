import numpy as np
import pandas as pd 
df = pd.read_csv('heart_disease_dataset.csv')
columns_array = list(df.columns)
df_array = df.values
numerical_variables = ['age','resting_blood_pressure','cholesterol','max_heart_rate_achieved', 'num_major_vessels','st_depression']
def z_scaling(array,columns,numerical_variables):
    var_list = []
    for i in numerical_variables:
        var_list.append(columns.index(i))
    for j in var_list:
        array[:,j] = (array[:,j]-array[:,j].mean())/(array[:,j].std())

print(df_array)
z_scaling(df_array,columns_array,numerical_variables)

print(df_array)
