def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        mylist = array[i-1:j]
        mylist.sort()
        answer.append(mylist[k-1])
    return answer


if __name__ == "__main__":
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
