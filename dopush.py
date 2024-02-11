import time
import subprocess
import os
from pushover import Client
client = Client("", api_token="")
file_to_delete = "output.txt"
while True:
# 检查文件是否存在
    if os.path.exists(file_to_delete):
    # 删除文件
        command = "mv output.txt output1.txt"
# 使用subprocess运行命令
        resulttodo = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"{file_to_delete} 已移动。")
    else:
        print(f"{file_to_delete} 不存在，无需移动。")
# 要运行的命令
    command = "python run.py"
# 使用subprocess运行命令
    resulttodo = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("已经获得了新的新闻")
    with open('output.txt', 'r') as file:
        lines = [next(file) for _ in range(1)]
    result = ''.join(lines)

    with open('output1.txt', 'r') as file:
        linestest = [next(file) for _ in range(1)]
    resulttest = ''.join(linestest)
    print("result",result)
    print("resulttest",resulttest)
    if resulttest != result:
        print("有新鲜事，准备发送")
        with open('output.txt', 'r') as file:
            lines = [next(file) for _ in range(2)]
        result1 = ''.join(lines)
        if len(result1) > 800:
    # 截取前200个字符
            result1 = result1[:800]
        client.send_message(result1, title=result)
        time.sleep(300)
    else:
        print("没有新鲜事")
        time.sleep(300)
#client.send_message(lines_3_to_6, title="新闻2")
#client.send_message(lines_7_to_9, title="新闻3")
