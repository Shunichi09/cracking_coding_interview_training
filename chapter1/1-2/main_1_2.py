import argparse

def main_py(strings):
    """
    """
    reversed_strings = list(reversed(strings))
    reversed_strings = ''.join(reversed_strings)

    return reversed_strings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str, default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1 = "ttest"
    case_2 = "tes"
    case_3 = "hello"

    if args.prog_type == "py":
        assert main_py(case_1) == "tsett", "error"
        assert main_py(case_2) == "set", "error"
        assert main_py(case_3) == "olleh", "error"

        print("clear!!")