class Solution:
    def pattern1(self, n):
        for i in range(1 ,n + 1):

            for j in range(i):
                print("*" , end=" ")
            print()

obj = Solution()
obj.pattern1(5) 
           
# output:
# *
# * *       
# * * *
# * * * *
# * * * * *

            
class Solution:
    def pattern1(self, n):
        for i in range(1 ,n + 1):
            for j in range(i):
                print("*" , end=" ")
            print()

obj = Solution()
obj.pattern1(2)

# output:
# *
# * *