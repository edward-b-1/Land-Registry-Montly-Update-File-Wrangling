'''
Extract all zip files from folder `data` into `data_unzip`.
'''


import os
from zipfile import ZipFile
from lib import is_leapyear
from lib import month_to_day_leapyear
from lib import month_to_day
from lib import month_integer_to_string


def main():
    for year in range(2015, 2024+1):
        print(f'year={year}')
        
        for month in range(1, 12+1):
            if is_leapyear(year):
                day = month_to_day_leapyear[month]
            else:
                day = month_to_day[month]
            filename = f'PPMS_update_{year}_{month}_{day}_ew.zip'
            if not os.path.exists(f'.\\data\\{filename}'):
                print(f'file {filename} does not exist')
            else:
                with ZipFile(f'.\\data\\{filename}') as zip:
                    month_as_string = month_integer_to_string[month]
                    zip_internal_filename = f'PPMS_update_{day}_{month_as_string}_{year}_ew.txt'
                    print(f'{zip_internal_filename}')
                    zip.extract(
                        member=zip_internal_filename,
                        path=f'.\\data_unzip',
                    )


if __name__ == '__main__':
    main()
    
    