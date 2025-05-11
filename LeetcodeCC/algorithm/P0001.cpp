/**
 * Author: Deean
 * Date: 2025-05-11 09:28
 * FileName: P0001.cpp
 * Description:
 */

#include "../lib/code.h"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main() {
    vector nums = {2, 7, 11, 15};
    vector ans = Solution().twoSum(nums, 9);
    cout << ans.size() << endl;
    return 0;
}
