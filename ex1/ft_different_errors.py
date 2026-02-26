def garden_operations() -> None:
    try:
        num: int = int("abc")
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")
    
    try:
        res: int = 10 / 0
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")
    
    try:
        f = open("missing.txt", "r")
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    
    try:
        person = {"name": "Alice", "garden": "MyGarden"}
        print(person["plant"]) 
    except KeyError as e:
        print("Testing KeyError...")
        print(f"Caught KeyError: 'missing\\_{e}'\n")
    

def test_error_types() -> None:
    try:
        print("=== Garden Error Types Demo ===\n")
        garden_operations()
        res: int = 10 / 0
        f = open("file.txt", "r")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")
    finally:
        print("All error types tested successfully!")

test_error_types()  