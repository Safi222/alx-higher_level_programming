#! usr/bin/python3


"""

A test module for the class Base

Unittest classes:
    TestBase_init
    TestBase_to_json
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """Unittest to test the initialization of the base class"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)

    def test_unique_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_nb_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_after_del(self):
        b1 = Base()
        old_nb = Base().id
        del b1
        b2 = Base()
        self.assertEqual(old_nb, b2.id - 1)

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_str_id(self):
        self.assertEqual(Base("hi").id, "hi")

    def test_bytes_id(self):
        self.assertEqual(Base(b"hi").id, b"hi")

    def test_bytearray_id(self):
        self.assertEqual(Base(bytearray(b"hi")).id, bytearray(b"hi"))

    def test_memoryview_id(self):
        self.assertEqual(Base(memoryview(b"hi")).id, memoryview(b"hi"))

    def test_list_id(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_tuple_id(self):
        self.assertEqual(Base((2, 5)).id, (2, 5))

    def test_dict_id(self):
        self.assertEqual(Base({"hol": "sch"}).id, {"hol": "sch"})

    def test_negative_id(self):
        self.assertEqual(Base(-5).id, -5)

    def test_float_id(self):
        self.assertEqual(Base(5.6).id, 5.6)

    def test_NaN_id(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_inf_id(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_complex_id(self):
        self.assertEqual(Base(complex(5)).id, complex(5))

    def test_bool_id(self):
        self.assertEqual(Base(True).id, True)

    def test_set_id(self):
        self.assertEqual(Base({5, 6}).id, {5, 6})

    def test_frozen_set_id(self):
        self.assertEqual(Base(frozenset({5, 6})).id, frozenset({5, 6}))

    def test_range_id(self):
        self.assertEqual(Base(range(5)).id, range(5))

    def test_public_attribute(self):
        b1 = Base(20)
        b1.id = 25
        self.assertEqual(b1.id, 25)

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects())

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base(2, 5)


class TestBase_to_json(unittest.TestCase):
    """Unittest to test the method to_json_string of the Base class"""

    def test_to_json_rectangle_type(self):
        d = Rectangle(3, 5, 7, 9, 10).to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([d])))

    def test_to_json_rectangle_one_dict(self):
        d = Rectangle(3, 5, 7, 9, 10).to_dictionary()
        self.assertEqual([d], eval((Base.to_json_string([d]))))
        self.assertTrue(len(Base.to_json_string([d])) == 53)

    def test_to_json_rectangle_two_dict(self):
        d1 = Rectangle(3, 5, 7, 9, 10).to_dictionary()
        d2 = Rectangle(2, 4, 6, 8, 11).to_dictionary()
        self.assertEqual([d1, d2], eval((Base.to_json_string([d1, d2]))))
        self.assertTrue(len(Base.to_json_string([d1, d2])) == 106)

    def test_to_json_square_type(self):
        d = Square(3, 7, 9, 10).to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([d])))

    def test_to_json_square_one_dict(self):
        d = Square(3, 7, 9, 10).to_dictionary()
        self.assertEqual([d], eval((Base.to_json_string([d]))))
        self.assertTrue(len(Base.to_json_string([d])) == 39)

    def test_to_json_square_two_dict(self):
        d1 = Square(3, 7, 9, 10).to_dictionary()
        d2 = Square(2, 6, 8, 11).to_dictionary()
        self.assertEqual([d1, d2], eval((Base.to_json_string([d1, d2]))))
        self.assertTrue(len(Base.to_json_string([d1, d2])) == 78)

    def test_to_json_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)


class TestBase_save_to_file(unittest.TestCase):
    """Unittest to test the method save_to_file"""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(3, 5, 7, 9, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(3, 5, 7, 9, 10)
        r2 = Rectangle(2, 4, 6, 8, 11)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 106)

    def test_save_to_file_one_square(self):
        s = Square(3, 7, 9, 10)
        Square.save_to_file([s])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(3, 7, 9, 10)
        s2 = Square(2, 6, 8, 11)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 78)

    def test_save_to_file_class_name(self):
        s = Square(3, 7, 9, 10)
        Base.save_to_file([s])
        with open("Base.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_overwrite(self):
        s1 = Square(3, 7, 9, 10)
        Square.save_to_file([s1])
        s2 = Square(2, 6, 8, 11)
        Square.save_to_file([s2])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(len(f.read()), 39)

    def test_base_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_base_to_file_None(self):
        Base.save_to_file(None)
        with open("Base.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="UTF8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_rectangle_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_square_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], 2)


class TestBase_from_json(unittest.TestCase):
    """Unittest to test the method from_json_string of the Base class"""

    def test_from_json_string_type(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangle(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{'id': 89, 'size': 10, 'x': 4}]
        json_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
                {'id': 89, 'size': 10, 'x': 4},
                {'id': 7, 'size': 1, 'x': 7}
                ]
        json_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 2)


class TestBase_create(unittest.TestCase):
    """Unittest to test the method create of the Base class"""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (11) 7/9 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (11) 7/9 - 3/5", str(r1))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 7, 9, 11)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 7, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (1) 5/7 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 7, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (1) 5/7 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 7, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 7, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittest to test the method load_from_file"""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
