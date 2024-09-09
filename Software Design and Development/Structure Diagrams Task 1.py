#Task 1: Example One - Program Party Cost

#child_buffet = 2.00
#dietary_requirements = []

#cake_question = input("Is cake required? ")
#if cake_question == 'yes' or cake_question == 'Yes':
    #cake = 15.00
#else:
    #cake = 0
    
#adults = int(input('How many adults are attending? '))
#children = int(input('How many children are attending? '))

#for child in range(children):
    #dietary = input(f"What is child {child+1}'s dietary requirements? ")
    #dietary_requirements.append(dietary)

#if adults + children > 20:
    #venue = 0
#else:
    #venue = 50

#cost = (child_buffet * children) + cake + venue

#Task 1: Example Two - The Journey

#numOfstations = int(input("How many charging stations will you visit on your journey? "))
#startMiles = int(input("What is your current mileage? "))

#for repeat in range(numOfstations):
    #currentMiles = int(input(f"What is your current mileage? (mileage at station {repeat+1}) "))
    #kW_rating = int(input(f"What is the kW rating of the station you are at right now? (kW rating of station {repeat+1}) "))
    
    #if kW_rating == 7:
        #pricePerMile = 0
    #elif kW_rating == 22:
        #pricePerMike = 0.005
    #else:
        #pricePerMile = 0.01
        
    #milesTravelled = currentMiles - startMiles
    #startMiles = currentMiles

    #stage_cost = milesTravelled * pricePerMile