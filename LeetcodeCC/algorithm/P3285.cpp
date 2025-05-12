/**
 * Author: Deean
 * Date: 2025-05-12 23:09
 * FileName: P3285.cpp
 * Description: 
 */

#include "../lib/leetcode.h"

using namespace std;

class Solution {
public:
    vector<int> stableMountains(vector<int>& height, int threshold) {
        vector<int> index;
        for (int i = 1; i < height.size(); i++) {
            if (height[i - 1] > threshold) {
                index.push_back(i);
            }
        }
        return index;
    }
};

int main() {
    vector nums = {1, 2, 3, 4, 5};
    vector ans = Solution().stableMountains(nums, 2);
    cout << toString(ans) << endl;
    return 0;
}
