
import pandas as pd

# jak skrocic plik json do 30 wierszy?

df = pd.read_json('data.json')

new_df = df.dropna()        # usuwanie wierszy zawierajacych puste komorki

print(new_df.to_string())