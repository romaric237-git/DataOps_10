import unittest
from transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform_data(self):
        data = [{'old_column': 1}, {'old_column': 2}]
        result = transform_data(data)
        self.assertEqual(list(result['new_column']), [2, 4])

if __name__ == "__main__":
    unittest.main()