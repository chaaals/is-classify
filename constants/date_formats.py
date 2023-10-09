from enum import Enum

class DateFormatsEnum(Enum):
    MM_DD_YYYY = '%m-%d-%Y'
    DD_MM_YYYY = '%d-%m-%Y'
    S_MM_DD_YYYY = '%m/%d/%Y'
    S_DD_MM_YYYY = '%d/%m/%Y'
    MONTH_DD_YYYY = '%B %d, %Y'
    MON_DD_YYYY = '%b %d, %Y'
    DD_MONTH_YYYY = '%d %B, %Y'
    DD_MON_YYYY = '%d %b, %Y'
    YYYY_MM_DD = '%Y-%m-%d'
    YYYY_DD_MM = '%Y-%m-%d'
    S_YYYY_MM_DD = '%Y/%m/%d'
    S_YYYY_DD_MM = '%Y/%m/%d'

DATE_FORMATS = [
    DateFormatsEnum.MM_DD_YYYY.value,
    DateFormatsEnum.DD_MM_YYYY.value,
    DateFormatsEnum.S_MM_DD_YYYY.value,
    DateFormatsEnum.S_DD_MM_YYYY.value,
    DateFormatsEnum.MONTH_DD_YYYY.value,
    DateFormatsEnum.MON_DD_YYYY.value,
    DateFormatsEnum.DD_MONTH_YYYY.value,
    DateFormatsEnum.DD_MON_YYYY.value,
    DateFormatsEnum.YYYY_MM_DD.value,
    DateFormatsEnum.YYYY_DD_MM.value,
    DateFormatsEnum.S_YYYY_MM_DD.value,
    DateFormatsEnum.S_YYYY_DD_MM.value,
]