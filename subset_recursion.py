def power_set(inp):
    # returns a list of all subsets of the list a
    if not inp:
        return [[]]
    else:
        main_subset = []
        for small_subset in power_set(inp[1:]):
            main_subset += [small_subset]
            main_subset += [[inp[0]] + small_subset]
        return main_subset


if __name__ == '__main__':
    seq = ['a', 'b', 'c']
    ans = power_set(seq)
    print("Subset for {} is {} with len {}".format(seq, ans, len(ans)))
