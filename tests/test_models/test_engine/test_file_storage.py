#!/usr/bin/python3
"""This module contains tests for FileStorage class"""

import os
import unittest
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    
    def setUP(self):
        self.my_storage = FileStorage()
        self.test_file_path = "test_file.json"

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_all(self):

        obj_1 = {"name": "ALX", "number":98}
        obj_2 = {"name": "Brass", "number": 100}

        self.my_storage._FileStorage__objects = {
            "TestInst1": obj_1,
            "TestInst2": obj_2
        }

        self.assertEqual(self.my_storage.all(), {
            "TestInst1": obj_1,
            "TestInst2": obj_2
        })

    def test_new(self):
        object_ = {"name": "ALX", "number": 102}
        self.my_storage.new(object_)

        self.assertEqual(self.my_storage.FileStorage__objects, {"obj_3": object_})

    def test_save_reload(self):
        obj_1 = {"name": "ALX", "number":98}
        obj_2 = {"name": "Brass", "number": 100}

        self.my_storage._FileStorage__objects = {
            "TestInst1": obj_1,
            "TestInst2": obj_2
        }

        self.my_storage._FileStorage__file_path = self.test_file_path
        self.my_storage.save()
        self.my_storage._FileStorage__objects = {}
        self.my_storage.reload()

        self.assertEqual(self.my_storage.all(), {
            "TestInst1": obj_1,
            "TestInst2": obj_2
        })


if __name__ == "__main__":
    unittest.main()
