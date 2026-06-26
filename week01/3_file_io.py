'''
□ 写 file_io.py：
    - 把这3个学生的信息写入 students.json
    - 重新读取 students.json，打印出来
    - 捕获 FileNotFoundError 异常
'''
import json

# 数据准备
students = [
    {"name": "Zhang San", "scores": [11, 31, 51, 71], "average": 41.0},
    {"name": "Li Si",     "scores": [31, 51, 71, 91], "average": 61.0},
    {"name": "Wang Wu",   "scores": [91, 11, 21],     "average": 41.0},
]


# ① 写入 JSON 文件
with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("写入成功")

try:
    with open('students.json', 'r', encoding='uft-8') as f:
        data = json.load(f)
    for s in data:
        print(f"姓名：{s['name']} 分数{s['scores']}  平均分{s['average']}")
except FileNotFoundError:
    print("错误：students.json 文件不存在！")


with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("写入成功！")

# ② 读取 JSON 文件（带异常捕获）
try:
    with open('students.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for s in data:
        print(f"{s['name']} 平均分：{s['average']}")

except FileNotFoundError:
    print("错误：students.json 文件不存在！")