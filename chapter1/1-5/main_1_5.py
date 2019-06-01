import argparse

def main_py(strings):
    """
    Parameters
    -----------
    """
    original_strings = strings
    strings = list(strings)
    
    str_length = len(strings)
    str_count = 1
    current_str = strings[0]
    concated_strings = ''

    for j, string in enumerate(strings[1:]):
        if not current_str == string:
            temp_str = current_str + str(str_count)
            concated_strings += temp_str
            # reset
            str_count = 1
            current_str = string

        elif j+2 == str_length:  # last
            temp_str = current_str + str(str_count + 1)
            concated_strings += temp_str
        
        else:
            str_count += 1
    
    print(concated_strings)

    if len(list(concated_strings)) >= str_length:
        return original_strings
    

    return concated_strings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str, default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1 = "aabcccccaaa"
    case_2 = "aaaccbb"
    case_3 = "acb"

    if args.prog_type == "py":
        # assert main_py(case_1) == "a2b1c5a3", "error"
        # assert main_py(case_2) == "a3c2b2", "error"
        assert main_py(case_3) == "acb", "error"

        print("clear!!")