class GardenError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Caught garden error: {self.message}"


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"Caught WaterError:: {self.message}"


class Main:
    @staticmethod
    def test_custom_errors():
        print("=== Custom Garden Errors Demo ===\n")
        try:
            print("Testing PlantError...")
            raise PlantError("The tomato plant is wilting!\n")
        except PlantError as e:
            print(e)

        try:
            print("Testing WaterError...")
            raise WaterError("Not enough water in the tank!\n")
        except WaterError as e:
            print(e)

        print("Testing catching all garden errors...")
        try:
            raise GardenError("The tomato plant is wilting!")
        except GardenError as e:
            print(e)

        try:
            raise GardenError("Not enough water in the tank!\n")
        except GardenError as e:
            print(e)
        print("All custom error types work correctly!")


Main.test_custom_errors()
