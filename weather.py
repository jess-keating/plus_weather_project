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
    pass


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
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
