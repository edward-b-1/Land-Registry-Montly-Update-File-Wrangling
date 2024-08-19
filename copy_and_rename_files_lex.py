'''
Copy files from `data_unzip` to `data_unzip_lex` renaming files to
lexicographical.
'''


import os
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
            month_as_string = month_integer_to_string[month]
            filename = f'PPMS_update_{day}_{month_as_string}_{year}_ew.txt'
            if not os.path.exists(f'.\\data_unzip\\{filename}'):
                #print(f'file {filename} does not exist')
                print(f'.\\data_unzip\\{filename} does not exist')
            else:
                new_filename = f'PPMS_update_{year}_{month}_{day}_ew.txt'
                os.system(f'copy .\\data_unzip\\{filename} .\\data_unzip_lex\\{new_filename}')


if __name__ == '__main__':
    main()
    
    