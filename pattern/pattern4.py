class Solution:
    def pattern1(self, n):
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end="")
            print()

obj = Solution()
obj.pattern1(5)

# output:
# 1
# 22
# 333
# 4444
# 55555

class Solution:
    def pattern1(self, n):
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end="")
            print()

obj = Solution()
obj.pattern1(2)

# output:
# 1
# 22
