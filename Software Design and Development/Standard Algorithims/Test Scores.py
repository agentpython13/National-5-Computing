total = 0
for score in range(5):
    t_score  =int(input(f"How much did you get in test {score+1}? "))
    total += t_score
    print(f"You have scored {total} points in total!")