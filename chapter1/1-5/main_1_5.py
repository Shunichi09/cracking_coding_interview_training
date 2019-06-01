import argparse


def main_py(string):
    """
    Parameters
    -----------
    """
    original_string = string
    string = list(string)

    str_length = len(string)
    char_count = 1
    current_char = string[0]
    concated_string = ''

    for char in string[1:]:
        if current_char == char:
            char_count += 1
        else:
            temp_char = current_char + str(char_count)
            concated_string += temp_char
            # reset
            char_count = 1
            current_char = char

    # last
    temp_char = current_char + str(char_count)
    concated_string += temp_char

    print(concated_string)

    if len(list(concated_string)) >= str_length:
        return original_string

    return concated_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # python
    parser.add_argument('-t', '--prog_type', type=str, default="py")
    args = parser.parse_args()

    case_1 = "aabcccccaaa"
    case_2 = "aaaccbb"
    case_3 = "acb"

    if args.prog_type == "py":
        assert main_py(case_1) == "a2b1c5a3", "error"
        assert main_py(case_2) == "a3c2b2", "error"
        assert main_py(case_3) == "acb", "error"
        print("clear!!")