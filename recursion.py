def recurrsion(num):
    print(num)
    if num % 2 != 0:
        print("Please enter even number")
    elif num == 2:
        return num
    else:
        return recurrsion(num-2)

recurrsion(8)