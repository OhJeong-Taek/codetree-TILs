#include <iostream>
#include <unordered_map>

using namespace std;
int n, m;
unordered_map<int, int> map;

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        int val;
        cin >> val;
        map[val]++;
    }

    for (int i=0; i<m; i++) {
        int val;
        cin >> val;
        cout << map[val]<< ' ';
    }
    return 0;
}