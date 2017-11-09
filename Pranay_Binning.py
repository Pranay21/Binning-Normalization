import matplotlib.pyplot as plt
import pandas as pd
import numpy

df = pd.read_excel("ENB2012_data.xlsx", "Sheet1")  
print(df)


plt.hist(df['X3'], bins=25)
plt.title("Binning: Histogram for Energy Efficiency")
plt.xlabel("Wall Area")
plt.ylabel("Frequency")
plt.show()