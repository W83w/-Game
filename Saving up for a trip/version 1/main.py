YEAR_COSTS = [9, 15, 2, 8]
for dataset in range(10):
    school_trip_cost = int(input())## Тараты студентов на обеды
    proportion = input().split()
    num_students = int(input())

    for i in range(len(proportion)):
        proportion[i] = float(proportion[i])
    students_year = []

    for proportion in proportion:
        students = int(num_students * proportion)
        students_year.append(students)
    total_raised = 0
    for i in range(len(students_year)):
        total_raised = total_raised + students_year[i] * YEAR_COSTS[i]

        if total_raised / 2 < school_trip_cost:
                print('yeas')
        else:
                print("No")


