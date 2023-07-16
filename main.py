marks = []
name = input("Enter name:")
marks.append(name)
scoreMath = float(input("mark:"))
marks.append(scoreMath)
scoreHistory = float(input("mark:"))
marks.append(scoreHistory)
scoreIT = float(input("mark:"))
marks.append(scoreIT)
ave = (marks[1] + marks[2] + marks[3]) / 3
print(ave)
