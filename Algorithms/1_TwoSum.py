class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {integer in nums: its index}
        # Time complexity: O(N) worst case: might go through whole nums until the last integer to get the answer
        # Space complexity: O(N) built a dict to store int and their index. max(len(hash_map)) equals to len(nums)-1
        # e.g. [1,2,3,4,5] target = 9
        # We need to iterate whole list to get the answer. hash = {1:0, 2:1, 3:2, 4:3}

        # We could only apply two pointer methods if the array is sorted.
        # While the input array is not sorted, and the time complexity of sorting is O(NlogN).
        # So two pointer is not the best solution for this problem.
        # related topic: 167. Two Sum II - Input Array Is Sorted

        hashmap = {}  # build a dict to store index and value
        for index, value in enumerate(nums):
            # (target - value) already in hash --> return index & hash's "value"
            if target - value in hashmap:
                return [hashmap[target - value], index]
            # (target - value) not in hash --> store its index and value into hash
            else:
                hashmap[value] = index
