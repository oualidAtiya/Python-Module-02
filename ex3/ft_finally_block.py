class WaterError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Error : {self.message}"


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if (plant):
                print(f"Watering {plant}")
            else:
                raise WaterError("Cannot water None - invalid plant!")
    except WaterError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    plant_list = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering..")
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    plant_list = ["tomato", None, "carrots"]
    print("Testing with error...")
    water_plants(plant_list)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
