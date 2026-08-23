def main():
    n = int(input())
    
    numbers = list(map(int, input().split()))

    if not numbers:
        return

    largest = numbers[0]
    smallest = numbers[0]
    total_sum = 0
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        
        total_sum += num

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    reversed_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[i])

    # Print results matching the assignment output format
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Sum: {total_sum}")
    print(f"Even count: {even_count}")
    print(f"Odd count: {odd_count}")
    print("Reversed:", " ".join(map(str, reversed_numbers)))


if __name__ == "__main__":
    main()