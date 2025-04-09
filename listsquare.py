squares = [x**2 for x in range(1, 21) if x % 2 == 0]

total = sum(squares)

print("List of squares of even numbers from 1 to 20:", squares)
print("Sum of squares:",total)
