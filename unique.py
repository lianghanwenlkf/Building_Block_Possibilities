import json
import math

import numpy as np
from tqdm import tqdm

# 计算两个点之间的欧几里得距离
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def calculate_center(points):
    return np.mean(points, axis=0)

# 读取JSON文件
with open('valid_sets.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(len(data))
check = []
unique_data = {}

for index, buildings in tqdm(enumerate(data)):
    temp_list = []
    for i in range(len(buildings)-1):
        temp =0
        for j in range(len(buildings[i])):
            for k in range(len(buildings[i+1])):
                temp += (i+1)*(i+1)*(i+1)*euclidean_distance(buildings[i][j], buildings[i+1][k])+(i+1)*(i+1)*euclidean_distance(buildings[i][j], [2, 2, 2])
        temp_list.append(round(temp))
    temp_list.append(euclidean_distance(calculate_center(buildings[2]), calculate_center(buildings[6])))

    if temp_list not in check:
        check.append(temp_list)
        unique_data[len(check)] = [buildings]
    else:
        unique_data[check.index(temp_list) + 1].append(buildings)

print(len(unique_data))
for key, value in unique_data.items():
    if len(value) != 24:
        print(f'key={key}, len={len(value)}')
# 将去重后的数据保存到新的JSON文件
with open('valid_sets_unique.json', 'w', encoding='utf-8') as file:
    json.dump(unique_data, file, ensure_ascii=False)

print("去重后的数据已保存到 output.json 文件。")
