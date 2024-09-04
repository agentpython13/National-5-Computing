#bennetthomas
#29/08/2023
#my name

print("Hello!")
name = str(input("What's your name?"))
print("Hi,", name)
age = int(input("How old are you?"))
if age >= 13 and age <=19:
    print("Wow,", name, "you are a teenager!")
elif age < 13:
    print("You are quite young", name)
else:
    print("You are an adult", name)
answer = int(input("How are you on a scale of 1-10!?"))
if answer >= 5:
    print("Glad to hear that!")
else:
    print("I hope you get better!")
