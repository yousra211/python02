def garden_operations(operation: str) -> None:
    if operation == "value_error":
        num: int = int("abc")

    elif operation == "zero_division":
        res: int = 10 / 0

    elif operation == "file_not_found":
        f = open("missing.txt", "r")

    elif operation == "key_error":
        person = {"name": "Alice", "garden": "MyGarden"}
        print(person["plant"])

    elif operation == "multiple":
        res: int = 10 / 0
        f1 = open("file.txt", "r")


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        garden_operations("value_error")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero_division")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file_not_found")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden_operations("key_error")
    except KeyError as e:
        print(f"Caught KeyError: missing\\_{e}\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


print("=== Garden Error Types Demo ===\n")
test_error_types()