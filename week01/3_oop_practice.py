'''
□ 写 oop_practice.py:
    - 定义一个 Student 类
      属性:name, scores（list）
      方法:add_score(score)、average()、__repr__()
      
    - 创建3个 Student 实例
    - 调用 add_score 添加多个成绩
    - 打印每个学生的平均分
'''
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self,score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        else: 
            return sum(self.scores) / len(self.scores)

    def __repr__(self): 
        return f"Student(name={self.name!r}, scores={self.scores}, average={self.average():.2f})"
'''
# 类方法的第一参数必须是self，否则肯定出错。
repr是 Python 的魔法方法，定义"这个对象打印出来长什么样"。
!r 表示用 repr() 格式输出，字符串会自动加引号 → '张三'
{self.average():.2f}调用方法并保留2位小数 → 85.00
'''
Z = Student('Zhang San')
L = Student('Li Si')
W = Student('Wang Wu')


Z.add_score(11)
Z.add_score(31)
Z.add_score(51)
Z.add_score(71)
W.add_score(91)
W.add_score(11)
L.add_score(31)
L.add_score(51)
L.add_score(71)
L.add_score(91)
W.add_score(21)

print(f"W的平均分是：{W.average():.2f}")
print(f"L的平均分是：{L.average():.2f}")
print(f"Z的平均分是：{Z.average():.2f}")