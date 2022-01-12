from datetime import datetime


class BaseValidator:

    @classmethod
    def validate(cls, value):
        raise NotImplementedError()

    @classmethod
    def _validate_is_number(cls, str_value: str) -> bool:
        if not str_value:
            return False
        try:
            int(str_value)
            return True
        except ValueError:
            return False

    @classmethod
    def _validate_length(cls, str_value: str, min_length: int, max_length: int = None) -> bool:
        if str_value is None:
            return False

        value_length = len(str_value)
        if value_length < min_length:
            return False

        if max_length and value_length > max_length:
            return False

        return True

    @classmethod
    def _validate_birthday(cls, str_date: str) -> bool:
        if not str_date:
            return False

        date_str_length = len(str_date)
        if date_str_length == 6:
            date_format = '%y%m%d'
        elif date_str_length == 8:
            date_format = '%Y%m%d'
        else:
            return False

        try:
            datetime.strptime(str_date, date_format)
            return True
        except ValueError:
            return False

    @classmethod
    def _str_to_int_list(cls, str_value: str) -> [int]:
        if not str_value:
            return []
        return [int(value) for value in str_value]
