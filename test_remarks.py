import unittest
import random
import os
from modules.file_operations import *

class EntityTestCase(unittest.TestCase):
    """Test new_entity function."""

    def setUp(self):
        """Create a random number to emulate an entity."""
        self.random_number = str(random.randint(100000, 999999)) + '.md'
        self.new_file_dir = path_structure + '/' + self.random_number

    def test_file_creation(self):
        """Test random id file and empty file."""
        self.new_file = create_entity(self.random_number)
        self.assertFalse(os.path.isdir(self.new_file_dir))

unittest.main()
