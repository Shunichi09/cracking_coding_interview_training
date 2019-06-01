# include <iostream>
using namespace std;

/*
1文字の時は''←この記号。複数の文字数の時は""←この記号。
この時メモリにはASCⅡコードに対応した数字（コード）が格納される
*/

/* 配列の長さを求める場合は
    sizeof(array)/sizeof(array[0]);
    これでintとかだとサイズが大きくなりすぎること防ぐ
*/

// p171参考（ノーベルの教科書）
// c++は配列を引数に取る場合は次のように書く
// g++ は char array[]だと通らない。。。
bool checkDuplicate(char* array, int array_size){
    // first check    
    if (array_size > 256){return false;}

    bool char_set[256];
    int val;

    for (int i = 0; i < array_size; i++){
        val = int(array[i]);  // c++はこれでASCIIが獲得可能
        cout << array[i] << " : " << val << endl;

        if (char_set[val]){
            return false;
        }
        char_set[val] = true;
    }
    return true;
}

int main(){
    // test case
    char case_1[6] = "ttest";
    char case_2[4] = "tes";
    char case_3[6] = "hello";

    bool ans;
    // case 1
    int array_size = sizeof(case_1)/sizeof(case_1[0]) - 1;  //サイズ
    cout << case_1 << " : " << array_size << endl;
    ans = checkDuplicate(case_1, array_size);
    cout << "case_1 : " << ans << endl;

    // case 2    
    array_size = sizeof(case_2)/sizeof(case_2[0]) - 1;  //サイズ
    cout << case_2 << " : " << array_size << endl;
    ans = checkDuplicate(case_2, array_size);
    cout << "case_2 : " << ans << endl;
    
    // case 3
    array_size = sizeof(case_3)/sizeof(case_3[0]) - 1;  //サイズ
    cout << case_3 << " : " << array_size << endl;
    ans = checkDuplicate(case_3, array_size);
    cout << "case_3 : " << ans << endl;
}
