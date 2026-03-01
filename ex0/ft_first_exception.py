def check_temperature(temp_str: str) -> int:
    try:
        num: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number\n")

    if num < 0:
        raise ValueError(f"Error: {num}°C is too cold for plants (min 0°C)\n")
    elif num > 40:
        raise ValueError(f"Error: {num}°C is too hot for plants (max 40°C)\n")
    else:
        return num


def test_temperature_input() -> None:
    temp: tuple[int, str, int, int] = (25, "abc", 100, -50)
    for t in temp:
        print(f"Testing temperature: {t}")
        try:
            num: int = check_temperature(t)
        except ValueError as e:
            print(e)
        else:
            print(f"Temperature {num}°C is perfect for plants!\n")


print("=== Garden Temperature Checker ===\n")
test_temperature_input()
print("All tests completed - program didn't crash!")
