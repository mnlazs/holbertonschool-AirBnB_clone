#!/usr/bin/python3
"""
Esta es un modulo de prueba de BaseModel, llamado\
    test_base_model que usa Test Unitarios sobre el modulo\
        'models/base_model', derechos a Chris!\
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TASK 1 UNIT TESTS"""
    def test_bas_mod_id(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_bas_mod_crt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def test_bas_mod_upd(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_uwu_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_ini_tim(self):
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_sav_upd_met(self):
        bm1 = BaseModel()
        cat = bm1.created_at
        uat = bm1.updated_at
        bm1.save()
        self.assertEqual(bm1.created_at, cat)
        self.assertNotEqual(bm1.updated_at, uat)

    def test_richard(self):
        bm1 = BaseModel()
        richard = bm1.to_dict()
        self.assertIsInstance(richard, dict)
        self.assertIsInstance(richard["updated_at"], str)
        self.assertIsInstance(richard["created_at"], str)

    def test_str_met(self):
        bm1 = BaseModel()
        self.assertIn(bm1.id, str(bm1))


class TestBaseModel2(unittest.TestCase):
    "TASK 2 UNIT TESTS"
    def test_init_with_kwargs(self):
        created_at = '2023-04-20T00:00:00.000000'
        updated_at = '2023-04-20T00:00:00.000000'
        richard1 = {
            'id': 'villager',
            'created_at': created_at,
            'updated_at': updated_at,
            'name': 'uwu'
        }
        bm1 = BaseModel(**richard1)
        self.assertEqual(bm1.id, 'villager')
        self.assertEqual(bm1.created_at, datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.updated_at, datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.name, 'uwu')


if __name__ == "__main__":
    unittest.main()

    class TestBaseModel(unittest.TestCase):
        """Test for BaseModel class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = BaseModel()
        self.test_model2 = BaseModel()

    def test_basic_setup(self):
        """test for to_json method of BaseModel class
        """
        self.assertTrue(hasattr(self.test_model1, "id"))
        self.assertTrue(hasattr(self.test_model1, "__class__"))
        self.assertTrue(hasattr(self.test_model1, "created_at"))
        self.assertTrue(hasattr(self.test_model1, "updated_at"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        """testing attributes to ensure proper typing
        """
        self.assertTrue(type(self.test_model1.id) is str)
        self.assertTrue(type(self.test_model1.__class__) is type)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        m1u = self.test_model1.updated_at
        m2u = self.test_model2.updated_at
        self.assertTrue(type(m1c) is datetime.datetime)
        self.assertTrue(type(m2c) is datetime.datetime)
        self.assertTrue(type(m1u) is datetime.datetime)
        self.assertTrue(type(m2u) is datetime.datetime)

    def test_save(self):
        """testing whether save updates the updated_at attribute
        """
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

    def test_to_json(self):
        """tests to_json method with diffs in output & in-memory objects
        """
        testmodelid = self.test_model1.id
        jsondict = self.test_model1.to_json()
        self.assertNotEqual(jsondict, self.test_model1.__dict__)
        self.assertEqual(jsondict["id"], self.test_model1.__dict__["id"])
        self.assertNotEqual(jsondict["created_at"],
                            self.test_model1.__dict__["created_at"])
        self.assertNotEqual(type(jsondict["created_at"]),
                            type(self.test_model1.__dict__["created_at"]))

if __name__ == '__main__':
    unittest.main()
