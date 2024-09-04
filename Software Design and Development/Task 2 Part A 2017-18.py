#Task 2 2017-18

#create list of readings to display at the end
readings= []
#create empty signal pattern string to be added to
signalp = ""

#create loop to loop through all 5 readings
for x in range(5):
    #ask user for reading
    reading = float(input("Enter reading: "))
    #round reading to 0 decimal places
    reading = int(round(reading, 0))
    #add appropriate letter to signal pattern
    if reading > 80:
        signalp += "S"
    elif reading <= 80 and reading >= 30:
        signalp += "M"
    else:
        signalp += "P"
    #add reading to list of readings
    readings.append(reading)
#display signal pattern
print(signalp)
#loop through reading and display each one with their reading number
for x in readings:
    num = 1
    print(f"Reading {num} - {x}")
    num += 1
    

