num = 123
rev = 0
while  num > 0 :
    
    rem = num % 10
    
    rev = rev * 10 + rem
    
    num = num // 10
    
print(rev)

# Output: 321

# # String Method

# num = 123

# num_str = str(num)


# reverse = num_str[0:1]

# print(reverse)
# num = 123
# rev = 0
# while  num > 0 :
    
#     rem = num % 10
    
#     rev = rev * 10 + rem
    
#     num = num // 10
    
# print(rev)