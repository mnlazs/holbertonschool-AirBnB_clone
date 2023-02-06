#!/usr/bin/python3
"""
Esta es un modulo de prueba de BaseModel, llamado\
    test_base_model que usa Test Unitarios sobre el modulo\
        'models/base_model'
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