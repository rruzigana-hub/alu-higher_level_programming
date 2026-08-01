#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest class for testing the Base class."""

    def test_id_public(self):
        """Test that id is a public attribute."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_increments(self):
        """Test that id increments when None is given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_zero(self):
        """Test that id=0 is respected and not treated as None."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test that a negative id is accepted as-is."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_to_json_string_none(self):
        """Test to_json_string with None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        list_dicts = [{"id": 1, "width": 2, "height": 3}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(eval(result), list_dicts)

    def test_to_json_string_type(self):
        """Test that to_json_string returns a str."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)

    def test_from_json_string_none(self):
        """Test from_json_string with None returns []."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string returns []."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        json_string = '[{"id": 1, "width": 2}]'
        self.assertEqual(
            Base.from_json_string(json_string), [{"id": 1, "width": 2}])

    def test_from_json_string_type(self):
        """Test that from_json_string returns a list."""
        self.assertIsInstance(Base.from_json_string('[{"id": 1}]'), list)

    def test_json_round_trip(self):
        """Test that to_json_string and from_json_string are inverses."""
        list_dicts = [{"id": 1, "width": 2}, {"id": 2, "width": 3}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_str), list_dicts)

    def test_save_to_file_none(self):
        """Test save_to_file with None writes '[]' to file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Test save_to_file writes correct JSON for a list of objects."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(
            eval(content), [r1.to_dictionary(), r2.to_dictionary()])
        os.remove("Rectangle.json")

    def test_save_to_file_filename(self):
        """Test that save_to_file uses '<ClassName>.json' as filename."""
        Square.save_to_file([Square(5)])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_save_to_file_overwrites(self):
        """Test that save_to_file overwrites an existing file."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        r = Rectangle(5, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(eval(content), [r.to_dictionary()])
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file returns [] if the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_round_trip_rectangle(self):
        """Test save/load round trip for Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))
        os.remove("Rectangle.json")

    def test_load_from_file_round_trip_square(self):
        """Test save/load round trip for Square instances."""
        s1 = Square(5, 0, 0, 1)
        s2 = Square(7, 9, 1, 2)
        Square.save_to_file([s1, s2])
        result = Square.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(s1))
        self.assertEqual(str(result[1]), str(s2))
        os.remove("Square.json")

    def test_create_rectangle(self):
        """Test create() builds a Rectangle from a dictionary."""
        r1 = Rectangle(3, 5, 1, id=99)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create() builds a Square from a dictionary."""
        s1 = Square(3, 1, 2, 99)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_module_documented(self):
        """Test that the base module has documentation."""
        self.assertTrue(len(__import__("models.base",
                                        fromlist=["base"]).__doc__) > 0)

    def test_class_documented(self):
        """Test that the Base class has documentation."""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_methods_documented(self):
        """Test that all Base methods have documentation."""
        methods = [Base.__init__, Base.to_json_string, Base.save_to_file,
                   Base.from_json_string, Base.create, Base.load_from_file]
        for method in methods:
            self.assertTrue(len(method.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
