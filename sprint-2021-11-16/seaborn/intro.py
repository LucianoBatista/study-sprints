import pandas as pd

lista1 = [1, 2, 3, 4]
lista2 = [2, 3, 4, 5]

pd_test = pd.DataFrame({"lista1": lista1, "lista2": lista2})

for index, rows in pd_test.iterrows():
    print(index)
