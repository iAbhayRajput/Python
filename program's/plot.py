import pandas as  pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot(kind='scatter',x="Age", y="Height")
plt.show()
