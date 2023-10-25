from re import compile
from warnings import warn
from dateutil.parser import parse

class UserInfo:
    NAME_REGEXP = compile(r'^[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*){1,2}$')
    BIRTHDAY_REGEXP = compile(r'\d{2}[-/]\d{2}[-/]\d{4}|[A-Z][a-z]+\s\d{2},\s\d{4}|\d{2}\s[A-Z][a-z]+,\s\d{4}|\d{4}[-/]\d{2}[-/]\d{2}')
    CELL_NO_REGEXP = compile(r'^(0\d{10}|(?:\+63|63)(?:-\d{10}|\d{10}))$')
    # email format: name@domain.topleveldomain
    #   name: any number of any letters, numbers, and these characters: ! # $ % & ' * + - / = ? ^ _ ` { |
    #   domain: any number of any letters, numbers, a hypen, and a period
    #   topleveldomain: minimum of 2 of any letters, and a period (.net, .com, .co.uk, .plm.edu.ph)
    EMAIL_REGEXP = compile(r"^(\w|[!#$%&'*+-/=?^`{|])+@(\w|[-.])+\.(\w|[.]){2,}$")
    
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