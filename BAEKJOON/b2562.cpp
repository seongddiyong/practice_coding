#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    unsigned int arr1[9] = {0};
    unsigned int arr2[9] = {0};
    for(int i=0; i<9; i++) {
        cin >> arr1[i];
        // if(arr1[i] > 100 || arr1[i] < 1) cout << "error "; i--;
        arr2[i] = arr1[i];
    }
    sort(arr1, arr1+9);
    cout << arr1[9-1] << "\n";
    int i = 0;
    int ans = 1;
    while(arr2[i] != arr1[8]) {
        if(arr2[i] != arr1[8]) i++; ans++;
    }
    cout << ans;
}