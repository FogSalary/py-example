import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

# 鼠标连点功能
def start_clicking(event):
    print("wkr")
    try:
        count = int(entry_clicks.get())  # 获取用户输入的点击次数
        interval = float(entry_interval.get())  # 获取用户输入的点击间隔
        if count <= 0 or interval < 0:
            raise ValueError

        # 创建后台线程以执行点击
        def click_thread():
            for _ in range(count):
                pyautogui.click()
                time.sleep(interval)  # 等待指定间隔
            messagebox.showinfo("完成", "鼠标连点完成！")

        threading.Thread(target=click_thread, daemon=True).start()
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字（点击次数需为正整数，间隔为非负数）！")

# 创建主窗口
window = tk.Tk()
window.title("鼠标连点器")
window.geometry("300x200")

# 点击次数输入
label_clicks = tk.Label(window, text="点击次数：")
label_clicks.pack(pady=5)
entry_clicks = tk.Entry(window)
entry_clicks.pack(pady=5)

# 点击间隔输入
label_interval = tk.Label(window, text="点击间隔（秒）：")
label_interval.pack(pady=5)
entry_interval = tk.Entry(window)
entry_interval.pack(pady=5)

# 启动按钮
start_button = tk.Button(window, text="开始连点", command=start_clicking)
start_button.pack(pady=10)


window.bind("<Control-g>", start_clicking)

# 运行主循环
window.mainloop()
