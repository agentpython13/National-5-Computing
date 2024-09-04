choices = []
choice = True

#looping through inputs
for student in range(5):
    #receiving inputs
    name = input()
    age = int(input())
    #checking if age is valid
    if age < 12 or age > 17:
        choice = False
    test1 = int(input())
    test2 = int(input())
    #checking if test scores are valid
    if test1 + test2 < 70:
        choice =  False
    #adding name to choices if pupil is valid
    if choice  == True:
        choices.append(name)
print()
#printing accepted pupils
if len(choices) >= 1:
    for name in choices:
        print(f"{name} was accepted!")
    
    
