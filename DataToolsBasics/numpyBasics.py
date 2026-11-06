import numpy as np

a = np.array([10, 20, 30, 40])

print(a) # [10, 20, 30, 40]

a = np.array([1, 2, 3])

print(a * 2) # [2 4 6]

print(a + 10) # [11 12 13]

print(a ** 2) # [1 4 9]

X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(X.shape)  # (2, 3)
print(X.ndim)   # 2
print(X.size)   # 6
print(X.dtype)  # int64 (platforma bağlı)

a = np.array([1, 2, 3])
print(a.shape)  # (3,)

row = np.array([[1, 2, 3]])
print(row.shape)  # (1, 3)

X = np.zeros((10, 20, 3))

print(X.shape) # (10, 20, 3)

# reshape()
a = np.arange(12)

print(a.shape) # (12,)

b = a.reshape(3, 4)

print(b)

# auto
a = np.arange(12)

a.reshape(3, -1).shape # (3, 4)

a.reshape(-1, 2).shape # (6, 2)

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(X[1, 2])  # 60
print(X[0, 0])  # 10
print(X[-1, 1]) # 80

print(X[0:2, 1:3]) # [[20 30] [50 60]]

print(X[:, 1].shape) # (3,)

print(X[:, 1:2].shape) # (3, 1)

a = np.array([10, 20, 30, 40])

b = a[1:3]

b[0] = 99

print(a) # [10 99 30 40]

b = a[1:3].copy()

a = np.array([10, 20, 30, 40])

b = a[[1, 2]]
b[0] = 99

print(b)

print(a) # [10 20 30 40]

X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

v = np.array([10, 20, 30])

print(X + v) # [[11 22 33] [14 25 36]]

X = np.random.rand(100, 5)

mean = X.mean(axis=0)

print(mean.shape) # (5,)

std = X.std(axis=0)
X_scaled = (X - mean) / std

# NumPy'de * eleman bazlı çarpmayı, @ ise matris çarpımını ifade eder.