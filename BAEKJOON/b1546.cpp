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
        if(arr[i] > 100 || arr[i] < 0) cout << "error";
        if(i == (n-1)) {
            sort(arr, arr + n);
            max = arr[n-1];
        }
        if(arr[i] == 0) count++;
        if(count == n-2) break; 
    }
    for(int i=0; i<n; i++){
        arr[i] = arr[i]/max*100;
        sum += arr[i];
    }

    cout << (sum/n);
}