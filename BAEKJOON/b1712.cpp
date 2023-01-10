#include <iostream>
using namespace std;

int main(){
    unsigned int A, B, C;
    cin >> A >> B >> C;
    int i = 0;
    if(B>=C) i = -1;
    else i = (A/(C-B))+1;
    // 위의 수식은 손익분기점 식을 재정리하여 넣은 것 - 난이도가 확 낮아짐
    cout << i << endl;
}