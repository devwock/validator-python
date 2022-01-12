import settings
from validator.base_validator import BaseValidator


class PasswordValidator(BaseValidator):

    @classmethod
    def validate(cls, value: str) -> bool:

        if not value:
            return False

        if not cls._validate_length(value, settings.PASSWORD_MIN_LENGTH, settings.PASSWORD_MAX_LENGTH):
            return False

        special_count = 0
        number_count = 0
        upper_count = 0
        lower_count = 0
        for password_char in value:
            ascii = ord(password_char)
            if 48 <= ascii <= 57:  # 1 ~ 0
                number_count += 1
            elif 65 <= ascii <= 90:  # A ~ Z
                upper_count += 1
            elif 97 <= ascii <= 122:  # a ~ z
                lower_count += 1
            elif 33 <= ascii <= 126:  # special character
                special_count += 1
            else:  # invalid character
                return False

        return settings.PASSWORD_CHAR_SPECIAL_COUNT <= special_count and \
               settings.PASSWORD_CHAR_NUMBER_COUNT <= number_count and \
               settings.PASSWORD_CHAR_UPPER_COUNT <= upper_count and \
               settings.PASSWORD_CHAR_LOWER_COUNT <= lower_count
