#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;   // 테스트 케이스 수
    int x1,x2,y1,y2;
    int n;
    int cx[50], cy[50], r[50];
    double sd[50], ed[50];
    while(T--){
        int count = 0;
        // 아래는 입력
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> cx[i] >> cy[i] >> r[i];

            sd[i] = sqrt(pow(x1-cx[i],2)+pow(y1-cy[i],2));
            ed[i] = sqrt(pow(x2-cx[i],2)+pow(y2-cy[i],2));

            if(sd[i] > r[i] && ed[i] < r[i]) count++;
            else if(sd[i] < r[i] && ed[i] > r[i]) count ++;
        }
        cout << count << endl;
    }
}

/** 배열을 굳이 사용할 필요가 없었을 것 같다. 그냥 for문 안에서 다 해결하고 count 변수에
 * 저장만 해주었다면 괜찮았을 것 같다.
*/