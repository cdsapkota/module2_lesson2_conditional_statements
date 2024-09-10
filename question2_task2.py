num_one = int(input("Please enter the first number: "))
num_two = int(input("Please enter the second number: "))
num_three = int(input("Please enter the third number: "))

if num_one < num_two and num_one < num_three:
    print(f"{num_one} is the smallest number.")
elif num_two < num_one and num_two < num_three:
    print(f"{num_two} is the smallest number.")
else:
    print(f"{num_three} is the smallest number.")