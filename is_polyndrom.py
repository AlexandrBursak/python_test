
def is_palindrome(string):
    """
    BlaBlaBla

    >>> is_palindrome('anna')
    True
    >>> is_palindrome('Anna')
    True
    >>> is_palindrome('Walter')
    False
    >>> is_palindrome('12321')
    True
    >>> is_palindrome('123456')
    False
    """
    return str(string) == str(string)[::-1]
