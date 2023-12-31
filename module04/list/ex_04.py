numbers = ["123", "456", "321", "10", "75", "abc", "23c"]


def sanitize(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(el)
    return result


def transform_to_numbers(data):
    result = []
    for el in data:
        result.append(int(el))
    return result


san_nums = sanitize(numbers)
print(sorted(san_nums))
san_nums = transform_to_numbers(san_nums)
san_nums.sort()
print(san_nums)
print(max(san_nums) - min(san_nums))
print(sum(san_nums) / len(san_nums))
