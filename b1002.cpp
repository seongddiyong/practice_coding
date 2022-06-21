#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // t : number of test case
    // x,y : axis
    // r : distance
    int t, x1, y1, r1, x2, y2, r2, result;
    // dis : distance between two turret
    double dis;

    //cout << "insert number of test case" << endl;
    cin >> t;

    while(t > 0) {
        //cout << "insert x1 y1 r1 x2 y2 r2" << endl;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

        dis = sqrt(pow(x2-x1,2)+pow(y2-y1,2));

        // 원이 겹칠 때
        if(dis == 0 && r1 == r2) result = -1;
        // 원의 교점이 두개일 때
        // r1 + r2 가 거리보다 크면 교점이 두개
        // r2 - r1 의 절대값이 거리보다 적어도 두개
        else if(dis < r1 + r2 && abs(r2-r1) < dis) result = 2;
        // 원의 교점이 하나일 때
        // r1 + r2와 거리가 같다면 무조건 하나의 접점이 생김
        // 또한 
        else if(dis == r1 + r2) result = 1;
        else {
            result = 0;
        }

        cout << result << endl;

        t--;
    }

}