students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 66
}

def calculate_average(data):

    total = 0

    for score in data.values():
        total += score

    avg = total / len(data)

    return avg


def find_top_student(data):

    top_name = ""
    top_score = 0

    for name, score in data.items():

        if score > top_score:
            top_score = score
            top_name = name

    return top_name, top_score


average = calculate_average(students)

print("Average score:", average)

name, score = find_top_student(students)

print("Top student:", name)
print("Score:", score)