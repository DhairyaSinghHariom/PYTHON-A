
# if 
age = 20
if age >= 18:
    print("Eligible to vote.")


# ifelse

age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# example
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")


# if elif else

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# Nested
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


# Ternary statement

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

# Match case statement

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
