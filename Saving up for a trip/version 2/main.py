Year_coin = [12, 10, 7, 5] #Стоимость познего завтрака

for dataset in range(10): #За 10 лет собранно денег
    trip_coin = int(input()) #Денег для поездки
    proportions = int(input())
    num_students = int(input())

    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])
    students_per_year = [] # Список студентов

    for proportion in proportions:
        students = int(num_students * proportion)
        students_per_year.append(students)
        total_raised = 0

        for i in range(len(students_per_year)):
            total_raised = total_raised + students_per_year[i] * Year_coin[i]
        if total_raised / 2 < trip_coin:
            print('Yes')
        else:
            print("No")
