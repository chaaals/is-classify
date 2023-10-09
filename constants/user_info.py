from re import compile

class UserInfo:
    NAME_REGEXP = compile(r'^[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*){1,2}$')
    BIRTHDAY_REGEXP = compile(r'^\d{4}-\d{2}-\d{2}$')
    CELL_NO_REGEXP = compile(r'^\+63-\d{10}$')
    EMAIL_REGEXP = compile(r'^.+@.+\..{2,}$')

    def is_valid_name(self) -> bool | None:
        return self
    
    def is_valid_birthday(self) -> bool | None:
        return self
    
    def is_valid_cellno(self) -> bool | None:
        return self
    
    def is_valid_email(self) -> bool | None:
        return self