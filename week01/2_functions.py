'''
写 functions.py：
    - 写一个函数 compute_stats(scores: scores) -> dict
    - 返回 {'max': ..., 'min': ..., 'avg': ..., 'count': ...}
    - 给这个函数加上 docstring 和 type hint
    - 调用它并打印结果
'''

def compute_stats(scores: list) -> dict:
    """
    计算一组数字的统计信息。

    Args:
        scores (list): 包含数字的列表

    Returns:
        dict: 包含以下键的字典：
            - 'max'   : 最大值
            - 'min'   : 最小值
            - 'avg'   : 平均值
            - 'count' : 元素个数
    """
    return {
        'max':   max(scores),
        'min':   min(scores),
        'avg':   sum(scores) / len(scores),  # ✅ 键名无冒号
        'count': len(scores)                 # ✅ 键名无冒号
    }

result =  compute_stats ([85, 92, 78, 96, 88])
print(result)
