import argparse


def main_py(string_1, string_2):
    """
    片方をソート、もう片方をソートして比較
    教科書もソートを使ってるのでこれでよし
    """
    # string 1
    sorted_string_1 = list(sorted(list(string_1)))
    sorted_string_1 = ''.join(sorted_string_1)

    # string 2
    sorted_string_2 = list(sorted(list(string_2)))
    sorted_string_2 = ''.join(sorted_string_2)

    if sorted_string_1 == sorted_string_2:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str,
                        default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1_1 = "ttest"
    case_1_2 = "tsett"

    case_2_1 = "tes"
    case_2_2 = "set"

    case_3_1 = "hello"
    case_3_2 = "hells"

    if args.prog_type == "py":
        assert main_py(case_1_1, case_1_2), "error"
        assert main_py(case_2_1, case_2_2), "error"
        assert not main_py(case_3_1, case_3_2), "error"

        print("clear!!")
