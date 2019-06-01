import argparse

def main_py(strings):
    """
    Parameters
    -----------
    """
    # strings = list(strings).replace(' ')
    strings = strings.split(" ")
    
    concated_string = ""

    for string in strings:
        if not string == "":
            if not string is strings[-1]:
                string += "%20"
            
            concated_string += string
    
    return concated_string

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str, default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1 = "tt  est"
    case_2 = "te s"
    case_3 = "he  llo"

    if args.prog_type == "py":
        assert main_py(case_1) == "tt%20est", "error"
        assert main_py(case_2) == "te%20s", "error"
        assert main_py(case_3) == "he%20llo", "error"

        print("clear!!")