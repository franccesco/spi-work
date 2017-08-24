"""Functions regarding file and directory operations."""
# Do not call this script inside this directory.

import os
import time
from shutil import copyfile

# Define file estructure with date format
path_structure = 'entities/' + time.strftime('%Y/%m/%d')

def check_dir_exist():
    if os.path.isdir(path_structure):
        return True
    else:
        return False

def create_dir():
    if check_dir_exist():
        pass
    else:
        print("Directory '" + path_structure + "' does not exist. Creating...")
        os.makedirs(path_structure)

def create_entity(new_entity):
    """check if file exist. if not, then proceed to create."""

    entity_template = 'template.md'
    # Ask for new entity
    new_entity_estructure = path_structure + '/' + new_entity + '.md'

    # checks if file exist, if false: create new entity.
    if os.path.isfile(new_entity_estructure):
        print('Entity already exist.')
    else:
        # copy template file to new entity
        create_dir()
        copyfile(entity_template, new_entity_estructure)
        print('File ' + new_entity + ' created.')
