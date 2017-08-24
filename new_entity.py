# import file_operations.py variables and functions
from modules.file_operations import *

new_entity = input('New entity: ')

# create new entity and append .markdown extension
# ... 'cause it looks prettier dammit!
create_entity(new_entity + '.md')
