"""
- 手动实现一个 Counter 类，支持 __iter__ 和 __next__
    - 用 for 循环遍历它（从1数到10）
    - 写一个生成器函数 fibonacci()，yield 前10个斐波那契数
"""

class Counter:
    def __init__(self):
        self.current = 1
        self.max_num = 10

    def __iter__(self,):
        return self
    
    def __next__(self):
        
        if self.current > self.max_num:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

counter = Counter()
for x in counter:
    print(x)
