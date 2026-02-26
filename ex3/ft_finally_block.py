class Plant:
    def __init__(self, name: str) -> None:
        self.name = name

    def watering(self) -> None:
        print(f"Watering {self.name}")


def water_plants(plant_list: list[Plant]) -> None:
    print("Opening watering system")
    try:
        for p in plant_list:
            p.watering()
    except AttributeError:
        raise AttributeError("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list1: list[Plant] = [
        Plant("tomato"),
        Plant("lettuce"),
        Plant("carrots")
    ]

    plant_list2: list[Plant] = [
        Plant("tomato"),
        Plant("")
    ]
    try:
        print("Testing normal watering...")
        water_plants(plant_list1)
        print("Watering completed successfully!\n")

        print("Testing with error...")
        water_plants(plant_list2)
    except AttributeError as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")

test_watering_system()