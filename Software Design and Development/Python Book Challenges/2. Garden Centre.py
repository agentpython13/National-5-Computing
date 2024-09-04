#Garden Center
#bennetthomas
#31082023

print("Garden Center Program")
print()

tulip_spend = int(input("How much did you spend on tulips?"))
crocus_spend = int(input("How much did you spend oncrocuses?"))
snowdrop_spend = int(input("How much did you spend on snowdrops?"))
daffodil_spend = int(input("How much did you spend on daffodils?"))

total_spend = tulip_spend + crocus_spend + snowdrop_spend + daffodil_spend

print()
print("Total spent on bulbs was £", total_spend)

if  total_spend > 30:
    print()
    print("Please accept a gift of a free hyacinth bulb!")
