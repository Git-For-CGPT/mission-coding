Student_name = input("Enter your name: ")
maths_score = float(input("Enter your Maths score: "))
science_score = float(input("Enter your Science score: "))
english_score = float(input("Enter your English score: "))
total_score = maths_score + science_score + english_score
average_score = total_score / 3
if average_score >= 90:
    grade = "A+"
elif average_score >= 80:
    grade = "A"
elif average_score >= 70:
    grade = "B"
elif average_score >= 60:
    grade = "C"
elif average_score >= 50:
    grade = "D"
else:
    grade = "F"
status = "Fail" if any(score < 50 for score in [maths_score, science_score, english_score]) else ("Pass" if average_score >= 50 else "Fail")

print("Hello,", Student_name)
print("Your total score is:", total_score)
print("Your average score is:", f"{average_score:.2f}")
print("Your grade is:", grade)
print("Your status is:", status)
