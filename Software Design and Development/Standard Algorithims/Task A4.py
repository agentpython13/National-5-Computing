prev = float(input('Enter prev. meter reading!'))
current = float(input('Enter current meter reading!'))
if current < prev:
    print("Error, try again!")
    current = float(input())
unit_cost = float(input('Enter unit cost!'))
