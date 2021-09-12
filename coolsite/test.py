class TooShortName(Exception):
    pass

def foo(name):
    if len(name) < 10:
        raise TooShortName('Name too short')

foo('aa')