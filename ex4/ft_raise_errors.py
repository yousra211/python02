class Plant:
    def __init__(
            self, name: str, water_level: int, sunlight_hours: int
            ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!\n")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}\
                        is too high (max 10)\n")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}\
                        is too low (min 1)\n")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}\
                        is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}\
                        is too high (max 12)\n")
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    p1: Plant = Plant("tomato", 2, 4)
    p2: Plant = Plant(None, 4, 6)
    p3: Plant = Plant("carrots", 15, 4)
    p4: Plant = Plant("potatoes", 8, 0)

    try:
        print("Testing good values...")
        check_plant_health(p1.name, p1.water_level, p1.sunlight_hours)
        print("Testing empty plant name...")
        check_plant_health(p2.name, p2.water_level, p2.sunlight_hours)
    except ValueError as e:
        print(e)

    try:
        print("Testing bad water level...")
        check_plant_health(p3.name, p3.water_level, p3.sunlight_hours)
    except ValueError as e:
        print(e)

    try:
        print("Testing bad sunlight hours...")
        check_plant_health(p4.name, p4.water_level, p4.sunlight_hours)
    except ValueError as e:
        print(e)
    finally:
        print("All error raising tests completed!")


print("=== Garden Plant Health Checker ===\n")
test_plant_checks()
