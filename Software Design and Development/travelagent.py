travel_agent = []
booking_number = []
dates = []

for index in range(3):
    t_agent = input("Enter travel agent: ")
    b_number = int(input("Enter booking_number: "))
    d = input("Enter date: ")
    travel_agent.append(t_agent)
    booking_number.append(b_number)
    dates.append(d)

print(travel_agent)
print(booking_number)
print(dates)