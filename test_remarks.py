import unittest
import modules
import os
import time
import random

class EntityTestCase(unittest.TestCase):
    """Test new_entity function."""

    def setUp(self):
        self.new_entity_id = str(random.randint(100000, 999999))
        self.path = 'entities/' + time.strftime('%Y/%m/%d')
        self.id_full_path = self.path + '/' + self.new_entity_id + '.md'

    def test_file_creation(self):
        """Test random id file and empty file."""
        modules.io.create_entity(self.new_entity_id)
        # check if file exist
        self.assertTrue(os.path.isfile(self.id_full_path))
        self.assertEqual(self.id_full_path, self.id_full_path)

unittest.main()
