def find_max_min(seq, n):
    if n == 0:
        return seq[0], seq[0]
    else:
        ma, mi = find_max_min(seq, n - 1)
        return max(seq[n], ma), min(seq[n], mi)


if __name__ == '__main__':
    A = [10, 22, 33, 32, 65, 29, 11, 67]
    print(find_max_min(A, len(A) - 1))
