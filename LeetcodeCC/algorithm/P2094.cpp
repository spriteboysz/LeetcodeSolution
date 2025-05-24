/**
 * Author: Deean
 * Date: 2025-05-13 22:30
 * FileName: P2094.cpp
 * Description: 
 */

#include <iterator>

#include "../lib/leetcode.h"

using namespace std;

class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        int counter[10] = {0};
        for (int digit : digits) {
            counter[digit]++;
        }
        vector<int> ans;
        for (int i = 100; i < 1000; i += 2) {
            int counter1[10];
            copy(begin(counter), end(counter), begin(counter1));

            counter1[i / 100] -= 1;
            counter1[i / 10 % 10] -= 1;
            counter1[i % 10] -= 1;

            bool flag = true;
            for (int j = 0; j < 10; j++) {
                if (counter1[j] < 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

int main() {
    vector digits = {2, 1, 3, 0};
    vector ans = Solution().findEvenNumbers(digits);
    cout << toString(ans) << endl;
    return 0;
}
