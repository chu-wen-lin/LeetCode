class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 如果fast指到的元素不等於val，它一定是會是答案的其中一個元素 -> 將fast指到的元素複製到slow位置，然後將兩個指針同時右移；
        # 如果fast指針指向的元素等於val，它不能出現在答案裡，此時slow指針不動，fast指針右移一位
        # Time Complexity: O(N), Space Complexity: O(1) for both solutions

        # Solution 1: two pointer
        fast, slow = 0, 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # Solution 2: two pointer approach too :) Actually, the index in for-loop is fast pointer in solution 1
        start = 0
        for i, item in enumerate(nums):
            if item != val:
                nums[start] = item
                start += 1
        return start
