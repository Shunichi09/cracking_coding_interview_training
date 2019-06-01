import argparse

def main_py(string):
    """
    Parameters
    -----------
    """
    # strings = list(strings).replace(' ')
    string = string.split(" ")
    
    concated_string = ""

    for char in string:
        if not char == "":
            if not char is string[-1]:
                char += "%20"
            
            concated_string += char
    
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