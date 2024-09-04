no = int(input("How many contestants are there? "))
qual = float(input("What is the qualification mark? "))

for contestant in range(no):
    array = []
    for judge in range(4):
        score = float(input(f"What is Contestant {contestant + 1}'s score, Judge {judge + 1}?"))
        while score < 0 or score > 6.0:
            print("Invalid Score!")
            score = float(input(f"What is Contestant {contestant + 1}'s score, Judge {judge + 1}?"))
        array.append(score)
    if sum(array) >= qual:
        print(f"Constestant {contestant +1} has qualified!")
    else:
        print(f"Constestant {contestant +1} been eliminated!")
    print()
        
            
    
