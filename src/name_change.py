import fileinput
import os

try:
    projection_path = os.path.join(os.path.dirname(
        __file__), '../fd_data/projections.csv')
    with fileinput.FileInput(projection_path, inplace=True) as file:
        for line in file:
            print(line.replace('III', '')
                  .replace('II', '')
                  .replace('IV', '')
                  .replace('Jr.', '')
                  .replace('Sr.', '')
                  .replace('Moe Harkless', 'Maurice Harkless')
                  .replace('PJ Washington', 'P.J. Washington')
                  .replace('Jakarr Sampson', 'JaKarr Sampson')
                  .replace('KJ Martin', 'Kenyon Martin')
                  .replace('Cameron Thomas', 'Cam Thomas')
                  .replace('Nicolas Claxton', 'Nic Claxton')
                  .replace('Marjon Beauchamp', 'MarJon Beauchamp')
                  .replace('DeAndre Ayton', 'Deandre Ayton')
                  .replace('Guillermo Hernangomez', 'Willy Hernangomez')
                  .replace('Michael Porter Jr.', 'Michael Porter')
                  .replace(' \"', '\"'), end='')
except:
    print('FD Projections failed to rename')
    pass

try:
    projection_path = os.path.join(os.path.dirname(
        __file__), '../dk_data/projections.csv')
    with fileinput.FileInput(projection_path, inplace=True) as file:
        for line in file:
            print(line.replace('DeAndre Ayton', 'Deandre Ayton').replace(
                'Aaron NeSmith', 'Aaron Nesmith'), end='')
except:
    print('DK Projections failed to rename')
    pass
