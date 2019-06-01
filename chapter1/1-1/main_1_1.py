import argparse

def main_py(string):
    """
    pythonにおける解法
    """

    if len(list(string)) == len(set(list(string))):
        # there is no same str
        return True
    else:
        # there is the same str
        return False

def main_like_cpp(string):
    """
    c++ likeな解法
    """

    if len(string) > 256:  # because these is not strings whose length is more than 256 in the case of using ASCII 
        return False
    
    boolean_char_sets = [False for _ in range(256)]

    for char in list(string):
        val = ord(char)  # ordがASCIIのコードを取得可能
        print("char : {0}, val : {1}".format(char, val))
        if boolean_char_sets[val]:  # 文字が出現している
            return False
        boolean_char_sets[val] = True

    return True 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--prog_type', type=str, default="py")  # 実行するプログラムタイプ
    args = parser.parse_args()

    case_1 = "ttest"
    case_2 = "tes"
    case_3 = "hello"

    if args.prog_type == "py":
        assert not main_py(case_1), "error"
        assert main_py(case_2), "error"
        assert not main_py(case_3), "error"
        print("clear!!")

    if args.prog_type == "cpp":
        assert not main_like_cpp(case_1), "error"
        assert main_like_cpp(case_2), "error"
        assert not main_like_cpp(case_3), "error"
        print("clear!!")