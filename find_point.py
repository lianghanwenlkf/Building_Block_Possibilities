import itertools
import numpy as np
import json
from tqdm import tqdm

# 计算两个点之间的欧几里得距离
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# 主函数
def find_point(n, output_file_path):
    # 生成所有点的组合
    points = [(x, y, z) for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]
    print(len(points))

    # 用于存储符合条件的四个点
    valid_combinations = []

    count = 0

    # 遍历所有四个点的组合，使用 tqdm 显示进度条
    for combo in tqdm(itertools.combinations(points, n), desc="Processing combinations", total=len(list(itertools.combinations(points, n)))):
        count += 1
        is_valid = True
        # 对每个点，检查与其他三个点的距离
        for i, p1 in enumerate(combo):
            min_distance = float('inf')
            # 计算 p1 与其他点的距离
            for j, p2 in enumerate(combo):
                if i != j:
                    distance = euclidean_distance(p1, p2)
                    min_distance = min(min_distance, distance)
            # 如果最小距离大于1.1，则该组合不符合要求
            if min_distance >= 1.1:
                is_valid = False
                break
        # 如果所有点都符合条件，则保存该组合
        if is_valid:
            valid_combinations.append(combo)

    # 将符合条件的组合保存为 JSON 文件
    with open(output_file_path, "w") as json_file:
        json.dump(valid_combinations, json_file, indent=4)

    print(count)
    print(f"\n共找到 {len(valid_combinations)} 个符合条件的组合，并已保存到json文件。")


def main():
    n = 4
    output_file_path = f'{n}_points_combinations.json'
    find_point(n, output_file_path)

# 运行主函数
if __name__ == "__main__":
    main()
