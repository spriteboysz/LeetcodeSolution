/**
 * Author: Deean
 * Date: 2025-05-11 22:27
 * FileName: P2769.cpp
 * Description: 2769. 找出最大的可达成数字
 */

#include "../lib/code.h"

using namespace std;

class Solution {
public:
    int theMaximumAchievableX(int num, int t) {
        return num + t * 2;
    }
};

int main() {
    int ans = Solution().theMaximumAchievableX(3, 2);
    cout << ans << endl;
    return 0;
}
