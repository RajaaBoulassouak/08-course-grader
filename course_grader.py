def course_grader(param):
    sum = 0
    for index in range(len(param)):
        if param[index] < 50:
            return "fail"
        sum = sum + param[index]
    
    avg = sum / (len(param) -1)
    if avg < 70:
        return "fail"
    else:
        return "pass"
