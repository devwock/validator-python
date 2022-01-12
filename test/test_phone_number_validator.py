import unittest

from validator.phone_number_validator import PhoneNumberValidator


class TestPhoneNumberValidator(unittest.TestCase):

    def test_phione_number_validator(self):
        phone_numbers = {
            '1588-1588': True,
            '02-1588-1588': True,
            '02-123-4567': True,
            '02-1234-5678': True,
            '031-123-4567': True,
            '031-1234-5678': True,
            '011-123-4567': True,
            '010-1234-5678': True,
            '010-1234-567811': False,
            '010-123-567': False,
            '02-123-567': False,
        }
        for phone_number, assert_equal_value in phone_numbers.items():
            self.assertEqual(PhoneNumberValidator.validate(phone_number), assert_equal_value)
