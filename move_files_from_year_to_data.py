'''
Copy files from year folders to single folder `data`, with sensible
lexicographical name convention.
'''


import os
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
            else:
                new_filename = f'PPMS_update_{year}_{month}_{day}_ew.zip'
                os.system(f'copy .\\{year}\\{filename} .\\data\\{new_filename}')


if __name__ == '__main__':
    main()
    
    