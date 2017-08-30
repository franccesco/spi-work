"""Test remarks and its functions."""

import unittest
import modules
import time
import random
from os import path


class EntityTestCase(unittest.TestCase):
    """Test new_entity function."""

    def setUp(self):
        """Set up variables and locations."""
        # simulating an entity ID
        self.new_entity_id = str(random.randint(100000, 999999))

        # defining path structure (today) and template locations
        self.path = 'entities/' + time.strftime('%Y/%m/%d')
        self.id_full_path = self.path + '/' + self.new_entity_id + '.md'
        self.draft_location = self.path + '/draft_entity.md'
        self.am_template_location = 'templates/am_template.md'
        self.am_pep_template_location = 'templates/am_pep_template.md'
        self.empty_template_location = 'templates/empty_template.md'
        self.pep_template_location = 'templates/pep_template.md'

        # opening templates to read them later and compare them
        with open(self.empty_template_location) as empty_temp_object:
            self.empty_template = empty_temp_object.read()
        with open(self.am_template_location) as am_temp_object:
            self.am_template = am_temp_object.read()
        with open(self.am_pep_template_location) as am_pep_temp_object:
            self.am_pep_template = am_pep_temp_object.read()
        with open(self.pep_template_location) as pep_temp_object:
            self.pep_template = pep_temp_object.read()

    # uncomment this section to test new file creations
    # but it can clutter the folders when ran too many times
    def test_file_creation(self):
        """Test random id file and empty file."""
        modules.io.create_entity(self.new_entity_id)
        # check if file exist
        self.assertTrue(path.isfile(self.id_full_path))
        self.assertEqual(self.id_full_path, self.id_full_path)

    def test_empty_file(self):
        """Test if empty file is named correctly."""
        modules.io.create_entity()
        self.assertTrue(self.draft_location)

    def test_created_templates(self):
        """Test if all template are created correctly."""
        # create skeleton draft and open it to compare it
        modules.io.create_entity()
        with open(self.draft_location) as draft_location_object:
            draft_template = draft_location_object.read()
        self.assertEqual(self.empty_template, draft_template)

        # create PEP template
        modules.io.create_entity(entity_PEP=True, entity_AM=False)
        with open(self.draft_location) as draft_location_object:
            draft_template = draft_location_object.read()
        self.assertEqual(self.pep_template, draft_template)

        # create adverse media template
        modules.io.create_entity(entity_AM=True)
        with open(self.draft_location) as draft_location_object:
            draft_template = draft_location_object.read()
        self.assertEqual(self.am_template, draft_template)

        # create PEP with adverse media template
        modules.io.create_entity(entity_AM=True, entity_PEP=True)
        with open(self.draft_location) as draft_location_object:
            draft_template = draft_location_object.read()

    # def test_no_overwrite():
    #     overwrite_options = modules.io.create_entity(overwrite_entity=False)
    #     self.assertFalse(overwrite_options, 'False returned')


if __name__ == '__main__':
    unittest.main()
