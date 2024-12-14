import numpy as np
import json
from tqdm import tqdm

# 计算两个点之间的欧几里得距离
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


# 定义旋转矩阵：绕X轴旋转90度、绕Y轴旋转90度、绕Z轴旋转90度
def rotate_x_90(coords):
    # 绕X轴旋转90度的旋转矩阵
    rotation_matrix = np.array([[1, 0, 0],
                                [0, 0, -1],
                                [0, 1, 0]])
    return np.dot(coords, rotation_matrix.T)


def rotate_y_90(coords):
    # 绕Y轴旋转90度的旋转矩阵
    rotation_matrix = np.array([[0, 0, 1],
                                [0, 1, 0],
                                [-1, 0, 0]])
    return np.dot(coords, rotation_matrix.T)


def rotate_z_90(coords):
    # 绕Z轴旋转90度的旋转矩阵
    rotation_matrix = np.array([[0, -1, 0],
                                [1, 0, 0],
                                [0, 0, 1]])
    return np.dot(coords, rotation_matrix.T)


# 旋转四个点
def rotate_points(points):
    rotated_points = []
    for x_rot in range(8):  # 绕X轴旋转0°, 90°, 180°, 270°
        for y_rot in range(8):  # 绕Y轴旋转0°, 90°, 180°, 270°
            for z_rot in range(8):  # 绕Z轴旋转0°, 90°, 180°, 270°
                # 初始化旋转矩阵为单位矩阵
                rotation = np.array(points)

                # 依次应用旋转
                for _ in range(x_rot):
                    rotation = rotate_x_90(rotation)
                for _ in range(y_rot):
                    rotation = rotate_y_90(rotation)
                for _ in range(z_rot):
                    rotation = rotate_z_90(rotation)

                rotated_points.append(rotation)

    return rotated_points

# 计算中心
def calculate_center(points):
    return np.mean(points, axis=0)

# 主函数
def find_buildings(reference_points, output_file_path, points):
    # 计算参考点的中心
    reference_center = calculate_center(reference_points)

    # 用于存储符合条件的四个点
    valid_combinations = []

    # 遍历所有四个点的组合
    for combo in tqdm(points):

        # 旋转四个点
        rotated_points = rotate_points(combo)
        check = False

        for idx, rotation_set in enumerate(rotated_points):

            # 计算旋转后的点的中心
            rotated_center = calculate_center(rotation_set)

            # 平移旋转后的点使得中心与参考点的中心重合
            translation = reference_center - rotated_center
            translated_points = rotation_set + translation

            A = np.array(translated_points)
            B = np.array(reference_points)

            # Step 1: 对 A 中的所有坐标值取整
            A_rounded = np.round(A, 2)
            B_rounded = np.round(B, 2)

            # Step 2: 检查 A 中的每个点是否在 B 中
            # 使用 np.isin() 来验证 A 中的每个点是否存在于 B 中
            # 这里需要确保两个数组的维度一致且是逐元素比较。
            result = np.all(np.isin(A_rounded.view([('', A_rounded.dtype)] * A_rounded.shape[1]),
                                    B_rounded.view([('', B_rounded.dtype)] * B_rounded.shape[1])))

            if result:
                check = True
                break

        if check > 0:
            valid_combinations.append(combo)

    # 将符合条件的组合保存为 JSON 文件
    with open(output_file_path, "w") as json_file:
        # noinspection PyTypeChecker
        json.dump([tuple(map(tuple, combo)) for combo in valid_combinations], json_file, indent=4)

    print(f"\n共找到 {len(valid_combinations)} 个符合条件的组合，并已保存到{output_file_path}文件。")


def main():
    n = 7
    if n == 1:
        reference_points = [(1, 1, 1), (1, 2, 1), (2, 2, 1), (2, 3, 1)]  # 积木1
        input_file_path = f"4_points_combinations.json"
    elif n == 2:
        reference_points = [(1, 2, 1), (1, 1, 1), (2, 1, 1), (2, 1, 2)]  # 积木2
        input_file_path = f"4_points_combinations.json"
    elif n == 3:
        reference_points = [(1, 1, 1), (1, 2, 1), (2, 2, 1), (2, 2, 2)]  # 积木3
        input_file_path = f"4_points_combinations.json"
    elif n == 4:
        reference_points = [(1, 2, 1), (1, 1, 1), (2, 1, 1)]  # 积木4
        input_file_path = f"3_points_combinations.json"
    elif n == 5:
        reference_points = [(1, 1, 1), (2, 1, 1), (2, 2, 1), (3, 1, 1)]  # 积木5
        input_file_path = f"4_points_combinations.json"
    elif n == 6:
        reference_points = [(1, 2, 1), (2, 2, 1), (2, 2, 2), (2, 1, 1)]  # 积木6
        input_file_path = f"4_points_combinations.json"
    else:
        reference_points = [(1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 3, 1)]  # 积木7
        input_file_path = f"4_points_combinations.json"
    output_file_path = f"building_{n}.json"

    with open(input_file_path, 'r') as file:
        data = json.load(file)

    find_buildings(reference_points, output_file_path, data)


# 运行主函数
if __name__ == "__main__":
    main()
