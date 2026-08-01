#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittest class for testing the Rectangle class."""

    def test_is_base_subclass(self):
        """Test that Rectangle inherits from Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(3, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_attributes_assigned(self):
        """Test that width, height, x, y are assigned correctly."""
        r = Rectangle(3, 4, 5, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_id_passed_to_base(self):
        """Test that the id argument is passed to the Base constructor."""
        r = Rectangle(3, 4, id=99)
        self.assertEqual(r.id, 99)

    def test_id_auto_increment(self):
        """Test that id auto-increments when not given."""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)

    def test_width_type_error(self):
        """Test that a non-integer width raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_type_error(self):
        """Test that a non-integer height raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_x_type_error(self):
        """Test that a non-integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_type_error(self):
        """Test that a non-integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, [])

    def test_width_zero_value_error(self):
        """Test that width of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative_value_error(self):
        """Test that a negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero_value_error(self):
        """Test that height of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative_value_error(self):
        """Test that a negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_negative_value_error(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_negative_value_error(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_x_zero_ok(self):
        """Test that x=0 is a valid value."""
        r = Rectangle(10, 2, 0, 0)
        self.assertEqual(r.x, 0)

    def test_setter_width(self):
        """Test the width setter."""
        r = Rectangle(1, 1)
        r.width = 20
        self.assertEqual(r.width, 20)

    def test_setter_width_invalid(self):
        """Test the width setter with an invalid value."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = -20

    def test_area(self):
        """Test that area() returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7).area(), 56)

    def test_display_basic(self):
        """Test display() with no offset."""
        r = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """Test display() with x and y offset."""
        r = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args_partial(self):
        """Test update() with a partial list of positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 2, 10))

    def test_update_args_full(self):
        """Test update() with all positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_kwargs(self):
        """Test update() with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(
            (r.id, r.width, r.x, r.y), (89, 2, 3, 1))

    def test_update_kwargs_skipped_when_args_present(self):
        """Test that kwargs are ignored when args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, height=100)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.height, 10)

    def test_to_dictionary_keys(self):
        """Test that to_dictionary returns the correct keys."""
        r = Rectangle(10, 2, 1, 9, 3)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that to_dictionary returns the correct values."""
        r = Rectangle(10, 2, 1, 9, 3)
        d = r.to_dictionary()
        self.assertEqual(d["id"], 3)
        self.assertEqual(d["width"], 10)
        self.assertEqual(d["height"], 2)
        self.assertEqual(d["x"], 1)
        self.assertEqual(d["y"], 9)

    def test_to_dictionary_type(self):
        """Test that to_dictionary returns a dict."""
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_module_documented(self):
        """Test that the rectangle module has documentation."""
        self.assertTrue(len(__import__(
            "models.rectangle", fromlist=["rectangle"]).__doc__) > 0)

    def test_class_documented(self):
        """Test that the Rectangle class has documentation."""
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_methods_documented(self):
        """Test that all Rectangle methods have documentation."""
        methods = [Rectangle.__init__, Rectangle.area, Rectangle.display,
                   Rectangle.__str__, Rectangle.update,
                   Rectangle.to_dictionary]
        for method in methods:
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
