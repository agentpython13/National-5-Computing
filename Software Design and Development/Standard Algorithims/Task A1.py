scores = []
test_score = int(input())
while test_score < 0 or test_score > 100:
    print("Error, try again!")
    test_score = int(input())
scores.append(test_score)

    