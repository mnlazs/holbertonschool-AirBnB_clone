import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.test_model1 = BaseModel()
        self.test_model2 = BaseModel()

    def test_basic_setup(self):
        self.assertTrue(hasattr(self.test_model1, "id"))
        self.assertTrue(hasattr(self.test_model1, "__class__"))
        self.assertTrue(hasattr(self.test_model1, "created_at"))
        self.assertTrue(hasattr(self.test_model1, "updated_at"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        self.assertTrue(type(self.test_model1.id) is str)
        self.assertTrue(type(self.test_model1.__class__) is type)
        self.assertTrue(type(self.test_model1.created_at) is datetime)
        self.assertTrue(type(self.test_model1.updated_at) is datetime)

class TestBaseModel2(unittest.TestCase):
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
