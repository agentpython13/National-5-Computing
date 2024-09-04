#bennetthomas
#05/10/23

import random

#create list of endings
endings = ['ing', 'end', 'axe', 'gex', 'goh']
#ask user how many usernames are to be generated
num = int(input("How many students are usernames to be generated for?"))

#set loop to generate required number of usernames
for x in range(num):
    partial = ""
    #ask user to input partial student name (again if inputted wrong first time)
    while len(partial) != 3:
        partial = input("What are the first three letters of the student's name?")
        #display error message if partial student name is not 3 letters long
        if len(partial) != 3:
             print("The partial name you have inputted is invalid! Try Again!")
    #generate random number
    rannum = random.randint(1,5)
    #generate random ending according to random number and concatenate with partial student name and create username
    username = partial + endings[rannum-1]
    #display username
    print(username)


        
            
            
        
        
