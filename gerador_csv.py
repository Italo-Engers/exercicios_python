import pandas as pd
import json
df = pd.read_csv("./io_exercise/arquivos/how_prices.csv")
sample = df.to_dict()

with open('./io_exercise/arquivos/how_prices.json', 'w') as fp:
    json.dump(sample, fp)