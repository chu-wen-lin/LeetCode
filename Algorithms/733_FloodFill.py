class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        length, width = len(image), len(image[0])

        originalColor = image[sr][sc]

        if originalColor == newColor:  # base case
            return image

        # solution 1: recursive
        #         def dfs(sr: int, sc:int):
        #             if image[sr][sc] == originalColor:
        #                 image[sr][sc] = newColor

        #                 if sr - 1 >= 0: #上
        #                     print(sr-1, sc)
        #                     dfs(sr-1, sc)

        #                 if sr + 1 < length: #下
        #                     print(sr+1, sc)
        #                     dfs(sr+1, sc)

        #                 if sc - 1 >= 0: #左
        #                     print(sr, sc-1)
        #                     dfs(sr, sc-1)

        #                 if sc + 1 < width: #右
        #                     print(sr, sc+1)
        #                     dfs(sr, sc+1)

        #         dfs(sr, sc)
        # return image

        # solution 2: iterative
        stack = [(sr, sc)]
        while stack:
            sr, sc = stack.pop()
            if image[sr][sc] == originalColor:
                image[sr][sc] = newColor

                if sr - 1 >= 0:
                    stack.append((sr - 1, sc))
                if sr + 1 < length:
                    stack.append((sr + 1, sc))
                if sc - 1 >= 0:
                    stack.append((sr, sc - 1))
                if sc + 1 < width:
                    stack.append((sr, sc + 1))

        return image

