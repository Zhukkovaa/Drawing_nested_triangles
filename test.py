import unittest
from unittest.mock import Mock
from main import validate_input

class TestValidateInput(unittest.TestCase):

    def test_valid_positive_integer1(self):
        # Тестирование ввода допустимого положительного целого числа
        input_num = "50"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertTrue(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="")

    def test_valid_positive_integer2(self):
        # Тестирование ввода допустимого положительного целого числа
        input_num = "10"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertTrue(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="")

    def test_negative_integer1(self):
        # Тестирование ввода отрицательного целого числа
        input_num = "-1337"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

    def test_negative_integer2(self):
        # Тестирование ввода отрицательного целого числа
        input_num = "-1488"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

    def test_zero_input(self):
        # Тестирование ввода нуля
        input_num = "0"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

    def test_letters_input(self):
        # Тестирование ввода нечисловых данных
        input_num = "abcdefg"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="Введите числовое значение")

    def test_symbols_input(self):
        # Тестирование ввода нечисловых данных
        input_num = ";*"
        error_label = Mock()  # Создаем заглушку для tk.Label()
        result = validate_input(input_num, error_label)
        self.assertFalse(result)
        # Проверка, что заглушка была вызвана с нужными аргументами
        error_label.config.assert_called_once_with(text="Введите числовое значение")

if __name__ == '__main__':
    unittest.main()