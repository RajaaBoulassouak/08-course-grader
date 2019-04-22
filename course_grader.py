def course_grader(param):
    sum = 0
    for index in range(len(param)):
        sum = sum + param[index]
    print(sum)

    avg = sum / (len(param) -1)
    print(avg)
    print(avg > 70)
