#Dental Fillings
#bennetthomas
#31082023

print("Dental Fillings")
print()

print("""
Your choice of fillings is:
    1. Temporary
    2. Amalgram
    3. White
    4. Super White

""")

choice = int(input("Please enter number of choice of filling:"))
number = int(input("How many do you want?"))
                   
cost = 1

if choice == 1:
    cost *= (8 * number)     
if choice == 2:
    cost *= (14 * number)     
if choice == 3:
    cost *= (43 * number)
if choice == 4:
    cost *= (67 * number)
    
print()

print(str(number) + " fillings will cost £" + str(cost))
