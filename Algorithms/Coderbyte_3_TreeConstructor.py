# Check if an array of integer pairs can form a binary tree properly.
# HINT:
# (1) each node have at most 2 children
# (2) each node have at most 1 parent – the root does not have parents

# Example 1:
# Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: True

# Example 2:
# Input:  ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
# Output: False

from typing import List
# solution 1
# def TreeConstructor(strArr: List[str]):
#     from collections import Counter
#     parents = []
#     children = []
#
#     for pair in strArr:
#         pair_list = pair.split(',')
#         children.append(int(pair_list[0][1:]))
#         parents.append(int(pair_list[1][:-1]))
#
#     for v in Counter(parents).values():
#         if v > 2:
#             return False
#     for v in Counter(children).values():
#         if v > 1:
#             return False
#
#     return True


# solution 2:
# Time Complexity: O(N) because we iterate each pair exactly once
# Space Complexity: O(N) if tree is valid, length of parent dictionary equals to number of pairs
def TreeConstructor(strArr: List[str]):
    parents = {}   # {node: itsparent}
    children = {}  # {itsparent: children_num}
    for s in strArr:
        node, itsparent = map(int, s.replace("(", "").replace(")", "").split(','))
        # print(node, itsparent)

        if node in parents:  # 這個node已經有parent了
            return False
        else:
            parents[node] = True

        if itsparent in children:
            children[itsparent] += 1
            if children[itsparent] > 2:  # 這個node的小孩超過2個
                return False
        else:
            children[itsparent] = 1
    return True


print(TreeConstructor(["(1,2)", "(2,4)", "(7,2)"]))
