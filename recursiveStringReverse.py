def reverse(string, n):
    if n == 0:
        return string[0]
    else:
        return string[n] + reverse(string, n - 1)


if __name__ == '__main__':
    s = "abcdef"
    print(reverse(s, len(s) - 1))
