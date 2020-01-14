def is_palindrome(s, start, stop):
    if start < stop - 1:
        return s[start] == s[stop] and is_palindrome(s, start + 1, stop - 1)
    else:
        return True


if __name__ == '__main__':
    string = "aac"
    print("{} is palindrome:{}".format(string, is_palindrome(string, 0, len(string) - 1)))
