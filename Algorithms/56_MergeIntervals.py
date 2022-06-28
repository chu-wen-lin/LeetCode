class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # overlap: current interval begins after the previous interval ends
        # 1. Sort the intervals by start value
        # 2. ontinue comparing the start of the current interval and the end of the previous interval
        # a. If current interval begins after the previous interval ends,
        #    then they do not overlap and we just append the current interval to merged_intervals.
        # b. Else(Overlapping),
        #    If current interval ends after previous interval, merge them by updating the end of the previous interval

        # Time Complexity: O(NlogN)
        # sort invocation: O(NlogN); linear scan: O(N) So the runtime is dominated by the complexity of sorting
        # Space Complexity: O(N)  In the worst-case scenario, len(merged_intervals) is equal to the len(intervals)

        intervals.sort(key=lambda x: x[0])  # sort by start value

        merged_intervals = []

        for i, ele in enumerate(intervals):
            if not merged_intervals or ele[0] > merged_intervals[-1][1]:  # first interval or current interval begins after the previous interval ends
                merged_intervals.append(ele)
            else:  # if current interval ends after previous interval, update the end of the previous interval
                merged_intervals[-1][1] = max(merged_intervals[-1][1], ele[1])

        return merged_intervals
