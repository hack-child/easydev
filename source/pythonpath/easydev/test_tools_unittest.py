#!/usr/bin/env python3
# coding: utf-8

import unittest
import tempfile
import os
import tools


class TestTools(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        pass

    def test_render(self):
        expected = 'Nombre: Teresa\nPaís: Portugal'
        template = 'Nombre: $name\nPaís: $country'
        data = (('name', 'Teresa'), ('country', 'Portugal'))
        result = tools.render(template, data)
        self.assertEqual(result, expected)

    def test_render_number(self):
        expected = 'Age: 40\nPhone: 12345678'
        template = 'Age: $age\nPhone: $phone'
        data = (('age', 40), ('phone', 12345678))
        result = tools.render(template, data)
        self.assertEqual(result, expected)

    def test_file_open(self):
        expected = 'LibreOffice Python'
        test_path = os.path.join(self.test_dir, 'test.txt')
        with open(test_path, 'w') as f:
            f.write(expected)
        result = tools.file_open(test_path)
        self.assertEqual(result, expected)

    def test_file_open_binary(self):
        expected = b'LibreOffice Python'
        test_path = os.path.join(self.test_dir, 'test.txt')
        with open(test_path, 'wb') as f:
            f.write(expected)
        result = tools.file_open(test_path, 'rb')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()