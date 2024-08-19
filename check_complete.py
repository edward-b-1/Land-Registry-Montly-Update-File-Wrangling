'''
Check that each year contains the full set of expected files. (12 in total,
1 for each month.)
'''


from lib import check_output_file_exists
from lib import is_leapyear
from lib import month_to_day_leapyear
from lib import month_to_day


def main():
    for year in range(2015, 2024 + 1):
        print(f'year={year}')

        for month in range(1, 12 + 1):
            if is_leapyear(year):
                day = month_to_day_leapyear[month]
            else:
                day = month_to_day[month]
            filename = f'PPMS_update_{year}_{month}_{day}_ew.zip'
            if not check_output_file_exists(f'{year}\\{filename}'):
                print(f'file {filename} does not exist')


if __name__ == '__main__':
    main()
