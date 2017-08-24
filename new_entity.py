# import file_operations.py variables and functions
from modules.file_operations import *

active = True
print("Press 'q' to quit.")

while active:
    new_entity = input('Entity: ')
    if new_entity == 'q':
        print('Exiting...')
        break
    else:
        # create new entity and append .markdown extension
        # ... 'cause it looks prettier dammit!
        create_entity(new_entity + '.md')
