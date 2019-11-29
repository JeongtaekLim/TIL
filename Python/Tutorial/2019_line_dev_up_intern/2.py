def run():
    import itertools
    from functools import cmp_to_key
    numbers = input().strip().split(' ')
    numbers = list(map(''.join, itertools.permutations(numbers)))
    transformed = [{'str': x, 'int': int(x)} for x in numbers]
    transformed = sorted(transformed, key=cmp_to_key(lambda a, b: a['int'] - b['int']))
    k = int(input())
    print(transformed[k - 1]['str'])


if __name__ == "__main__":
    run()
