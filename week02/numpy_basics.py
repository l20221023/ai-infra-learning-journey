"""
numpy_basics.py —— NumPy 基础练习
    - 创建各种数组（zeros、ones、random、arange）
    - reshape、transpose、squeeze/unsqueeze
    - 矩阵乘法（np.dot 和 @）
    - broadcast：(3,1) + (1,4) 的结果是什么？手算后验证
运行方式：python numpy_basics.py
"""
import torch
import numpy as np

print("=" * 50)
print("1. 创建各种数组")
print("=" * 50)

zeros = np.zeros((3, 4))
ones  = np.ones((2, 3))
rand  = np.random.random((3, 3))     # 均匀分布 [0, 1)
randn = np.random.randn(3, 3)        # 标准正态分布
arr   = np.arange(0, 10, 2)         # [0, 2, 4, 6, 8]
twos  = np.full((3,4), 2)
eye   = np.eye(4)
linspace = np.linspace(0, 2, 5)
intmatrix = np.arange(1,10).reshape(3,3)
intmatrix2 = np.random.randint(1, 20,(3,4))

print("zeros (3×4):\n", zeros)
print("ones  (2×3):\n", ones)
print("random(3×3):\n", rand.round(3))
print("arange(0,10,2):\n", arr)
print("twos:\n", twos)
print("eye:\n", eye)
print("linspace:\n", linspace)
print("intmatrix (3*3):\n", intmatrix)
print("intmatrix2 (3*4):\n", intmatrix2)


print("\n" + "=" * 50)
print("2. reshape / transpose / squeeze / unsqueeze / flatten / concatenate / stack / hstack / vstack")
print("=" * 50)

a = np.arange(12)           # shape (12,)
b = a.reshape(3, 4)         # shape (3, 4)
c = b.T                     # transpose → shape (4, 3)
d = b.flatten()             # flatten → shape(12,)
e = np.concatenate((a, b.flatten()), axis = 0)
f = np.stack((a, d), axis = 0)
g = np.hstack((b, b))
h = np.vstack((b, b))
i = np.expand_dims(b, axis=0)

print("arange(12):", a)
print("reshape(3,4):\n", b)
print("transpose:\n", c)
print("flatten:\n", d)
print("concatenate(a, b.flatten()):\n", e)
print("stack(a, b, axis = 0):\n", f)
print("hstack(a, b, c):\n", g)
print("vstack(a, b, c):\n", h)
print("unsqueeze(b):\n", i)


# squeeze：去掉所有长度为 1 的维度
d = np.ones((1, 3, 1, 4))  # shape (1, 3, 1, 4)
print("ones((1, 3, 1, 4)):\n", d)
e = d.squeeze()             # shape (3, 4)
print(f"\nsqueeze: {d.shape} → {e.shape}")
print("squeeze:\n", e)

# expand_dims（相当于 unsqueeze）：在指定轴插入维度
f = np.ones((3, 4))         # shape (3, 4)
g = np.expand_dims(f, axis=0)  # shape (1, 3, 4)
h = np.expand_dims(f, axis=2)  # shape (3, 4, 1)
print("f(3,4):\n", f)
print(f"g的形状：{g}")
print(f"h的形状：{h}")
print(f"expand_dims axis=0: {f.shape} → {g.shape}")
print(f"expand_dims axis=2: {f.shape} → {h.shape}")

print("\n" + "=" * 50)
print("3. 矩阵乘法：np.dot 和 @")
print("=" * 50)

A = np.array([[1, 2],
              [3, 4]], dtype=np.int64)   # (2, 2)
B = np.array([[5, 6],
              [7, 8]], dtype=np.int64)   # (2, 2)

C = A + B


print("A:\n", A)
print("B:\n", B)
print("C:\n", C)
print("np.dot(A, B):\n", np.dot(A, B))
print("A @ B:\n",        A @ B)         # 完全等价
print("元素逐一相乘 A*B:\n", A * B)     # 注意区别！

print("\n" + "=" * 50)
print("4. 广播 Broadcasting：(3,1) + (1,4)")
print("=" * 50)

# 手算：
#   (3,1) 沿 axis=1 扩展 → (3,4)
#   (1,4) 沿 axis=0 扩展 → (3,4)
# 结果形状 (3,4)，每行 = 列向量的该行值 + 行向量

col = np.array([[1],   # shape (3, 1)
                [2],
                [3]])

row = np.array([[10, 20, 30, 40]])  # shape (1, 4)

result = col + row
print("col (3,1):\n", col)
print("row (1,4):", row)
print("col + row → shape", result.shape)
print(result)
print("""
手算验证：
  行0: 1 + [10,20,30,40] = [11,21,31,41]
  行1: 2 + [10,20,30,40] = [12,22,32,42]
  行2: 3 + [10,20,30,40] = [13,23,33,43]
""")

print("全部通过 ✓")