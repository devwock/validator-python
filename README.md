# validator-python

여러 Validator 파이썬 구현 모음

## CrnValidator

사업자 등록번호 검증

```python
from validator.crn_validator import CrnValidator
CrnValidator.validate('사업자등록번호')

True/False
```

## PasswordValidator

### Prerequisite

`settings.py`에서 다음 정책을 정할 수 있습니다.

```python
PASSWORD_MIN_LENGTH = 6  # 비밀번호 최소 길이
PASSWORD_MAX_LENGTH = None # 비밀번호 최대 길이
PASSWORD_CHAR_SPECIAL_COUNT = 2  # 특수 문자 최소 글자 수
PASSWORD_CHAR_LOWER_COUNT = 2  # 영소문자 최소 글자 수
PASSWORD_CHAR_UPPER_COUNT = 2  # 영대문자 최소 글자 수
PASSWORD_CHAR_NUMBER_COUNT = 2  # 숫자 최소 글자 수
```

### Example

```python
from validator.password_validator import PasswordValidator
PasswordValidator.validate('비밀번호')

True/False
```

## PhoneNumberValidator

전화번호 검증

```python
from validator.phone_number_validator import PhoneNumberValidator
PhoneNumberValidator.validate('전화번호')

True/False
```

## RrnValidator

주민등록번호/외국인등록번호 검증

단, 주민등록번호 마지막 검증 숫자는 2020년 10월부터 뒤 첫자리를 제외하고 전부 무작위로 변경되어 제거되었습니다.  
따라서 `111111-1111111`도 올바른 주민등록번호입니다.

```python
from validator.rrn_validator import RrnValidator
RrnValidator.validate('주민등록번호')

True/False


RrnValidator.validate_birthday('주민등록번호 앞자리')

True/False
```
