#include <iostream>
#include <algorithm>  // sort
#include <stdio.h>
#include <string.h>

using namespace std;

#define SIZE_OF_ARRAY(array) (sizeof(array)/sizeof(array[0])-1)

bool check_same_by_sort(char* string_1, int size_string_1, char* string_2, int size_string_2){

    // まず長さを確認
    if (size_string_1 != size_string_2){
        return false;
    }

    // cout << string_1 << endl;
    // cout << string_2 << endl;

    // ２つをソートして確認
    sort(string_1, string_1+size_string_1);
    sort(string_2, string_2+size_string_2);

    // cout << string_1 << endl;
    // cout << string_2 << endl;

    //比較、strcmpは一致で0を返す
    if (strcmp(string_1, string_2)==0){
        return true;
    }
    else{
        return false;
    }
}

int main(){

    bool ans;

    char case_1_1[] = "ttest";
    char case_1_2[] = "tsett";

    // ２つをソートして確認
    ans = check_same_by_sort(case_1_1, SIZE_OF_ARRAY(case_1_1), case_1_2, SIZE_OF_ARRAY(case_1_2));
    cout << "case 1 : " << ans << endl;

    char case_2_1[] = "tes";
    char case_2_2[] = "sit";
    ans = check_same_by_sort(case_2_1, SIZE_OF_ARRAY(case_2_1), case_2_2, SIZE_OF_ARRAY(case_2_2));
    cout << "case 2 : " << ans << endl;
    
    char case_3_1[] = "hello";
    char case_3_2[] = "helldss";
    ans = check_same_by_sort(case_3_1, SIZE_OF_ARRAY(case_3_1), case_3_2, SIZE_OF_ARRAY(case_3_2));
    cout << "case 3 : " << ans << endl;
}