import json
from tqdm import tqdm


# 读取多个JSON文件
def load_json_files(filenames):
    all_combinations = []
    for filename in filenames:
        with open(filename, 'r') as file:
            data = json.load(file)
            all_combinations.append(data)
    return all_combinations


# 主函数
def main():
    # 文件列表，假设我们有7个JSON文件
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

    # 用于存储符合条件的7个点组合
    valid_sets = []

    for building_1 in tqdm(all_combinations[0]):
        for building_2 in all_combinations[1]:
            check_1 = []
            for point in building_1:
                check_1.append(point)
            for point in building_2:
                check_1.append(point)
            if len(check_1) != len(set(map(tuple, check_1))):
                continue
            for building_3 in all_combinations[2]:
                check_2 = []
                for point in building_1:
                    check_2.append(point)
                for point in building_2:
                    check_2.append(point)
                for point in building_3:
                    check_2.append(point)
                if len(check_2) != len(set(map(tuple, check_2))):
                    continue
                for building_4 in all_combinations[3]:
                    check_3 = []
                    for point in building_1:
                        check_3.append(point)
                    for point in building_2:
                        check_3.append(point)
                    for point in building_3:
                        check_3.append(point)
                    for point in building_4:
                        check_3.append(point)
                    if len(check_3) != len(set(map(tuple, check_3))):
                        continue
                    for building_5 in all_combinations[4]:
                        check_4 = []
                        for point in building_1:
                            check_4.append(point)
                        for point in building_2:
                            check_4.append(point)
                        for point in building_3:
                            check_4.append(point)
                        for point in building_4:
                            check_4.append(point)
                        for point in building_5:
                            check_4.append(point)
                        if len(check_4) != len(set(map(tuple, check_4))):
                            continue
                        for building_6 in all_combinations[5]:
                            check_5 = []
                            for point in building_1:
                                check_5.append(point)
                            for point in building_2:
                                check_5.append(point)
                            for point in building_3:
                                check_5.append(point)
                            for point in building_4:
                                check_5.append(point)
                            for point in building_5:
                                check_5.append(point)
                            for point in building_6:
                                check_5.append(point)
                            if len(check_5) != len(set(map(tuple, check_5))):
                                continue
                            for building_7 in all_combinations[6]:
                                check_6 = []
                                for point in building_1:
                                    check_6.append(point)
                                for point in building_2:
                                    check_6.append(point)
                                for point in building_3:
                                    check_6.append(point)
                                for point in building_4:
                                    check_6.append(point)
                                for point in building_5:
                                    check_6.append(point)
                                for point in building_6:
                                    check_6.append(point)
                                for point in building_7:
                                    check_6.append(point)
                                if len(check_6) == len(set(map(tuple, check_6))):
                                    valid_sets.append([building_1, building_2, building_3, building_4, building_5, building_6, building_7])

    # 将符合条件的组合保存为新的 JSON 文件
    with open("valid_sets.json", "w") as json_file:
        # noinspection PyTypeChecker
        json.dump(valid_sets, json_file)

    print(f"\n共找到 {len(valid_sets)} 个符合条件的组合，并已保存到 'valid_sets.json' 文件。")


# 运行主函数
if __name__ == "__main__":
    main()