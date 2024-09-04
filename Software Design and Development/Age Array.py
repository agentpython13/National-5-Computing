array = []
for num in range(10):
    age = int(input(f"Enter age of Person {num+1}: "))
    while age < 1 or age > 120:
        print("Invalid Age")
        age = int(input(f"Enter age of Person {num+1}: "))
    array.append(age)
print(array)
        
