'''
Combine all files from folder `data` into a single file.

Add new column for original file date.
'''


import os
import pandas
from datetime import datetime
from lib import is_leapyear
from lib import month_to_day_leapyear
from lib import month_to_day


def main():
    df_list = []
    
    for year in range(2015, 2024+1):
        print(f'year={year}')
        
        for month in range(1, 12+1):
            if is_leapyear(year):
                day = month_to_day_leapyear[month]
            else:
                day = month_to_day[month]
            filename = f'PPMS_update_{year}_{month}_{day}_ew.txt'
            if not os.path.exists(f'.\\data_unzip_lex\\{filename}'):
                print(f'file {filename} does not exist')
            else:
                print(f'reading data from file: {filename}')
                df = pandas.read_csv(f'.\\data_unzip_lex\\{filename}', header=None)
                print(df)
                file_date = datetime(
                    year=year,
                    month=month,
                    day=day,
                )
                df['X'] = file_date
                df_list.append(df)
    
    df = pandas.concat(df_list)
    print(df.columns)
    df.to_csv('PPMS_update.csv', index=False)
    

if __name__ == '__main__':
    main()
    
    