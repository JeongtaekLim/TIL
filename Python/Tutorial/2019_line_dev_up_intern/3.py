def run():
    # input settings
    n = int(input())
    persons = list()
    time_table = [0 for x in range(151)]
    for i in range(n):
        tmp = input().strip().split(' ')
        tmp = [int(x) for x in tmp]
        persons.append(tmp)

    # iterate persons
    for p in persons:
        for idx in range(p[0], p[1]):
            time_table[idx] += 1
    time_table = sorted(time_table)
    print(time_table[-1])


if __name__ == "__main__":
    run()
