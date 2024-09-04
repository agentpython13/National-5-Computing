#Tuck Shops
#benenetthomas
#31082023

print("Tuck Shop")
print()

print("""
Your choices are:
    1 .Crisps: 50p
    2. Cans: 80p
    3. Chocolate: 70p
    4. Water: 40p
""")

choice = int(input("Enter number of item you wish to purchase"))
number = int(input("Enter number of the item chosen you wish to purchase"))
cost = 1
print()

if choice == 1:
    cost *= number * 50
elif choice == 2:
    cost *= number * 80
elif choice == 3:
    cost *= number * 70  
else:
    cost *= number * 40


print("The cost of your purchase is ", cost, "pence")
