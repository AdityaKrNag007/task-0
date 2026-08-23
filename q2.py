def process_list(numbers):

    modified_list = numbers.copy()

    for num in modified_list[:]:
        if num < 0:
            modified_list.remove(num)

    modified_list.append(0)

    modified_list.sort()

    return modified_list


if __name__ == "__main__":
    original = [5, -2, 8, -1, 3]
    result = process_list(original)

    print("Original:", original)
    print("Result:", result)