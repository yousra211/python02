class GardenError(Exception):
    pass


class WaterError(GardenError):
    def __init__(self, name, water):
        if water > 10:
            msg = f"Error checking {name}: Water level {water}\
                is too high (max 10)"
        else:
            msg = f"Error checking {name}: Water level {water}\
                is too low (min 1)"
        super().__init__(msg)


class SunError(GardenError):
    def __init__(self, name, sun):
        if sun > 12:
            msg = f"Error checking {name}: Sunlight hours {sun}\
                is too high (max 12)\n"
        else:
            msg = f"Error checking {name}: Sunlight hours {sun}\
                is too low (min 2)\n"
        super().__init__(msg)


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name: str = name
        self.water: int = water
        self.sun: int = sun


class GardenManager:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        if not plant.name:
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        else:
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")

    def watering(self, plants: list[Plant]) -> None:
        print("Opening watering system")
        try:
            for p in plants:
                print(f"Watering {p.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        if plant.water > 10:
            raise WaterError(plant.name, plant.water)
        elif plant.water < 1:
            raise WaterError(plant.name, plant.water)
        elif plant.sun < 2:
            raise SunError(plant.name, plant.sun)
        elif plant.sun > 12:
            raise SunError(plant.name, plant.sun)
        else:
            print(f"{plant.name}: healthy (water: {plant.water},\
                  sun: {plant.sun})")


def enough_water(water_in_trank: int) -> int:
    if water_in_trank < 50:
        raise GardenError("Caught GardenError: Not enough water in tank")
    else:
        return 0


def test_garden_management() -> None:
    g = GardenManager("alice")

    plant_data: list[tuple[str, int, int]] = [
        ("tomato", 5, 8),
        ("lettuce", 15, 4),
        (None, 12, 3)
    ]

    plants: list[Plant] = [
        Plant(name, water, sun)
        for name, water, sun in plant_data
    ]

    print("=== Garden Management System ===\n")

    try:
        print("Adding plants to garden...")
        for p in plants:
            g.add_plant(p)

    except ValueError as e:
        print(e)

    try:
        print("\nWatering plants...")
        g.watering(g.plants)
        print("\nChecking plant health...")
        for p in g.plants:
            g.check_plant_health(p)
    except GardenError as e:
        print(e)

    try:
        print("\nTesting error recovery...")
        enough_water(plants[0].water)
    except GardenError as e:
        print(e)
    finally:
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")


test_garden_management()
