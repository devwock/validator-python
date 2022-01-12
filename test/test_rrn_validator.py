import unittest

from validator.rrn_validator import RrnValidator


class TestRrnValidator(unittest.TestCase):

    def test_rrn_validator(self):
        rrns = {
            '870606-1286252': True,  # 견본 주민등록번호
            '800304-1034513': True,  # 견본 주민등록번호
            '910407-2076661': True,  # 견본 주민등록번호
            '771029-8878160': True,  # 견본 외국인 등록번호
            '731228-2686181': True,  # 견본 외국인 등록번호
            '700101-5801798': True,  # 견본 외국인 등록번호
            '111111-1111118': True,
            '123456-1234567': False,
        }
        for rrn, assert_equal_value in rrns.items():
            self.assertEqual(RrnValidator.validate(rrn), assert_equal_value)
