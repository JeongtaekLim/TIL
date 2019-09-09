from functools import cmp_to_key

def solution(n, build_frame):
    GIDOONG = 0
    BO = 1
    """
    obj = {
        "start": (0,1),
        "end": (1,1),
        "type: 0
    }
    """
    built = []

    def get_index(start, end, type):
        for index, obj in enumerate(built):
            if obj['start'] == start and obj['end'] == end and obj['type'] == type:
                return index
        return -1

    def is_ok_g(g):
        g_start = g["start"]
        if g["start"][1] == 0:
            return True
        if g["end"][1] > n:
            return False

        filtered_b = list(
            filter(lambda obj: obj["type"] == 1 and
                               (obj["start"] == g_start or
                                obj["end"] == g_start), built))
        if len(filtered_b) > 0:
            return True

        filtered_g = list(filter(lambda obj: obj["type"] == 0 and obj["end"] == g_start, built))
        if len(filtered_g) > 0:
            return True
        return False

    def is_ok_bo(b):
        b_start = b["start"]
        b_end = b["end"]
        if b_end[0] > n:
            return False
        filtered_g = list(filter(
            lambda obj: obj["type"] == 0 and
                        ((obj["end"] == b_start) or
                         (obj["end"] == b_end)), built))
        if len(filtered_g) > 0:
            return True

        filtered_b = list(
            filter(lambda obj: obj["type"] == 1 and
                               (b_start == obj["end"] or
                                b_end == obj["start"]), built))
        if len(filtered_b) >= 2:
            return True
        return False

    def is_ok(insert=True):
        if insert:
            obj = built[-1]
            if obj["type"] == BO:
                passed = is_ok_bo(obj)
            else:
                passed = is_ok_g(obj)

            if not passed:
                return False
            return True

        for obj in built:
            if obj["type"] == BO:
                passed = is_ok_bo(obj)
            else:
                passed = is_ok_g(obj)
            if not passed:
                return False
        return True

    for b in build_frame:
        new_frame = dict()
        new_frame['start'] = (b[0], b[1])
        t = b[2]
        new_frame['type'] = t
        if t == 0:
            new_frame['end'] = (b[0], b[1] + 1)
        else:
            new_frame['end'] = (b[0] + 1, b[1])
        insert = b[3]
        if insert == 1:
            built.append(new_frame)
            if is_ok():
                pass
            else:
                built = built[:-1]
        else:
            index = get_index(new_frame['start'], new_frame['end'], new_frame['type'])
            built = built[:index] + built[index + 1:]
            if is_ok(insert=False):
                pass
            else:
                built.append(new_frame)
    answer = [[obj['start'][0], obj['start'][1], obj['type']] for obj in built]
    answer = sorted(answer, key=cmp_to_key(lambda x, y: x[2] - y[2]))
    answer = sorted(answer, key=cmp_to_key(lambda x, y: x[1] - y[1]))
    answer = sorted(answer, key=cmp_to_key(lambda x, y: x[0] - y[0]))
    return answer


if __name__ == "__main__":
    # solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
    #              [3, 2, 1, 1]])
    # solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
    #              [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
    solution(2, [[0, 0, 0, 1], [0, 1, 0, 1], [0, 2, 0, 1]])
