no = int(input("How many pupils are there?"))
print()
for pupil in range(no):
    array = []
    exams = int(input(f"How many exams did pupil {pupil+1} sit?"))
    for exam in range(exams):
        score = int(input(f"What did the pupil get for exam {exam+1}?"))
        array.append(score)
    print(f"pupil {pupil+1}'s average score is {sum(array)/exams}")
    print()
