if __name__ == '__main__':
    student_results = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        student_results.append([name, score])

    second_lowest = sorted(set([result[1] for result in student_results]))[1]

    second_lowest_students = [result[0] for result in student_results if result[1] == second_lowest]
    second_lowest_students_names = sorted(second_lowest_students)
    for i in range(len(second_lowest_students_names)):
        print(second_lowest_students_names[i])
