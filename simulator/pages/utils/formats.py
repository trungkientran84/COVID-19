def global_format_func(s):
    fmt = {
        'state': 'State',
        'city': 'City'
    }
    if s in fmt.keys():
        return fmt[s]
    else:
        return s
