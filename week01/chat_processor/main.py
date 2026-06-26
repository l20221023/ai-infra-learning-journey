import os
from process import load_chat, count_messages, avg_msg_length, save_report

BASE_DIR = os.path.dirname(__file__)

# 1. 读取文件
data = load_chat(os.path.join(BASE_DIR, 'chat_log.json'))     # ✅ 完整路径

# 2. 统计
counts = count_messages(data)
avgs = avg_msg_length(data)

# 3. 保存报告
stats = {
    'count': counts,
    'avg_length': avgs
}
save_report(stats, os.path.join(BASE_DIR, 'report.json'))     # ✅ 完整路径

# 4. 打印
for user, count in counts.items():                            # ✅ .items() 解包
    print(f"{user}: 发言{count}次，平均消息长度{avgs[user]:.1f}字")

'''
.key .value 这个错误已经出现三次了——字典遍历键值对只有一种写法：for k, v in dict.items()，建议把这个写在手边。
'''