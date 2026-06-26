import json
import os
'''
messages = [
    {"user": "张三", "time": "10:00", "msg": "你好"},
    {"user": "李四", "time": "10:01", "msg": "你好你好"},
    {"user": "王五", "time": "10:02", "msg": "大家好！"},
    {"user": "张三", "time": "10:03", "msg": "今天天气真不错"},
    {"user": "李四", "time": "10:04", "msg": "是啊，适合出去走走"},
    {"user": "王五", "time": "10:05", "msg": "我已经在外面了哈哈"},
    {"user": "张三", "time": "10:07", "msg": "在哪里玩呢？"},
    {"user": "王五", "time": "10:08", "msg": "公园，风景很好"},
    {"user": "李四", "time": "10:09", "msg": "下午我也去"},
    {"user": "张三", "time": "10:11", "msg": "等我，我一起去"},
    {"user": "王五", "time": "10:12", "msg": "好的，三点见"},
    {"user": "李四", "time": "10:13", "msg": "没问题"},
    {"user": "张三", "time": "10:15", "msg": "要带什么东西吗"},
    {"user": "王五", "time": "10:16", "msg": "带点水就行"},
    {"user": "李四", "time": "10:17", "msg": "我带零食"},
    {"user": "张三", "time": "10:18", "msg": "太好了我最喜欢吃零食"},
    {"user": "王五", "time": "10:20", "msg": "哈哈那就不愁了"},
    {"user": "李四", "time": "10:21", "msg": "对了停车方便吗"},
    {"user": "王五", "time": "10:22", "msg": "东门有停车场，不贵"},
    {"user": "张三", "time": "10:23", "msg": "好，三点东门见！"},
    {"user": "李四", "time": "10:24", "msg": "👍"},
    {"user": "王五", "time": "10:25", "msg": "不见不散"}
]

with open('messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii = False, indent = 4)
print("消息已经成功写入json文件！")
'''
'''
□ 写 process.py，实现以下函数：
    - load_chat(filepath) -> list       # 读取 json
    - count_messages(data) -> dict      # 每人发言次数
    - avg_msg_length(data) -> dict      # 每人平均消息长度
    - save_report(stats, filepath)      # 保存结果到新 json

□ 写 main.py，调用上面4个函数，打印报告
'''
BASE_DIR = os.path.dirname(__file__)

def load_chat(filepath) -> list:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"错误：{filepath} 文件不存在！")
        return []

def count_messages(data) -> dict:
    count = {}
    for user in data:
        use = user['user']
        if use not in count:
            count[use] = 0
        count[use] += 1 
    return count

def avg_msg_length(data) -> dict:
    count = {}
    length = {}
    for user in data:
        use = data['user']
        if user not in count:
            count[use] = 0
            length[use] = 0
        length[use] += len(data['msg'])
        count[use] += 1
    avg = {}
    for user in count:
        avg[user] = length[user]/count[user]
    return avg


def save_report(stats, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)
    print("文件已经保存")
