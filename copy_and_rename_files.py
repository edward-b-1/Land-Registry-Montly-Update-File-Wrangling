'''
All the files are initially dumped into the directory `input`. This script
moves (copies) the files from `input` to their correct year name directory.
'''

import os


from lib import rename_filename
from lib import get_year
from lib import check_output_file_exists
from lib import copy_file_from_input_dir_to_year_dir


def main():
    input_path = 'input'

    for filename in os.listdir(input_path):
        #print(filename)
        new_filename = rename_filename(filename)
        #print(new_filename)
        year = str(get_year(filename))
        if not check_output_file_exists(f'{year}\\{new_filename}'):
            print(f'{year}\\{new_filename}')
            new_filename = rename_filename(filename)
            copy_file_from_input_dir_to_year_dir(
                input_dir_filename=filename,
                year=year,
                new_filename=new_filename,
            )


if __name__ == '__main__':
    main()
