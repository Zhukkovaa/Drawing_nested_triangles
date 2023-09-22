import unittest
import tkinter as tk
from main import validate_input

class TestValidateInput(unittest.TestCase):

    def setUp(self):
        # Создаем окно Tkinter для тестирования
        self.root = tk.Tk()

    def tearDown(self):
        # Уничтожаем окно Tkinter после каждого теста
        self.root.destroy()

    def test_valid_positive_integer1(self):
        # Тестирование ввода допустимого положительного целого числа
        input_num = "50"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertTrue(result)
        self.assertEqual(error_label.cget("text"), "")  # Проверка, что текст метки пуст

    def test_valid_positive_integer2(self):
        # Тестирование ввода допустимого положительного целого числа
        input_num = "10"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertTrue(result)
        self.assertEqual(error_label.cget("text"), "")  # Проверка, что текст метки пуст

    def test_negative_integer1(self):
        # Тестирование ввода отрицательного целого числа
        input_num = "-1337"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Enter a positive integer greater than 0")

    def test_negative_integer2(self):
        # Тестирование ввода отрицательного целого числа
        input_num = "-228"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Enter a positive integer greater than 0")

    def test_zero_input(self):
        # Тестирование ввода нуля
        input_num = "0"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Enter a positive integer greater than 0")

    def test_non_numeric_input1(self):
        # Тестирование ввода нечисловых данных
        input_num = "abcdefg"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Enter a numeric value")

    def test_non_numeric_input2(self):
        # Тестирование ввода нечисловых данных
        input_num = ";*"
        error_label = tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        self.assertEqual(error_label.cget("text"), "Enter a numeric value")

if __name__ == '__main__':
    unittest.main()