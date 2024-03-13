function find_middle_number(numbers):
    # numbers: A list of distinct numbers where n > 2.
    if len(numbers) <= 2:  # Check if the list length is at least 3.
        print(ValueError("Not enough numbers for performing the operation"))
        exit()

    first_number = numbers[0]
    second_number = numbers[1]
    third_number = numbers[2]

    if first_number < second_number:  # Check if the first number is less than the second number.
        if first_number > third_number:  # Check if the first number is greater than the third number.
            return first_number
        else:
            return third_number  # Adjusted to return third_number if it's not smaller than both.
    else:
        if second_number > third_number:  # Check if the second number is greater than the third number.
            return second_number
        else:
            return third_number  # This ensures it returns the third number if it's not the smallest.
