import unittest

from validator.crn_validator import CrnValidator


class TestCrnValidator(unittest.TestCase):

    def test_crn_validator(self):
        crns = {
            '120-86-65164': True,  # Google
            '220-81-62517': True,  # Naver
            '120-81-47521': True,  # Kakao
            '144-81-10490': True,  # 라인
            '120-88-00767': True,  # 쿠팡
            '120-87-65763': True,  # 배민
            '375-87-00088': True,  # 당근
            '120-88-01280': True,  # 토스
            '125-88-45232': False,  # 랜덤
        }
        for crn, assert_equal_value in crns.items():
            self.assertEqual(CrnValidator.validate(crn), assert_equal_value)
