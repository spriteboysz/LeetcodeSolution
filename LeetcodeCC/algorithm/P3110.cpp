/**
 * Author: Deean
 * Date: 2025-05-11 22:15
 * FileName: P3110.cpp
 * Description: 3110. 字符串的分数
 */

#include "../lib/codec.h"

using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        for (int i = 1; i < s.length(); i++) {
            score += abs(s[i] - s[i - 1]);
        }
        return score;
    }
};

int main() {
    int ans = Solution().scoreOfString("hello");
    cout << ans << endl;
    return 0;
}
