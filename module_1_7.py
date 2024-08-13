# 2023/09/26 00:00|Дополнительное практическое задание по модулю*

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron', })  # Упорядочить по алфавиту, и на выходе присваиваю список, а не множество
#average_grades = dict(zip(students, grades))    # Склеиваем два списка в словарь
ave_grades = []

for a in grades:
    ave_grades.append(sum(a)/len(a))


print('Средние оценки: ', ave_grades)
print('Студенты: ', students)
result = dict(zip(students, ave_grades))
print(result)



