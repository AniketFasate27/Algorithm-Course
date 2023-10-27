function find_middle_number(numbers):
  """Finds a number that is neither the minimum nor the maximum of a list of numbers.

  Args:
    numbers: A list of distinct numbers.

  Returns:
    A number that is neither the minimum nor the maximum of `numbers`.
  """

  if len(numbers) <= 2:
    raise ValueError("The list must contain at least 3 distinct numbers.")

  first_number = numbers[0]
  second_number = numbers[1]
  third_number = numbers[2]

  if first_number < second_number:
    if first_number < third_number:
      return first_number
    else:
      return second_number
  else:
    if first_number > third_number:
      return second_number
    else:
      return third_number

# Example usage:

numbers = [10, 5, 2, 1, 3]
middle_number = find_middle_number(numbers)

print(middle_number)
