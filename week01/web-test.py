'''
创建10个整数的列表、for循环打印平方、列表推导式重写、找出偶数放入新列表
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num ** 2)
squares = [num ** 2 for num in numbers]
news = [num for num in numbers if num % 2 == 0]

'''
第二天写 dict_practice.py：
    - 创建一个学生成绩字典 {'张三': 85, '李四': 92, ...}（至少5个）
    - 打印成绩最高的学生
    - 打印平均分
    - 新增一个学生，删除一个学生
    - 用 items() 遍历并格式化打印

□ 写 functions.py：
    - 写一个函数 compute_stats(scores: list) -> dict
    - 返回 {'max': ..., 'min': ..., 'avg': ..., 'count': ...}
    - 给这个函数加上 docstring
    - 调用它并打印结果
'''
# ============================================================
# dict_practice.py —— 字典练习
# 知识点：字典创建、查询、增删、遍历
# ============================================================


# ── 第一部分：创建学生成绩字典 ────────────────────────────
scores = {
    '张三': 85,
    '李四': 92,
    '王五': 78,
    '赵六': 96,
    '陈七': 88,
}
print("学生成绩字典:", scores)


# ── 第二部分：打印成绩最高的学生 ──────────────────────────
# max() 加 key 参数，告诉它"按照 scores 字典里的值来比大小"
top_student = max(scores, key=lambda name: scores[name])
print(f"\n成绩最高：{top_student}，分数：{scores[top_student]}")


# ── 第三部分：打印平均分 ──────────────────────────────────
# scores.values() 取出所有分数，sum() 求和，len() 求人数
avg = sum(scores.values()) / len(scores)
print(f"班级平均分：{avg:.1f}")   # :.1f 表示保留 1 位小数


# ── 第四部分：新增 / 删除学生 ─────────────────────────────
# 新增：直接用 scores['新名字'] = 分数
scores['周八'] = 73
print(f"\n新增周八后：{scores}")

# 删除：pop(key) 移除并返回该键的值
removed_score = scores.pop('王五')
print(f"删除王五（分数 {removed_score}）后：{scores}")


# ── 第五部分：用 items() 遍历并格式化打印 ─────────────────
# items() 同时返回 (键, 值) 对，可以直接解包成两个变量
print("\n--- 成绩单 ---")
for name, score in scores.items():
    # 根据分数给出评级
    if score >= 90:
        grade = '优秀'
    elif score >= 80:
        grade = '良好'
    else:
        grade = '及格'
    print(f"  {name:<4} {score:>3} 分  [{grade}]")
    # :<4 左对齐占4字符，:>3 右对齐占3字符，让输出整齐

