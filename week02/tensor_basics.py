"""
tensor_basics.py —— PyTorch Tensor 基础练习
运行方式：python tensor_basics.py
"""

import numpy as np
import torch as torch

print("PyTorch version:", torch.__version__)

print("\n" + "=" * 50)
print("1. 创建各种 Tensor")
print("=" * 50)

zeros = torch.zeros(3, 4)
ones  = torch.ones(2, 3)
rand  = torch.rand(3, 3)      # 均匀分布 [0, 1)
randn = torch.randn(3, 3)     # 标准正态分布
arr   = torch.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

print("zeros (3×4):\n", zeros)
print("ones  (2×3):\n", ones)
print("rand  (3×3):\n", rand.round(decimals=3))
print("arange(0,10,2):", arr)

print("\n" + "=" * 50)
print("2. reshape / transpose / squeeze / unsqueeze")
print("=" * 50)

a = torch.arange(12)        # shape (12,)
b = a.reshape(3, 4)         # shape (3, 4)
c = b.T                     # transpose → (4, 3)  [也可用 b.permute(1,0)]

print("a.shape:\n", a.shape)
print("arange(12):", a)
print("reshape(3,4):\n", b)
print("transpose:\n", c)

# squeeze
d = torch.ones(1, 3, 1, 4)
e = d.squeeze()
print(f"\nsqueeze: {tuple(d.shape)} → {tuple(e.shape)}")

# unsqueeze（PyTorch 原生支持，比 expand_dims 更常用）
f = torch.ones(3, 4)
g = f.unsqueeze(0)   # (1, 3, 4)
h = f.unsqueeze(2)   # (3, 4, 1)
print(f"unsqueeze(0): {tuple(f.shape)} → {tuple(g.shape)}")
print(f"unsqueeze(2): {tuple(f.shape)} → {tuple(h.shape)}")

print("\n" + "=" * 50)
print("3. 矩阵乘法：torch.mm / torch.matmul / @")
print("=" * 50)

A = torch.tensor([[1, 2],
                  [3, 4]], dtype=torch.float32)
B = torch.tensor([[5, 6],
                  [7, 8]], dtype=torch.float32)

print("A:\n", A)
print("B:\n", B)
print("torch.mm(A,B):\n",     torch.mm(A, B))
print("torch.matmul(A,B):\n", torch.matmul(A, B))  # 支持 batch
print("A @ B:\n",              A @ B)               # 语法糖
print("元素逐一相乘 A*B:\n",   A * B)

print("\n" + "=" * 50)
print("4. 广播：(3,1) + (1,4)")
print("=" * 50)

col = torch.tensor([[1], [2], [3]], dtype=torch.float32)  # (3,1)
row = torch.tensor([[10, 20, 30, 40]], dtype=torch.float32)  # (1,4)

result = col + row
print("col:\n", col)
print("row:", row)
print(f"结果 shape: {tuple(result.shape)}")
print(result)

print("\n" + "=" * 50)
print("5. NumPy ↔ PyTorch 互转")
print("=" * 50)

# --- NumPy → Tensor ---
np_arr = np.array([[1.0, 2.0], [3.0, 4.0]])
t_from_np = torch.from_numpy(np_arr)   # 共享内存（CPU）
t_copy    = torch.tensor(np_arr)       # 拷贝

print("np_arr:\n", np_arr)
print("from_numpy (共享内存):\n", t_from_np)

# 验证共享内存：修改 np_arr，from_numpy 的 tensor 也会变
np_arr[0, 0] = 99.0
print("修改 np_arr[0,0]=99 后:")
print("  np_arr:", np_arr[0])
print("  from_numpy:", t_from_np[0])  # 同步变为 99
print("  tensor(拷贝):", t_copy[0])   # 不变，仍为 1

# --- Tensor → NumPy ---
t = torch.ones(2, 3)
np_from_t = t.numpy()         # 共享内存（仅 CPU tensor）
np_copy   = t.numpy().copy()  # 显式拷贝

print("\ntensor:\n", t)
print("tensor.numpy():\n", np_from_t)

# 验证：修改 tensor 后 numpy 同步
t.fill_(7.0)
print("t.fill_(7) 后 np_from_t:\n", np_from_t)   # 同步 → 7
print("np_copy（不变）:\n", np_copy)              # 不变 → 1

print("\n全部通过 ✓")
print("""
关键结论：
  torch.from_numpy()  / tensor.numpy()  → 共享内存，修改互相影响
  torch.tensor(arr)   / arr.copy()      → 独立拷贝，安全但多占内存
""")