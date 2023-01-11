#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    int arr[101] = {0};
    int v;
    int result=0;
    for(int i=0; i < n; i++) {
        cin >> arr[i];
        if(arr[i] > 100 || arr[i] < -100) {
            cout << "error";
            --i;
        }
    }
    cin >> v;
    for(int i = 0; i < n; i++) {
        if(arr[i] == v) result++;
    }
    cout << result << endl;
}