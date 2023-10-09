from re import compile
from warnings import warn
from dateutil.parser import parse

class UserInfo:
    NAME_REGEXP = compile(r'^[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*){1,2}$')
    BIRTHDAY_REGEXP = compile(r'\d{2}[-/]\d{2}[-/]\d{4}|[A-Z][a-z]+\s\d{2},\s\d{4}|\d{2}\s[A-Z][a-z]+,\s\d{4}|\d{4}[-/]\d{2}[-/]\d{2}')
    CELL_NO_REGEXP = compile(r'^\+63-\d{10}$')
    EMAIL_REGEXP = compile(r'^.+@.+\..{2,}$')

    def is_valid_name(self) -> bool | None:
        return self
    
    def is_valid_birthday(date: str) -> bool | None:
        try:
            parse(date)
            return True
        except:
            warn('Date not valid.')
            return None
    
    def is_valid_cellno(self) -> bool | None:
        return self
    
    def is_valid_email(self) -> bool | None:
        return self