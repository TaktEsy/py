# 2023/09/26 00:00|Дополнительное практическое задание по модулю*

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron', })  # Упорядочить по алфавиту, и на выходе присваиваю список, а не множество

average_grades = dict(zip(students, grades))    # Склеиваем два списка в словарь

print(grades)
print(students)

for i in grades:
    print(sum(i)/len(i))


for j in average_grades.values():
    print(sum(j)/len(j))

