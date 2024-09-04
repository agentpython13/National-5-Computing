lottery_numbers = []
for repeat in range(6):
    number = int(input("Enter number: "))
    while number < 1 or number > 49:
        print("Invalid Number!")
        number = int(input("Enter number: "))
    lottery_numbers.append(number)

for num in range(6):
    print(lottery_numbers[num])
    
        
