"""
Return true for palidrome
test with case sensitive and non case sensitive
EG : Madam
"""

import string


class Palindrome:
    @staticmethod
    def is_palindrome(word):
        if word[::-1] == word:
            return True

        if word[::-1].lower() == word.lower():
            return True

        return False

    @staticmethod
    def is_palindrome_method_2(word):
        str = ''
        for i in word:
            str = i + str

        if word == str:
            return True

        if word.lower() == str.lower():
            return True

        return False


print("Method 1 Check Case-sensitivity : ", Palindrome.is_palindrome('Madam'))
print("Method 1 Check Non-Case-sensitivity : ", Palindrome.is_palindrome('Madam'))
print("Method 1 Check for non palindrome : ", Palindrome.is_palindrome('test'))

print("Method 2 Check Case-sensitivity : ", Palindrome.is_palindrome_method_2('Madam'))
print("Method 2 Check Non-Case-sensitivity : ", Palindrome.is_palindrome_method_2('Madam'))
print("Method 2 Check for non palindrome : ", Palindrome.is_palindrome_method_2('test'))
