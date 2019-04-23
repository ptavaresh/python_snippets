def gradingStudents(grades):
    #
    # Write your code here.
    #
    result = []
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i += (5 - i % 5)
        result.append(i)
    return result

arr = [22,3,69,74,85,12,33,82,99]

print(gradingStudents(arr))
