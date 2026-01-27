print("Version 1: Green Alien")
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points for shooting the alien.")

print()  # Empty line for spacing

# Version 2: Running the else block (non-green alien)
print("Version 2: Yellow Alien")
alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points for shooting the alien.")

print()  # Empty line for spacing
# Version 3: Using elif to check multiple colors
print("Version 3: Multiple Alien Colors")
alien_color = input("Enter the alien color (green, yellow, red): ").strip().lower()
if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the alien.")
elif alien_color == 'red':
    print("Congratulations! You just earned 15 points for shooting the alien.")
else:
    print("Unknown alien color. No points awarded.")
    
