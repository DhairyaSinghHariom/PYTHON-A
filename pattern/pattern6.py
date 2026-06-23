# Pattern 
class Solution:
    def pattern1(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

obj = Solution()
obj.pattern1(5)

# output:

# 12345
# 1234
# 123
# 12    
# 1


class Solution:
    def pattern1(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

obj = Solution()
obj.pattern1(2)

# output:
# 12
# 1
