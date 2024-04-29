import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 创建一个新的图形和一个可视化轴
fig, ax = plt.subplots()
ax.set_xlim(0, 100)  # 设置x轴范围
ax.set_ylim(0, 100)  # 设置y轴范围

line, = ax.plot([], [])  # 绘制空曲线

def init():
    line.set_data([], [])  # 初始化曲线数据
    return line,

def update(frame):
    mem = psutil.virtual_memory().used / 1024**3  # 获取内存使用量并转换为GB
    xdata = line.get_xdata()  # 获取曲线的x数据
    ydata = line.get_ydata()  # 获取曲线的y数据
    xdata = list(xdata) + [frame]  # 更新x数据
    ydata = list(ydata) + [mem]  # 更新y数据
    line.set_data(xdata, ydata)  # 设置曲线的新数据
    ax.set_xlim(0, frame)  # 根据frame更新x轴范围
    ax.set_ylim(0, max(ydata) + 1)  # 根据y数据更新y轴范围
    return line,

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=1000)  # 创建动画
plt.show()  # 显示动画
