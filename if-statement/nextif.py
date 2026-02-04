i = 10
if i == 10:
 
    #  First if statement
    if i < 15:
        print("i is smaller than 15")
        
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
  print("i is not equal to 10")