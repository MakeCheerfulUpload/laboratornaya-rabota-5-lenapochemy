import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("лаба 5 допп.csv", delimiter=";", encoding="utf-8")
fig = plt.figure(figsize=(20,10))
sns.boxplot(data=df, orient="v")
plt.xticks(rotation=45)
plt.show()