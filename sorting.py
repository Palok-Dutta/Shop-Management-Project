def bubble_sort(data, key):
    result = data.copy()

    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if result[j][key] > result[j + 1][key]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(data, key):
    result = data.copy()

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j][key] < result[smallest][key]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result
