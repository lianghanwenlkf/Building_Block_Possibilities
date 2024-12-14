import json
import os

from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import time


def load_json_files(filenames):
    all_combinations = []
    for filename in filenames:
        with open(filename, 'r') as file:
            data = json.load(file)
            all_combinations.append(data)
    return all_combinations


# 计算欧几里得距离的函数
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2)**2))


def paint(points, save_path, index):
    # 创建一个图形
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = ['purple', 'green', 'yellow', 'blue', 'cyan', 'red', 'pink']

    # 绘制点
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='r', s=100)

    # 连接距离小于1.1的点
    line_width = 5  # 线宽

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if euclidean_distance(points[i], points[j]) < 1.1:
                ax.plot([points[i, 0], points[j, 0]],
                        [points[i, 1], points[j, 1]],
                        [points[i, 2], points[j, 2]],
                        color=colors[index], linewidth=line_width)

    # 设置坐标轴刻度为整数
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.zaxis.set_major_locator(MaxNLocator(integer=True))


    # 设置坐标轴比例一致
    # 获取每个坐标轴的范围
    x_range = np.ptp(points[:, 0])
    y_range = np.ptp(points[:, 1])
    z_range = np.ptp(points[:, 2])

    # 找到最大范围，以便统一比例
    max_range = max(x_range, y_range, z_range)

    # 设置三个坐标轴的尺度一致
    ax.set_xlim([points[:, 0].min(), points[:, 0].min() + max_range])
    ax.set_ylim([points[:, 1].min(), points[:, 1].min() + max_range])
    ax.set_zlim([points[:, 2].min(), points[:, 2].min() + max_range])

    ax.set_xlim([1, 3])
    ax.set_ylim([1, 3])
    ax.set_zlim([1, 3])

    # 设置标签
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.savefig(save_path)
    plt.close()


def main():
    filenames = [
        "building_1.json",
        "building_2.json",
        "building_3.json",
        "building_4.json",
        "building_5.json",
        "building_6.json",
        "building_7.json"
    ]

    # 读取所有文件
    all_combinations = load_json_files(filenames)
    for i, building in enumerate(all_combinations):
        print(f"积木{i+1}")
        time.sleep(1)
        for j, points in tqdm(enumerate(building), total=len(building)):
            points = np.array(points)
            folder_path = f'{i+1}'
            os.makedirs(folder_path, exist_ok=True)
            save_path = folder_path + f'/{j+1}.png'
            paint(points, save_path, i)


if __name__ == "__main__":
    main()
