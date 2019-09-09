from functools import cmp_to_key

if __name__ == "__main__":
    a = [
        {'age': 11, 'height': 123},
        {'age': 10, 'height': 124},
        {'age': 9, 'height': 125},
        {'age': 8, 'height': 126}
    ]
    b = [2, 3, 1, 5, 2]
    # print(sorted(a, key=cmp_to_key(lambda x, y: x['age'] - y['age'])))
    b.sort(reverse=True)
    print(b)
    # print(a)
