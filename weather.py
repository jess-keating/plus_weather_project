import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_object = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return date_object.strftime("%A %d %B %Y")  # e.g. Tuesday 06 July 2021


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_fahrenheit = float(temp_in_fahrenheit)
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5 / 9
    temp_in_celsius = round(temp_in_celsius, 1)
    return temp_in_celsius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
        
    Returns:
        A float representing the mean value.
    """
    temperature = [float(number) for number in weather_data]
    
    total = sum(temperature)
    count = len(temperature)
    mean = total / count
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row:
                # Convert numeric columns to int, keep date as string
                converted_row = [row[0], int(row[1]), int(row[2])]
                data.append(converted_row)
    return data
    


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
        #retrun value and index is enumerate? return (min_value, index)? return the min value use "min()" so min(list)?
    """
    if not weather_data:
        return ()

    # Ensure all values are numbers (convert strings to float)
    weather_data = [float(x) for x in weather_data]

    min_value = min(weather_data)
    min_index = None

    for index, value in enumerate(weather_data):
        if value == min_value:
            min_index = index

    return (min_value, min_index)



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()

    # Ensure all values are numbers (convert strings to float)
    weather_data = [float(x) for x in weather_data]

    max_value = max(weather_data)
    max_index = None

    for index, value in enumerate(weather_data):
        if value == max_value:
            max_index = index

    return (max_value, max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_days = len(weather_data)

    # Extract low and high temperatures for calculation
    lows = [convert_f_to_c(day[1]) for day in weather_data]
    highs = [convert_f_to_c(day[2]) for day in weather_data]

    # Find min and max using your helper functions
    min_temp, min_index = find_min(lows)
    max_temp, max_index = find_max(highs)

    min_day = convert_date(weather_data[min_index][0])
    max_day = convert_date(weather_data[max_index][0])

    # Calculate averages
    avg_low = calculate_mean(lows)
    avg_high = calculate_mean(highs)

    # Format final summary string
    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {min_day}.\n"
        f"  The highest temperature will be {format_temperature(max_temp)}, and will occur on {max_day}.\n"
        f"  The average low this week is {format_temperature(round(avg_low, 1))}.\n"
        f"  The average high this week is {format_temperature(round(avg_high, 1))}.\n"
    )

    return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary_lines = []

    for day in weather_data:
        date = convert_date(day[0])
        low_c = convert_f_to_c(day[1])
        high_c = convert_f_to_c(day[2])

        daily_summary = (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {format_temperature(low_c)}\n"
            f"  Maximum Temperature: {format_temperature(high_c)}\n\n"
        )
        summary_lines.append(daily_summary)

    return "".join(summary_lines)
