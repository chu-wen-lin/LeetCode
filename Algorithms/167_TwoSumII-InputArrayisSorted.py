class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution 1: two pointers
        #         left = 0
        #         right = len(numbers) - 1

        #         while left < right:
        #             summation = numbers[left] + numbers[right]

        #             if summation == target:
        #                 return [left + 1, right + 1] #題目敘述中回傳的array index從1開始

        #             elif summation < target:
        #                 left += 1

        #             elif summation > target:
        #                 right -= 1

        # solution 2: hash map
        hash = {}  # build a dict to store index and value.
        for index, value in enumerate(numbers):
            # (target - value) already in hash --> return index & hash's "value"
            if target - value in hash:
                return [hash[target - value], index + 1]
            # (target - value) not in hash --> store its index and value into hash
            else:
                hash[value] = index + 1

