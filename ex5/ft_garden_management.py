class GardenError(Exception):
    def __init__(self, message):
        self.message = message


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"Error checking {self.message} "


class GardenManager:
    tank = 20

    def __init__(self, name):
        self.name = name
        self.garden = Garden(name)

    def add_plant(self, plant):
        if (plant.name == ""):
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        else:
            self.garden.list_plants += [plant]
            print(f"Added {plant.name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.garden.list_plants:
                if (plant):
                    print(f"Watering {plant.name} - success")
                else:
                    raise WaterError("Cannot water None - invalid plant!")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(name, water, sun):
        if (not (water >= 1 and water <= 10)):
            w = water
            raise WaterError(f"{name}: Water level {w} is too high (max 10)\n")
        elif (not (sun >= 2 and sun <= 12)):
            raise GardenError("Caught GardenError: Not enough water in tank\n")
        else:
            print(f"{name}: healthy! (water: {water}, sun: {sun})")

    @staticmethod
    def check_tank():
        if (GardenManager.tank < 100):
            raise GardenError("Caught GardenError: Not enough water in tank")


class Garden:
    def __init__(self, manager):
        self.list_plants = []


class Plant:
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class Main:
    @staticmethod
    def main():
        print("=== Garden Management System ===\n")
        try:
            print("Adding plants to garden...")
            oualid = GardenManager("oualid")
            tomato = Plant("tomato", 5, 8)
            lettuce = Plant("lettuce", 15, 10)
            invalid = Plant("", 5, 11)
            oualid.add_plant(tomato)
            oualid.add_plant(lettuce)
            oualid.add_plant(invalid)
        except PlantError as e:
            print(e)

        try:
            print("\nWatering plants...")
            oualid.water_plants()
        except WaterError as e:
            print(e)

        try:
            print("\nChecking plant health...")
            for plant in oualid.garden.list_plants:
                oualid.check_plant_health(plant.name, plant.water, plant.sun)
        except WaterError as e:
            print(e)

        try:
            print("Testing error recovery...")
            oualid.check_tank()
        except GardenError as e:
            print(e)
        finally:
            print("System recovered and continuing...\n")

        print("Garden management system test complete!")


Main.main()
