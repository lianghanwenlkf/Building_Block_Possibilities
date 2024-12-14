import json
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from tqdm import tqdm


# 计算欧几里得距离的函数
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2)**2))


with open('valid_sets_unique.json', 'r') as file:
    data_0 = json.load(file)

for key, value in tqdm(data_0.items(), total=len(data_0)):
    index = 0
    for buildings in value:
        data = []
        for building in buildings:
            data.append(np.array(building))

        # 创建一个图形
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # 定义不同颜色
        colors = ['purple', 'green', 'yellow', 'blue', 'cyan', 'red', 'pink']

        # 绘制七组数据
        for i in range(7):
            # 绘制点
            ax.scatter(data[i][:, 0], data[i][:, 1], data[i][:, 2], color=colors[i], s=100, label=f"Group {i+1}")

            # 连接距离小于1.1的点
            line_width = 4  # 线宽

            for j in range(len(data[i])):
                for k in range(j + 1, len(data[i])):
                    if euclidean_distance(data[i][j], data[i][k]) < 1.1:
                        ax.plot([data[i][j, 0], data[i][k, 0]],
                                [data[i][j, 1], data[i][k, 1]],
                                [data[i][j, 2], data[i][k, 2]],
                                color=colors[i], linewidth=line_width)

        # 设置坐标轴刻度为整数
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.zaxis.set_major_locator(MaxNLocator(integer=True))

        ax.set_xlim([1, 3])
        ax.set_ylim([1, 3])
        ax.set_zlim([1, 3])

        # 设置标签
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        folder_path = f'result/{key}'
        os.makedirs(folder_path, exist_ok=True)
        index += 1
        plt.savefig(folder_path + f'/{index}.png')
        plt.close()
