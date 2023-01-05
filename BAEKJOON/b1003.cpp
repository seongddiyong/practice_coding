#include <iostream>
using namespace std;

long long arr[50] = {0,1,};

long long fibonacci(int n) {
    if (n == 0 || n == 1) {
        return arr[n];
    } else if (arr[n] == 0) {
        arr[n] = fibonacci(n-1) + fibonacci(n-2);
    }
    return arr[n];
}

int main(){
    int T,N;
    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> N;
        if(N==0) cout << "1 0" << endl;
        else cout << fibonacci(N-1) << ' ' << fibonacci(N) << endl;
    }
}