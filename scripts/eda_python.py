import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw/clients.csv")

df.info()
sns.countplot(data=df, x="churn")
plt.show()

df.to_csv("../data/processed/clients_clean.csv", index=False)
