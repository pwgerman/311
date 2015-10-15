from babel.dates import format_timedelta, format_datetime

def datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE MM/dd/y"
    return format_datetime(value, format)

def timedelta(value):
    return format_timedelta(value, locale='en_US')
