import argparse

def main_py(strings_1, strings_2):
    """
    Parameters
    -----------
    strings_1 : str
    """
    reversed_strings_1 = list(reversed(strings_1))
    reversed_strings_1 = ''.join(reversed_strings_1)

    if reversed_strings_1 == strings_2:
        return True
    else:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str, default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1_1 = "ttest"
    case_1_2 = "tsett"
    
    case_2_1 = "tes"
    case_2_2 = "set"    
    
    case_3_1 = "hello"
    case_3_2 = "hello"

    if args.prog_type == "py":
        assert main_py(case_1_1, case_1_2), "error"
        assert main_py(case_2_1, case_2_2), "error"
        assert not main_py(case_3_1, case_3_2), "error"

        print("clear!!")