/**
 * Author: Deean
 * Date: 2025-05-12 23:00
 * FileName: P3280.cpp
 * Description: 
 */

#include "../lib/leetcode.h"

using namespace std;

class Solution {
public:
    string binary(int x) {
        string s;
        while (x) {
            s.push_back('0' + (x & 1));
            x >>= 1;
        }
        reverse(s.begin(), s.end());
        return s;
    }

    string convertDateToBinary(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));
        return binary(year) + "-" + binary(month) + "-" + binary(day);
    }
};

int main() {
    string ans = Solution().convertDateToBinary("2025-05-12");
    cout << ans << endl;
    return 0;
}
