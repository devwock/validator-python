from validator.crn_validator import CrnValidator
from validator.password_validator import PasswordValidator
from validator.phone_number_validator import PhoneNumberValidator
from validator.rrn_validator import RrnValidator


def main():
    print(CrnValidator.validate('120-86-65164'))
    print(PasswordValidator.validate('qweRTY12!@#'))
    print(PhoneNumberValidator.validate('010-1234-5678'))
    print(RrnValidator.validate('111111-1111118'))


if __name__ == "__main__":
    main()
