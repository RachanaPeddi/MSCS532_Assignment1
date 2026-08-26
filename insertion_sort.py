def insertion_sort_decreasing(values):
    for i in range(1, len(values)):
        current_value = values[i]
        position = i - 1

        while position >= 0 and values[position] < current_value:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = current_value

    return values


if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")

    numbers = [int(value) for value in user_input.split()]

    print("Original Array:", numbers)

    insertion_sort_decreasing(numbers)

    print("Sorted Array (Decreasing Order):", numbers)