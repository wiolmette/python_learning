# Załóżmy, że masz dwie listy z danymi o studentach. Każdy element z 
# student_grades[i] 
# to lista ocen studenta o indeksie i. 
# Utwórz słownik, w którym kluczami będą imiona studentów, 
# a wartościami będą słowniki z dodatkowymi danymi, np.:
{
  "Adam": {"grades": [5, 5, 4], "average": 4.66},
  "Beata": {"grades": [3, 5, 3], "average": 3.66},
  "Cezary": {"grades": [4, 4, 4], "average": 4.0}
}

student_names = ["Adam", "Beata", "Cezary"]
student_grades = [[5, 5, 4], [3, 5, 3], [4, 4, 4]]

average_grades = []
for i in range(0, len(student_grades)):
    average_grades.insert(i, sum(student_grades[i])/len(student_grades[i]))
print(average_grades)

average_grades_slownik = {"grades": student_grades[0]}
print(average_grades_slownik)

# student_grades_slownik = {}
# student_grades_slownik["grades"] = student_grades
# print(student_grades_slownik)

slownik = {}
slownik2 = {}
slownik3 = {}

for i in range(0, len(student_names)):
    slownik2 = {"grades": student_grades[i]}
    slownik3 = {"average": average_grades[i]}
    slownik[student_names[i]] = slownik2, slownik3
print(slownik)

