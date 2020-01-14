def unique(lst):
    if len(lst) == 1:  # if a single element left, list has unique elements
        return True
    else:
        rem = lst[1:]
        return lst[0] not in rem and unique(rem)  # move to next element


if __name__ == '__main__':
    A = [19, 23, 45, 18, 21, 22, 67]
    print(unique(A))
