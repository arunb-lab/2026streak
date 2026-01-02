#elif statement in Python stands for "else if." 
# It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true. 
# Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.

age = 40
if age <= 10:
    print("Child.")
elif age <= 19:
    print("Teenager")
elif age <=35:
    print("Young Adult")
else :
    print("Adult")
