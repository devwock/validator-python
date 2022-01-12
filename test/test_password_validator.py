import unittest

from validator.password_validator import PasswordValidator


class TestPasswordValidator(unittest.TestCase):

    def test_password_validator(self):
        passwords = {
            '12345': False,
            '123456': False,
            '123456!@#': False,
            'qwerty': False,
            'qwerty12': False,
            'qwerty12!@#': False,
            'QWERTY': False,
            'QWERTY12': False,
            'QWERTY12!@#': False,
            'qweRTY12!@#': True,
        }
        for password, assert_equal_value in passwords.items():
            self.assertEqual(PasswordValidator.validate(password), assert_equal_value)


