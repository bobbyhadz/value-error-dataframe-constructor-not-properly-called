# ValueError: DataFrame constructor not properly called

import pandas as pd

data = {
    'Name': ['Alice', 'Bobby', 'Carl'],
    'Age': [29, 30, 31]
}

df = pd.DataFrame(data)

#     Name  Age
# 0  Alice   29
# 1  Bobby   30
# 2   Carl   31
print(df)
