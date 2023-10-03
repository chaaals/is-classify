import re

def is_valid_regex(pattern) -> bool:
    try:
        re.compile(pattern)
        return True
    except:
        return False