def add_one(num):  # not inside class don't need self
    return num + 1


def compare(num1, num2):
    if num1 > num2:
        return "first number greater than"
    elif num1 < num2:
        return "first number less than"
    elif num1 == num2:
        return "first number equal to"
