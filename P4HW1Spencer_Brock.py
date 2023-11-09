#CTI-110
#P4HW1-Score List
#spencer Brock
#11/9/2023



NumScores = int(input("enter numbers of grades: "))
scores = []

for i in range(NumScores):
    grade = int(input(f"Enter score  #{i + 1}:"))
    while grade < 0:
        print("Invalid Score!!")
        print("Score should be between 0 and 100")
        grade = int(input(f"Enter score {i + 1}: "))
    scores.append(grade)

ave = sum(scores)/len(scores)
if  ave > 90:
    letter = 'A';
elif ave > 80:
    letter ="B"
elif ave > 70:
    letter = "C"
elif ave > 60:
    letter = "D"
elif ave > 50:
    letter = "F"
    
print(f"Grade: {letter}")
print(f"Scores Average: {ave}")
print(f"Modified List: {scores}")
print(f"Lowest Score: {lowest(score)}")
