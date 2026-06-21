class Solution:
    def pattern1(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

obj = Solution()
obj.pattern1(5)

# output:
# 1
# 12
# 123
# 1234
# 12345

class Solution:
    def pattern1(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

obj = Solution()
obj.pattern1(2)

# output:
# 1
# 12
