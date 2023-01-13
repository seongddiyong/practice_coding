#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    double arr[1001];
    double max = 0;
    double sum = 0;
    int count=0;

    for(int i=0; i<n; i++) {
        cin >> arr[i];
        if(i == (n-1)) {
            sort(arr, arr + n);
            max = arr[n-1];
        }
    }
    for(int i=0; i<n; i++){
        arr[i] = arr[i]/max*100;
        sum += arr[i];
    } 
    // 이 부분의 for이 딱히 상관 없을 수도 있다.
    //문제에서는 최댓값은 계산하지 말라는 말은 안했기에
    // 그대로 묶어서 한 번에 계산하는게 더 빠르다.
    cout << (sum/n);
}