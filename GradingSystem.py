def gradingStudents(grades):
    new_arr = []
    el = 0
    for i in grades:
        if ((((i // 5) * 5) + 5) - i) < 3 and i >= 38:
            el = (((i // 5) * 5) + 5)
        elif ((((i // 5) * 5) + 5) - i) >= 3 and i >= 38:
            el = i
        elif i < 38:
            el = i

        new_arr.append(el)
    return new_arr