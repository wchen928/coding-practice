class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        if n < m:
            return 0

        def count(dist):
            res, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - dist >= curr:
                    res += 1
                    curr = position[i]
            return res

        position.sort()
        left, right = 0, position[-1] - position[0]

        while left < right:
            mid = (left + right) // 2 + 1
            
            if count(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left