year = 2020

months = {
    'Januari'   : 31,
    'Februari'  : year % 4 != 0 if 28 else 29,
    'March'     : 31,
    'April'     : 30,
    'May'       : 31,
    'June'      : 30,
    'Juli'      : 31,
    'August'    : 31,
    'September' : 30,
    'October'   : 31,
    'November'  : 30,
    'December'  : 31
}

days = [
    'Mo',
    'Tu',
    'We',
    'Th',
    'Fr',
    'Sa',
    'Su'
]