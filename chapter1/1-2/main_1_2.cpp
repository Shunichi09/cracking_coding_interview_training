#include <iostream>
using namespace std;

/* c++においてポインターが指してる値を見るには、*pにすれば良い、p自体は、アドレス
aが変数で、そのアドレスを見たい場合は、&aにする
*/

void reverse(char *str) {
  char *end = str;  // ポインターで一番初めを指す
  char temp;

  // まず空文字を探す
  // 最初のif文は空だった場合の判断
  if (str) {
    while (*end) {
      ++end;  // 終端のポインターまですすめる、*endで空文字かどうかの判断
    }

    --end;  // 必要なのは1つ前

    while (str < end) {  // アドレスを比較するstrはstartの意味
      temp = *str;       // strが今指してる変数

      *str = *end;  // strが指してるところにendが指しているものに代入
      *end = temp;

      ++str;  // 更新
      end--;
    }
  }
}

int main() {
  char case_1[6] = "ttest";
  char case_2[4] = "tes";
  char case_3[6] = "hello";

  cout << "before : " << case_1 << endl;
  reverse(case_1);
  cout << "after : " << case_1 << endl;

  cout << "before : " << case_2 << endl;
  reverse(case_2);
  cout << "after : " << case_2 << endl;

  cout << "before : " << case_3 << endl;
  reverse(case_3);
  cout << "after : " << case_3 << endl;
}