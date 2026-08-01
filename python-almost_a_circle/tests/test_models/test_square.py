#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittest class for testing the Square class."""

    def test_is_rectangle_subclass(self):
        """Test that Square inherits from Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_width_equals_height(self):
        """Test that width and height are both set to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_x_y_assigned(self):
        """Test that x and y are assigned correctly."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_id_passed(self):
        """Test that the id argument is passed through."""
        s = Square(3, 1, 3, 99)
        self.assertEqual(s.id, 99)

    def test_id_auto_increment(self):
        """Test that id auto-increments when not given."""
        s1 = Square(3)
        s2 = Square(3)
        self.assertEqual(s2.id, s1.id + 1)

    def test_no_extra_attributes(self):
        """Test that Square doesn't create new private attributes."""
        s = Square(5)
        self.assertFalse(hasattr(s, "_Square__size"))

    def test_str(self):
        """Test the __str__ representation."""
        s = Square(3, 1, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 1/3 - 3")

    def test_area(self):
        """Test that area() returns size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2).area(), 4)

    def test_size_getter(self):
        """Test the size getter returns width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test that the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_type_error(self):
        """Test that an invalid size raises TypeError."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_value_error(self):
        """Test that an invalid size raises ValueError."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -3

    def test_update_args_partial(self):
        """Test update() with a partial list of positional args."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual((s.id, s.size), (1, 2))

    def test_update_args_full(self):
        """Test update() with all positional args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_kwargs(self):
        """Test update() with keyword arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.id, s.size, s.y), (89, 7, 1))

    def test_update_kwargs_skipped_when_args_present(self):
        """Test that kwargs are ignored when args are given."""
        s = Square(5)
        s.update(89, size=100)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 5)

    def test_to_dictionary_keys(self):
        """Test that to_dictionary returns the correct keys."""
        s = Square(10, 2, 1, 3)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that to_dictionary returns the correct values."""
        s = Square(10, 2, 1, 3)
        d = s.to_dictionary()
        self.assertEqual(d["id"], 3)
        self.assertEqual(d["size"], 10)
        self.assertEqual(d["x"], 2)
        self.assertEqual(d["y"], 1)

    def test_to_dictionary_round_trip(self):
        """Test that a Square rebuilt from its dictionary is equal."""
        s1 = Square(10, 2, 1, 99)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_module_documented(self):
        """Test that the square module has documentation."""
        self.assertTrue(len(__import__(
            "models.square", fromlist=["square"]).__doc__) > 0)

    def test_class_documented(self):
        """Test that the Square class has documentation."""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_methods_documented(self):
        """Test that all Square methods have documentation."""
        methods = [Square.__init__, Square.__str__, Square.update,
                   Square.to_dictionary]
        for method in methods:
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
