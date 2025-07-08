#include "two_sum.h"
#include <algorithm>

std::vector<int> TwoSum::twoSum(std::vector<int>& nums, int target) {
    
    std::vector<std::pair<int, int>> sortedList;
    for (size_t i = 0; i < nums.size(); i++) {
        sortedList.push_back({nums[i], i});
    }
    sort(sortedList.begin(), sortedList.end());

    size_t l = 0, r = sortedList.size() - 1;
    int sum;

    while (l < r) {
        sum = sortedList[l].first + sortedList[r].first;
        if (sum == target) {
            return {std::min(sortedList[l].second, sortedList[r].second),
                    std::max(sortedList[l].second, sortedList[r].second)};
        } else if (sum > target) {
            r--;
        } else {
            l++;
        }
    }
    return {};
};