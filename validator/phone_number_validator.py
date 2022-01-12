# coding=utf-8
from validator.base_validator import BaseValidator


class PhoneNumberValidator(BaseValidator):

    _LAND_DIALINGS = [
        # 지역국번
        "02", "031", "032", "033", "041", "042", "043", "044", "051", "052",
        "053", "054", "055", "061", "062", "063", "064",
        # 핸드폰
        "010", "011", "012", "016", "017", "018", "019",
        # 공용서비스
        "030", "050", "060", "070", "080"
    ]

    _CARRIER_DIALINGS = [
        "1588", "1577", "1899", "1544", "1644", "1661", "1566", "1600",
        "1670", "1688", "1666", "1599", "1877", "1855", "1800"
    ]

    @classmethod
    def validate(cls, value: str) -> bool:
        if not value:
            return False

        phone_number = value.replace('-', '').replace(' ', '')

        if not cls._validate_is_number(phone_number):
            return False

        if not cls._validate_length(phone_number, min_length=8):
            return False

        phone_number_length = len(phone_number)

        if phone_number_length == 8:  # 1588-1588
            return phone_number[0:4] in cls._CARRIER_DIALINGS
        elif phone_number_length == 9:  # 02-123-4567
            return phone_number[0:2] in cls._LAND_DIALINGS
        elif 10 <= phone_number_length <= 11:  # 02-1234-1234, 031-123-1234, 010-1234-1234
            if phone_number[0:2] == '02':
                return True
            return phone_number[0:3] in cls._LAND_DIALINGS
        else:
            return False
