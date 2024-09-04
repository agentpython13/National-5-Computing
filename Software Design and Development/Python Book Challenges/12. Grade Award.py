#bennetthomas
#050923
#Grade Award

print("Validated Grade Award")
print()


name = input("Enter Pupil's name: ")
mark = int(input("Enter Pupil's mark: "))

while mark > 100 or mark < 0:
    print("Invaild Mark")
    mark = int(input("Enter Pupil's mark: "))

if mark >= 70:
    grade = "A"
if mark >= 60 and mark < 70:
    grade = "B"
if mark >= 50 and mark < 60:
    grade = "C"
if mark >= 40 and mark < 50:
    grade = "D"
else:
    grade = "F"

print(name, "with a mark of", mark, "out of 100 has achevied a grade of", grade)
