array = []
houses = ['Forbes', 'Douglas', 'Stuart', 'Gordon']
name = input()
house = input()
if house not in houses:
    print("Error, try again!")
    house = input()
array.append(name)
array.append(house)
print(array)