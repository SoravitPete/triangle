import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):

    valid_triangles = [
            (1, 1, 1),
            (3, 4, 5),
            (3, 4, 6),
            (6, 10, 20),
            (4, 5, 6)
            ]

    def test_valid_triangle(self):
        for a, b, c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue(is_triangle(a, b, c), msg)

    not_valid_triangles = [
            (20, 10, 10),
            (2, 1, 1),
            (6, 10, 4),
            (3, 4, 5),
            (4, 20, 50),
            (8, 7, 20)
        ]

    def test_not_triangle(self):
        for a, b, c in self.not_valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertFalse(is_triangle(a, b, c), msg)

    invalid_argument = [
            (-1, 2, 2),
            (1, -1, 2),
            (1, 2, -1),
            (3, 4, 5),
            (-2, 2, 1)
        ]

    def test_invalid_argument_raises_exception(self):
        for a, b, c in self.invalid_argument:
            with self.subTest():
                with self.assertRaises(ValueError):
                    b1 = is_triangle(a, b, c)
