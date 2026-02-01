from student import Student
from schoolClass import SchoolClass

dp = SchoolClass("FDP")

s1 = Student("Ali", 60,70,55)
s2 = Student("Maria", 55,65,80)
s3 = Student("Rayen", 70,55,58)

dp.add_student(s1)
dp.add_student(s2)
dp.add_student(s3)

print(round(s1.get_average_score(),2))
print(round(dp.get_class_average_grade()),2)

