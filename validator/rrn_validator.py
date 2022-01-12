# coding=utf-8
from validator.base_validator import BaseValidator


class RrnValidator(BaseValidator):
    # 주민등록번호/외국인등록번호 뒷 첫 자리
    # 1/2: 1900~1999년 사이에 탄생한 내국인
    # 3/4: 2000~2099년 사이에 탄생한 내국인
    # 5/6: 1900~1999년 사이에 탄생한 외국인
    # 7/8: 2000~2099년 사이에 탄생한 외국인
    # 9/0: 1800~1899년 사이에 탄생한 내국인 -> 현재 대부분 사망
    _RRN_FIRST_CODE = [1, 2, 3, 4, 5, 6, 7, 8]

    _FOREIGN_FIRST_CODE = _RRN_FIRST_CODE[4:]

    @classmethod
    def validate_rrn_first_code(cls, rrn_first_code):
        if not rrn_first_code:
            return False

        if rrn_first_code not in cls._RRN_FIRST_CODE:
            return False

        return True

    @classmethod
    def validate_birthday(cls, value: str) -> bool:
        return super()._validate_birthday(value)

    @classmethod
    def validate(cls, value: str) -> bool:
        if not value:
            return False

        rrn = value.replace('-', '').replace(' ', '')

        if not cls._validate_is_number(rrn):
            return False

        if not cls._validate_length(rrn, min_length=13, max_length=13):
            return False

        if not cls._validate_birthday(rrn[0:6]):
            return False

        if int(rrn[6]) not in cls._RRN_FIRST_CODE:
            return False

        # 외국인 등록번호 12번째 숫자 검증은 2012.06.01 이후 제거됨
        # https://overseas.mofa.go.kr/bo-ko/brd/m_6056/view.do?seq=918847

        # 마지막 번호 검증은 2020년 10월부터 뒤 첫자리를 제외하고 전부 무작위로 변경되어 제거됨
        return True
