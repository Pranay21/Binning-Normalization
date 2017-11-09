import matplotlib.pyplot as plt
import pandas as pd
import numpy

store = []
df = pd.read_excel("ENB2012_data.xlsx", "Sheet1")  

for row in df:
        expected = (0,1)
        initial = (245,416)
        initialdiff = initial[1] - initial[0]
        new = expected[1] - expected[0] 
        currentval = (df['X3'])
        newval = (((currentval - initial[0]) * new)/initialdiff) + expected[0]
        store.append(newval)

print(df)

plt.hist(store, normed=True)
plt.title("Normalization: Histogram for Energy Efficiency")

plt.ylabel("Frequency")
plt.xlabel("Wall Area")
plt.show()