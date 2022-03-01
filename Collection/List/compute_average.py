def compute_average(list):
    # additon = sum(list)
    addition = 0
    count = 0
    # length = len(list)
    for i in range(len(list)):
        addition = list[i] + addition
        count += 1
    average = addition / count
    return average


list = [1, -2, 4, -4, 9, -6, 16, -8, 25, -10]
compute_average(list)