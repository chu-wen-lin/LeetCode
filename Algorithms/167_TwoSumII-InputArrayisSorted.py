class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 1: two pointers
        # Time complexity: O(N)
        # Space complexity: O(1)

        left, right = 0, len(numbers) - 1

        while left < right:
            summation = numbers[left] + numbers[right]

            if summation == target:
                return [left + 1, right + 1]  # according to problem description, array index starts from 1

            elif summation < target:
                left += 1

            elif summation > target:
                right -= 1

        # Solution 2: hash map
        # Time complexity: O(N)
        # Space complexity: O(N) max(len(hash_map)) equals to len(nums)-1
        # hashmap = {}  # build a dict to store index and value
        # for index, value in enumerate(numbers):
        #     # (target - value) already in hash --> return index & hash's "value"
        #     if target - value in hashmap:
        #         return [hashmap[target - value], index + 1]
        #     # (target - value) not in hash --> store its index and value into hash
        #     else:
        #         hashmap[value] = index + 1

        # Solution 3: binary search
        # Time Complexity: O(NlogN) result in TLE
        # Each number we do a binary search, and each binary search is O(logN),
        # so overall time complexity is O(NlogN).
        # Space Complexity: O(1)
        # for i in range(len(numbers)):
        #     left, right = i + 1, len(numbers) - 1
        #     temp = target - numbers[i]
        #
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #
        #         if numbers[mid] == temp:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < temp:
        #             left = mid + 1
        #         else:
        #             left = mid - 1

