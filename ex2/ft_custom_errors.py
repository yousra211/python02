class GardenError(Exception):
    pass

class PlantError(GardenError):
    def __init__(self, name: str):
        super().__init__(f"The {name} plant is wilting!")

class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


class Plant:
    def __init__(self, name: str, wilt: str, water_in_trank: int) -> None:
        self.name = name
        self.wilt = wilt
        self.water_in_trank = water_in_trank
        

def wilting(wilt: bool, name: str) -> int:
    if wilt == True:
        raise PlantError(name)
    else:
        return 0

def enough_water(water_in_trank: int) -> int:
    if water_in_trank < 50:
        raise WaterError
    else:
        return 0

def test_custom_errors() -> None:
    plant = Plant("tomato", True, 40)
    print("=== Custom Garden Errors Demo ===")
    try:
        n1 = wilting(plant.wilt, plant.name)
    except PlantError as e:
        print("\nTesting PlantError...")
        print("Caught PlantError:", e)
    else:
        print(f"The {plant.name} plant is blooming!")

    try:
        n2 = enough_water(plant.water_in_trank)
    except WaterError as e:
        print("\nTesting WaterError...")
        print("Caught WaterError:", e)
    else:
        print("The water in the tank is enough")

    try:
        n1 = wilting(plant.wilt, plant.name)
    except GardenError as e:
        print("\nTesting catching all garden errors...")
        print("Caught a garden error:", e)

    try:
        n2 = enough_water(plant.water_in_trank)
    except GardenError as e:
        print("Caught a garden error:", e)
        print("\nAll custom error types work correctly!")
        
test_custom_errors()