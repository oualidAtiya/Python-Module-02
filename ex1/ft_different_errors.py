def garden_operations():
    try:
        print("Testing ValueError...")
        int('abc')
    except (ValueError):
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        int(10 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("file.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'file.txt'\n")

    try:
        print("Testing KeyError...")
        dic = {"fname": "oualid"}
        print(dic["lname"])
    except KeyError:
        print("Caught KeyError: 'lname'\n")

    try:
        print("Testing multiple errors together...")
        int('abc')
        int(10 / 0)
        open("file.txt")
        dic = {"fname": "oualid"}
        print(dic["lname"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()
