### 1099. Two Sum Less Than K

Source: https://leetcode.com/problems/two-sum-less-than-k/ (premium/locked problem) 

Given an array $A$ of integers and integer $K$, return the maximum $S$ such that there exists $i < j$ with $A[i] + A[j] = S$ and $S < K$. If no $i, j$ exist satisfying this equation, return $-1$.

**Example 1**
    
    Input: A = [34,23,1,24,75,33,54,8], K = 60
    Output: 58
    Explanation: 
    We can use 34 and 24 to sum 58 which is less than 60.

**Example 2**

    Input: A = [10,20,30], K = 15
    Output: -1
    Explanation: 
    In this case it's not possible to get a pair sum less that 15.

**Constraints**
- $1 <= A.length <= 100$
- $1 <= A[i] <= 1000$
- $1 <= K <= 2000$


---
### Similar problem: 
Given an array $A$ of integers and integer $K$, return $[i,j]$ such that there exists $i < j$ with $A[i] + A[j] = S$ and $S < K$.
If no $i, j$ exist satisfying this equation, return empty list. The answer must exclude duplicates.


**Example 1**

    Input: A = [1, 2, 3, 4]. K = 4
    Output: [[1, 2]]

**Example 2**
    
    Input: A = [1, 2, 3]. K = 3
    Output: []

**Example 3**

    Input: A = [1, 2, 2, 3, 4]. K = 5
    Output: [[1, 3], [2, 2]]

