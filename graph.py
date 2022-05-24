import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
file_name="kavya.xlsm"
y_axis_cols=[8]
x_axis_rows=[9]
y_axis = pd.read_excel(file_name,header=3,sheet_name='Sheet1', usecols=y_axis_cols)
x_axis = pd.read_excel(file_name,header=3,sheet_name='Sheet1', usecols=x_axis_rows)
x=x_axis
y=y_axis
plt.plot(x,y)
plt.xlabel("Temperature")
plt.ylabel("altitude")
plt.title("graph of altitude vs temperature")
plt.show()