def linear_search(data, target, key):
    for item in data:
        if item[key] == target:
            return item
    return None


def binary_search(data, target, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        if data[middle][key] == target:
            return data[middle]
        if data[middle][key] < target:
            low = middle + 1
        else:
            high = middle - 1
    return None


def jump_search(data, target, key):
    step = max(1, int(len(data) ** 0.5))
    start = 0

    while start < len(data):
        end = min(start + step, len(data))
        if data[end - 1][key] >= target:
            for item in data[start:end]:
                if item[key] == target:
                    return item
            return None
        start += step
    return None
