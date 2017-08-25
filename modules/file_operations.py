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

def create_entity(new_entity = 'draft_entity', AM = False, PEP = False, overwrite = False):
    """check if file exist. if not, then proceed to create."""

    empty_template = 'templates/empty_template.md'
    am_template = 'templates/am_template.md'
    am_pep_template = 'templates/am_pep_template.md'

    # Ask for new entity
    new_entity_estructure = path_structure + '/' + new_entity + '.md'

    # checks if file exist, if false: create new entity.
    if os.path.isfile(new_entity_estructure):
        return False

    elif AM == False and PEP == False:
        # copy empty skeleton
        create_dir()
        copyfile(empty_template, new_entity_estructure)
        return True

    elif AM == True and PEP == False:
        # copy adverse media only template
        create_dir()
        copyfile(am_template, new_entity_estructure)
        return True

    elif AM == True and PEP == True:
        # copy PEP template with adverse media
        create_dir
        copyfile(am_pep_template, new_entity_estructure)
        return True

    else:
        return False
