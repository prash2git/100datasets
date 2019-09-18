import pandas as pd
import seaborn as sns

data = 'data/galton-families.csv'

df = pd.read_csv(data)

print(df)

son = df['gender'] == 'male'

print(son)

son

sys.exit(0)