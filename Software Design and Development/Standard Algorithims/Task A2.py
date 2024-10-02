name = input()
age = int(input())
while age < 11 or age > 18:
    print("Error, try again!")
    age = int(input())
print(f"{name}, welcome to the talent show!")