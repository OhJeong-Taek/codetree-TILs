#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, k, v;
    cin >> n;
    unordered_map<int, int> m;

    for (int i=0; i<n; i++) {
        string s;
        cin >> s;
        if (s == "add") {
            cin >> k >> v;
            m[k] = v;
        }
        else if (s == "find") {
            cin >> k;
            if (m.find(k) != m.end()) {
                cout << m[k];
            } else {
                cout << "None";
            }
            cout << endl;
        }
        else if (s == "remove") {
            cin >> k;
            if (m.find(k) != m.end()){
                m.erase(k);
            }
        }
    }

    return 0;
}