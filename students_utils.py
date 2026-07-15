def calculate_average(*marks):
    return sum(marks) / len(marks)

def get_grade(avg, pass_mark=40):

    if avg < pass_mark:
        return "Fail"
    elif avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"