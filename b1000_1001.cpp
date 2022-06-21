#include <iostream>
using namespace std;

// 1000 덧셈 문제
void baek1000(int a, int b) {
    int result = a + b;

    cout << "RESULT : " << result << "\n" << endl;
}

// 1001 뺄셈 문제
void baek1001(int a, int b) {
    int result = a - b;

    cout << "RESULT : " << result << "\n" << endl;
}

int main() {
    int a, b;
    cout << "\n수 입력" << endl;
    cin >> a >> b;
    cout << "\nA = " << a << ", B = " << b << endl;
    cout << "\nA + B" << endl;
    baek1000(a,b);
    cout << "A - B" << endl;
    baek1001(a,b);
}