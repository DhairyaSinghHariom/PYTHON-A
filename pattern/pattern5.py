class Solution:
    def pattern1(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

obj = Solution()
obj.pattern1(5)

# output:

# *****
# ****
# ***
# **
# *


class Solution:
    def pattern1(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

obj = Solution()
obj.pattern1(2)

# output:

# **
# *