"""Functions regarding file and directory operations."""
# Do not call this script inside this directory.

import os
import time
from shutil import copyfile

# Define file estructure with date format
path_structure = 'entities/' + time.strftime('%Y/%m/%d')


def check_dir_exist():
    """Check if directory exists."""
    if os.path.isdir(path_structure):
        return True
    else:
        return False


def check_draft_exist(draft_location):
    """Check if draft exists."""
    if os.path.isfile(draft_location):
        return True
    else:
        return False


def create_dir():
    """Create directory if it's not created."""
    if check_dir_exist():
        return False
    else:
        os.makedirs(path_structure)
        return True


def create_entity(new_entity='draft_entity',
                  entity_AM=False,
                  entity_PEP=False):
    """Check if file exist. if not, then proceed to create."""
    empty_template = 'templates/empty_template.md'
    am_template = 'templates/am_template.md'
    am_pep_template = 'templates/am_pep_template.md'
    pep_template = 'templates/pep_template.md'
    # Ask for new entity
    new_entity_estructure = path_structure + '/' + new_entity + '.md'

    if entity_AM is False and entity_PEP is False:
        # copy empty skeleton
        create_dir()
        copyfile(empty_template, new_entity_estructure)
        return True

    elif entity_AM is True and entity_PEP is False:
        # copy adverse media only template
        create_dir()
        copyfile(am_template, new_entity_estructure)
        return True

    elif entity_AM is True and entity_PEP is True:
        # copy entity_PEP template with adverse media
        create_dir()
        copyfile(am_pep_template, new_entity_estructure)
        return True

    elif entity_AM is False and entity_PEP is True:
        # copy entity_PEP template with no adverse media
        create_dir()
        copyfile(pep_template, new_entity_estructure)
        return True

    else:
        return False
