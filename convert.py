import pandas as pd
df = pd.read_parquet('output.parquet', engine="pyarrow")
print(df)
