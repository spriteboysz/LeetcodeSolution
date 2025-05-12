/**
 * Author: Deean
 * Date: 2025-05-11 22:29
 * FileName: P3512.cpp
 * Description: 3512. 使数组和能被 K 整除的最少操作次数
 */

#include "../lib/codec.h"

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum % k;
    }
};

int main() {
    vector nums = {3, 9, 7};
    int ans = Solution().minOperations(nums, 5);
    cout << ans << endl;
    return 0;
}
