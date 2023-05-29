# -*- coding: utf-8 -*-
"""hw_009_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gx8YSabOAnWLSrJELV_fQ8LccklktHA8

# Задание
**Задача 40:**  Работать с файлом ***california_housing_train.csv***, который находится в папке 
***sample_data***. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (*population*)

**Задача 42:** Узнать какая максимальная ***households*** в зоне минимального значения ***population***
"""

import pandas as pd

file_path = '/content/sample_data/california_housing_train.csv'
df = pd.read_csv(file_path, sep = ',')

df.head(3)

df.head

df.describe()

df[df['population'] < 501]

len(df[df['population'] < 501].median_house_value)

df[df['population'] < 501].median_house_value.sum()

"""**Задача 40:**  Работать с файлом ***california_housing_train.csv***, который находится в папке 
***sample_data***. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (*population*)
"""

average_house_price = df[(df['population'] < 501)].median_house_value.sum() / len(df[(df['population'] < 501)].median_house_value)
print(average_house_price)

"""**Задача 42:** Узнать какая максимальная ***households*** в зоне минимального значения ***population***"""

df[['population']].min()

df[df['population'] == df['population'].min()].households.max()