from validator.base_validator import BaseValidator


class CrnValidator(BaseValidator):

    _VERIFICATION_CODE = [1, 3, 7, 1, 3, 7, 1, 3, 5]

    @classmethod
    def validate(cls, value: str) -> bool:
        if not value:
            return False

        crn = value.replace('-', '').replace(' ', '')

        if not cls._validate_is_number(crn):
            return False

        if not cls._validate_length(crn, min_length=10, max_length=10):
            return False

        crn_values = crn[:-1]
        crn_numbers = cls._str_to_int_list(crn_values)

        verification_value = 0
        for value1, value2 in zip(crn_numbers, cls._VERIFICATION_CODE):
            verification_value += value1 * value2

        verification_value += int(int(crn_values[-1]) * cls._VERIFICATION_CODE[-1] / 10)
        verification_value %= 10
        verification_value = verification_value if verification_value == 0 else 10 - verification_value
        
        if verification_value != int(crn[-1]):
            return False

        return True
