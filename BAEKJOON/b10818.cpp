#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[1000000];
    int max, min = 0;
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
        if(arr[i] > 1000000 || arr[i] < -1000000) {
            cout << "error";
            --i;
        }
        if(i == 0) {
            max = arr[i];
            min = arr[i];
        }
        else if(arr[i] > max) {
            max = arr[i];
        }
        else if(arr[i] < min) {
            min = arr[i];
        } else continue;
    }
    cout << min << " " << max << endl;
}