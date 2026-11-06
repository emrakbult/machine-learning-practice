import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


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

df[df["score"] >= 80]

filtered = df[
    (df["department"] == "CS") &
    (df["score"] > 80)
]

df.loc[
    df["score"] >= 80,
    ["name", "score"]
]

df.isna()
df.isna().sum()

clean_df = df.dropna()
clean_df = df.dropna(subset=["score"])

mean_age = df["age"].mean()
df["age"] = df["age"].fillna(mean_age)

median_age = df["age"].median()
df["age"] = df["age"].fillna(median_age)

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

train_df = train_df.copy()
test_df = test_df.copy()

mean_age = train_df["age"].mean()

train_df["age"] = train_df["age"].fillna(mean_age)
test_df["age"] = test_df["age"].fillna(mean_age)

a = pd.Series(
    [10, 20],
    index=["x", "y"]
)

b = pd.Series(
    [100, 200],
    index=["y", "x"]
)

print(a + b)

X = df[["age", "score"]].to_numpy()

X = np.array([
    [1, 2],
    [3, 4]
])

df = pd.DataFrame(
    X,
    columns=["feature1", "feature2"]
)