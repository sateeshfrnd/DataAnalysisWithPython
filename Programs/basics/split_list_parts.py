def split_list(src_list, num):
    avg = len(src_list) / float(num)
    result_list = []
    last = 0.0

    while last < len(src_list):
        result_list.append(src_list[int(last):int(last + avg)])
        last += avg

    return result_list


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]
        print("df")


list1 = split_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
print(list1)

list2 = split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
print(list2)

# print(list(split(list2,3)))

chunks(list2, 3)
