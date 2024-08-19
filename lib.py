
import os


month_to_day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

month_to_day_leapyear = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


month_string_to_integer = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12,
}


month_integer_to_string = {
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    5: 'may',
    6: 'jun',
    7: 'jul',
    8: 'aug',
    9: 'sep',
    10: 'oct',
    11: 'nov',
    12: 'dec',
}


def is_leapyear(year: int) -> bool:
    return year % 4 == 0


def get_year(filename):
    components = filename.split('_')
    return int(components[4])


def rename_filename(filename):
    components = filename.split('_')
    month = components[3]
    month_numerical = month_string_to_integer[month]
    reordered_components = [
        components[0],
        components[1],
        components[4],
        str(month_numerical),
        components[2],
        components[5],
    ]
    return '_'.join(reordered_components)


def copy_file_from_input_dir_to_year_dir(
    input_dir_filename,
    year,
    new_filename,
):
    os.system(f'copy .\\input\\{input_dir_filename} {new_filename}')


def check_output_file_exists(file_path):
    return os.path.exists(file_path)

