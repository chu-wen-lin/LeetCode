class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array非sorted，不像167可用two pointer或binary search做
        hash = {}  # build a dict to store index and value
        for index, value in enumerate(nums):
            # (target - value) already in hash --> return index & hash's "value"
            if target - value in hash:
                return [hash[target - value], index]
            # (target - value) not in hash --> store its index and value into hash
            else:
                hash[value] = index
