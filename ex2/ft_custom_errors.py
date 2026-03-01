class GardenError(Exception):
    """
    Base exception class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Raised when a plant is wilting.
    """
    def __init__(self, name: str) -> None:
        super().__init__(f"The {name} plant is wilting!")


class WaterError(GardenError):
    """
    Raised when there is not enough water in the tank.
    """
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


class Plant:
    """
    Represent a plant with its name, wilting status,
    and available water level.
    """
    def __init__(self, name: str, wilt: bool, water_in_trank: int) -> None:
        self.name = name
        self.wilt = wilt
        self.water_in_trank = water_in_trank


def wilting(wilt: bool, name: str) -> int:
    """
    Check if a plant is wilting.
    """
    if wilt is True:
        raise PlantError(name)
    else:
        return 0


def enough_water(water_in_trank: int) -> int:
    """
    Check if there is enough water in the tank.
    """
    if water_in_trank < 50:
        raise WaterError
    else:
        return 0


def test_custom_errors() -> None:
    """
    Raise and catch custom garden exceptions.
    """
    plant: Plant = Plant("tomato", True, 40)
    print("=== Custom Garden Errors Demo ===")
    try:
        wilting(plant.wilt, plant.name)
    except PlantError as e:
        print("\nTesting PlantError...")
        print("Caught PlantError:", e)
    else:
        print(f"The {plant.name} plant is blooming!")

    try:
        enough_water(plant.water_in_trank)
    except WaterError as e:
        print("\nTesting WaterError...")
        print("Caught WaterError:", e)
    else:
        print("The water in the tank is enough")

    try:
        wilting(plant.wilt, plant.name)
    except GardenError as e:
        print("\nTesting catching all garden errors...")
        print("Caught a garden error:", e)

    try:
        enough_water(plant.water_in_trank)
    except GardenError as e:
        print("Caught a garden error:", e)
        print("\nAll custom error types work correctly!")


test_custom_errors()
