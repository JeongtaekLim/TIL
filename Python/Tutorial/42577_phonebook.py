from functools import cmp_to_key


def solution(phone_book):
    phone_book = sorted(phone_book, key=cmp_to_key(lambda x, y: len(x) - len(y)))
    for idx, p in enumerate(phone_book):
        filtered = list(filter(lambda x: x[0:len(p)] == p, phone_book[idx+1:]))
        if len(filtered) > 0:
            return False
    return True


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["1", "12"]))
