age = int(input("Enter your age: "))

if age < 5:
    print("The ticket price is: Free")
elif 5 <= age <= 18:
    print("The ticket price is: ₹100")
elif 19 <= age <= 60:
    print("The ticket price is: ₹200")
else:
    print("The ticket price is: ₹150")
