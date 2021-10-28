#pip install pandas
#pip install lxml

### IMPORT LIBRARIES ###

import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]

print(df)
