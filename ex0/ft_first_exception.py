def check_temperature(temp_str):
    try:
        v = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number\n")
    if (v >= 0 and v <= 40):
        return v
    elif (v > 40):
        raise ValueError(f"Error: {v}°C is too hot for plants (max 40°C)\n")
    else:
        raise ValueError(f"Error: {v}°C is too cold for plants (min 0°C)\n")


def test_temperature_input():
    list_values = ['25', 'abc', '100', '-50']
    print("=== Garden Temperature Checker ===\n")
    for value in list_values:
        try:
            print(f"Testing temperature: {value}")
            print(f"Temperature {check_temperature(value)}", end="")
            print("°C is perfect for plants!\n")
        except ValueError as e:
            print(e)

    print("All tests completed - program didn't crash!")


test_temperature_input()
