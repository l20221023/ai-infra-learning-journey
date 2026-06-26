"""
- 模拟一个"读取学生成绩"函数
    - 对可能的错误（文件不存在、格式错误、成绩超范围）
      分别用 try/except 处理，给出友好提示
"""
import json

def read_student_scores():

    try:
        with open('scores.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("错误：scores.json 文件不存在！")

    except json.JSONDecodeError:
        print("错误：文件格式出错！")

    except ValueError:
        print("数值错误")

    except Exception as e:
        print("未知错误", e)

def validate_scores(data):
    for student in data:
        try:
            if not isinstance(student, dict):
                raise ValueError("数据格式错误")
            score = student['score']
            if score < 0 or score > 100:
                raise ValueError("成绩超范围")
        except KeyError:
            print("错误，数据格式错误")
        except ValueError as e:
            print("错误", e)

def main():

    if __name__ == "__main__":#“只有直接运行这个文件时，才执行 main”
        try:
            data = read_student_scores()
            if data:
                validate_scores(data)
        except Exception as e:
            print("未知错误", e)
    
    main()
    