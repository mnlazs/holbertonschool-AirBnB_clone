#!/usr/bin/python3
'''
This is the 'test_amenity' module.
test_amenity uses unittest to test the 'models/amenity' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Test for amenity class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = Amenity()
        self.test_model2 = Amenity()

    def test_basic_setup(self):
        """test for amenity class attributes
        """
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)
        self.assertTrue(type(m1c) is datetime.datetime)

    def test_types(self):
        """testing for proper typing of attributes
        """
        self.assertTrue(type(self.test_model1.name) is str)

    def test_save(self):
        """testing whether save updates the updated_at attribute
        """
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()