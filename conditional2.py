#Nested if..else Conditional Statement
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

#Ternary Conditional Statement
#A ternary conditional statement is a compact way to write an if-else condition in a single line. 
# It’s sometimes called a "conditional expression."

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

#Match case Statment
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")


        