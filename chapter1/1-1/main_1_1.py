import argparse

def main_py(strings):
    """
    pythonにおける解法
    """

    if len(list(strings)) == len(set(list(strings))):
        # there is no same str
        return False
    else:
        # there is the same str
        return True

def main_like_cpp(strings):
    """
    c++ likeな解法
    """

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str, default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1 = "ttest"
    case_2 = "tes"
    case_3 = "hello"

    if args.prog_type == "py":
        assert main_py(case_2), "error"
        print("clear!!")