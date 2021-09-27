
import pandas as pd


df = pd.read_csv(r"data/iris.csv")

# make sure the columns are correct
assert list(df.columns) == ['sepallength', 'sepalwidth', 'petallength',
                            'petalwidth', 'class']

# print out the length of the file (rowq length)
print(f"Number of Rows = {len(df)}")

# print out some important statistics!
print(f"Mean values:\n"
      f"{df.mean(numeric_only=True)}")
