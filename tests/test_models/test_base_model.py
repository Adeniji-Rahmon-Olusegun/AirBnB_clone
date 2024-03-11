#!/usr/bin/python3
"""Module contains tests for BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    def test_init(self):
        m_model = BaseModel()

        self.assertIsNotNone(m_model.id)
        self.assertIsNotNone(m_model.created_at)
        self.assertIsNotNone(m_model.updated_at)

    def test_save(self):
        m_model = BaseModel()

        last_update = m_model.updated_at
        curr_update = m_model.save()

        self.assertNotEqual(last_update, curr_update)
        self.assertIsInstance(last_update, datetime)
        # self.assertIsInstance(m_model.save(), datetime)

    def test_to_dict(self):
        m_model = BaseModel()

        model_dict = m_model.to_dict()

        self.assertIsInstance(model_dict, dict)

        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], m_model.id)
        self.assertEqual(model_dict["created_at"], m_model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], m_model.updated_at.isoformat())

    def test_str(self):
        m_model = BaseModel()

        self.assertTrue(str(m_model).startswith("[BaseModel]"))

        self.assertIn(m_model.id, str(m_model))

        self.assertIn(str(m_model.__dict__), str(m_model))

if __name__ == "__main__":
    unittest.main()

