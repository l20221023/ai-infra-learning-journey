'''
□ 写 dict_practice.py：
    - 创建一个学生成绩字典 {'张三': 85, '李四': 92, ...}（至少5个）
    - 打印成绩最高的学生
    - 打印平均分
    - 新增一个学生，删除一个学生
    - 用 items() 遍历并格式化打印
'''
scores = {
    '张三': 85,
    '李四': 92,
    '王五': 78,
    '赵六': 96,
    '陈七': 88,
}
print("学生成绩字典:", scores)
print("学生成绩最高分：",max(scores.values()))
print("学生成绩平均分：", sum(scores.values())/len(scores))
scores['勾八'] = 90
scores.pop('陈七')
for key, value in scores.items:
    print(key + "：" + str(value))