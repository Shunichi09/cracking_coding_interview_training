import argparse


def main_py(string):
    """
    """
    reversed_string = list(reversed(list(string)))
    reversed_string = ''.join(reversed_string)

    return reversed_string


def main_like_cpp(string):
    """
    c++ likeな解法
    あんまりポインタって考え方ないからpythonで書くの難しい
    """
    # without reverese
    string = list(string)
    left = 0
    right = len(string) - 1

    while left < right:
        temp = string[left]  # bufferに一時保存
        string[left] = string[right]
        string[right] = temp
        left += 1
        right -= 1

    reversed_string = ''.join(string)

    return reversed_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str,
                        default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1 = "ttest"
    case_2 = "tes"
    case_3 = "hello"

    if args.prog_type == "py":
        assert main_py(case_1) == "tsett", "error"
        assert main_py(case_2) == "set", "error"
        assert main_py(case_3) == "olleh", "error"
        print("clear!!")

    if args.prog_type == "cpp":
        assert main_like_cpp(case_1) == "tsett", "error"
        assert main_like_cpp(case_2) == "set", "error"
        assert main_like_cpp(case_3) == "olleh", "error"
        print("clear!!")
