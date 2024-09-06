#name = []
#for repeat in range(3):
    #firstname = input("Enter your first name:")
    #surname = input("Enter your surname:")
    #fullname = firstname + " " + surname
    #name.append(fullname)
#print(name)


name = ['alice adams','ben brown','carol codd']
newname = []
for x in range(len(name)):
  initial = name[x][0].upper()
  surname = name[x].split(' ')[1][0].upper()
  final = "idk" 
  print(initial,surname)
print(newname)

