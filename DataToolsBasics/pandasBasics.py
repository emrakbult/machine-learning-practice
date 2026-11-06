import pandas as pd
import numpy as np


df = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Mehmet"],
    "age": [20, 21, 22],
    "score": [85, 90, 70]
})

print(df)

ages = pd.Series(
    [20, 21, 22],
    index=["Ali", "Ayşe", "Mehmet"]
)

print(ages)

df["age"]     # Series
df[["age"]]   # DataFrame

print(df.shape)
print(df.dtypes)
print(df.columns)
print(df.index)

df.head()       # İlk 5 satır
df.tail()       # Son 5 satır
df.info()       # Veri tipleri, eksik olmayan değer sayıları
df.describe()   # Sayısal özet istatistikler

df = pd.DataFrame({
    "name": ["Ali", "Ayşe", "Deniz", "Ece", "Mert"],
    "age": [20, np.nan, 22, 21, 24],
    "score": [85, 70, np.nan, 90, 60],
    "department": ["CS", "EE", "CS", "CS", "EE"]
}, index=["s1", "s2", "s3", "s4", "s5"])

df.loc["s2":"s4", ["name", "score"]] # s4 included

df.iloc[1:4, 0:2] # 4 and 2 excluded