#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;
unordered_map<string, int> map;

int main() {
    int n;
    cin >> n;

    int maxVal = 0;
    for (int i=0; i<n; i++) {
        string s;
        cin >> s;
        map[s]++;
        maxVal = max(maxVal, map[s]);
    }

    cout << maxVal;
    return 0;
}