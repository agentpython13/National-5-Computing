#Kayaks

#asking for inputs
num = int(input("How many kayaks do you want to hire?"))
instructor = input("Do you want to hire an instructor?")

#validating inputs
if num > 20:
    print("We only have 20 kayaks!")
    num = int(input("How many kayaks do you want to hire?"))
if instructor != "Yes" and instructor != "No":
    print("That is not a valid answer to whether you want a kayak or not: please input 'yes' or 'no'")
    instructor = input("Do you want to hire an instructor?")
    
#setting total
total = 0

#adding price of kayaks to total
total += num * 25

#adding price of instructor if needed to total
if instructor == "Yes":
    total += 80

#outputting total
print(f"Your total comes out to £{total}")
    
