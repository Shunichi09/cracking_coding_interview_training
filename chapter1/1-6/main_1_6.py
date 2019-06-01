import argparse


def main_py(image):
    """

    Parameters
    ----------
    image : 
        
    """
    for num_layer in range(int(len(image) / 2)):  # レイヤー毎に

        first = num_layer  # 四角レイヤーの位置
        last = len(image) - num_layer - 1  # 四角レイヤーの大きさ

        for i in range(first, last): # そこのレイヤーの大きさの分
            offset = i - first  # 今どこの位置を指してるか、最初は左上から

            # 上の値を保存
            top = image[first][i]

            # 左から上へ
            image[first][i] = image[last-offset][first]

            # 下から左へ
            image[last-offset][first] = image[][]









if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--prog_type', type=str, default="py")
    args = parser.parse_args()

    case_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    case_1_ans = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    if args.prog_type == "py":
        assert main_py(case_1) == case_1_ans, "error"
        print("clear!!")