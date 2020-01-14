def find_max_min(seq, n):
    if n == 0:
        return seq[0], seq[0]
    else:
        return max(seq[n], find_max_min(seq, n-1)[0]), min(seq[n], find_max_min(seq, n-1)[1])


if __name__ == '__main__':
    A = [10, 22, 33, 32, 65, 29, 11, 67]
    print(find_max_min(A, len(A) - 1))
